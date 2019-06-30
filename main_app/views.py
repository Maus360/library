from main_app.models import Person, Book
from rest_framework import viewsets
from main_app.serializers import PersonSerializer, BookSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
