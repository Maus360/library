from django.db import models
from django.urls import reverse

from datetime import datetime


class Person(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        """
        Returns the url to access a particular person instance.
        """
        return reverse("person-detail", args=[str(self.id)])

    def books(self):
        """
        Returns all books, which author is object.
        """
        return Book.objects.filter(author=self.id)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


class Book(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
        Person, on_delete=models.CASCADE, null=False, related_name="books"
    )
    # Foreign Key used because Blog can only have one author/User, but bloggsers can have multiple blog posts.
    description = models.TextField(max_length=2000)
    post_date = models.DateTimeField(default=datetime.today)

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse("book-detail", args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
