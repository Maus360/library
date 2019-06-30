from django.test import TestCase

# Create your tests here.

from main_app.models import Person, Book


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        person = Person.objects.create(name="Bob")

    def test_get_absolute_url(self):
        print(Person.objects.all())
        person = Person.objects.get(id=1)
        self.assertEquals(Person.get_absolute_url(), "/person/1/")

    def test_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field("name").max_length
        self.assertEquals(max_length, 20)


import datetime


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        book_author = Person.objects.create(name="Bob")
        book = Book.objects.create(
            name="Test Book 1",
            author=book_author,
            description="Test Book 1 Description",
        )

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), "/book/1/")

    def test_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("name").max_length
        self.assertEquals(max_length, 200)

    def test_description_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_description_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("description").max_length
        self.assertEquals(max_length, 2000)

    def test_date_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("post_date").verbose_name
        self.assertEquals(field_label, "post date")

    def test_object_name(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.name
        self.assertEquals(expected_object_name, str(book))
