from rest_framework import viewsets

from book.models import Author, Book
from book.serializers import AuthorSerializer, BookSerializer
from rest_framework.pagination import PageNumberPagination


class BaseNumberPagination(PageNumberPagination):
    page_size = 10


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = BaseNumberPagination


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BaseNumberPagination
