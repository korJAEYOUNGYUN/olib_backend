from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer, LibrarySerializer, BookInfoSerializer
from .models import Book, Library, BookInfo


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = []

    def get_queryset(self):
        books = Book.objects.all()

        library = self.request.query_params.get('library')
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        publisher = self.request.query_params.get('publisher')
        published_year = self.request.query_params.get('year')

        if library:
            books = books.filter(library__name__icontains=library)
        if title:
            books = books.filter(book_info__title__icontains=title)
        if author:
            books = books.filter(book_info__author__icontains=author)
        if publisher:
            books = books.filter(book_info__publisher__icontains=publisher)
        if published_year:
            books = books.filter(book_info__published_year=published_year)

        return books


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = []


class BookInfoViewSet(viewsets.ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
