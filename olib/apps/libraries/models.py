from django.db import models

# Todo: 도서관 모델과 책 모델 필요, 도서관 모델은 책 모델과 일대다 관계, 책 모델의 pk에 도서관 id도 포함


class Library(models.Model):
    """ describes a library

    relationship with Book model

    """

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Book(models.Model):
    """ describes each books in a library

    relationship with Library, BookInfo model


    """

    library = models.ForeignKey("Library", on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    book_info = models.ForeignKey("BookInfo", on_delete=models.CASCADE)
    due = models.DateField


class BookInfo(models.Model):
    """ describes book info of a book

    relationship with Book model

    """

    isbn = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_year = models.CharField(max_length=10)
    category = models.CharField(max_length=255)

