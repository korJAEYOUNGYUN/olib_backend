from rest_framework import serializers

from .models import Library, BookInfo, Book


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    library = LibrarySerializer()
    book_info = BookInfoSerializer()

    class Meta:
        model = Book
        fields = '__all__'
