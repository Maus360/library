import sys

from main_app.models import Person, Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("name", "author", "description")


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    # book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ("name", "books")
