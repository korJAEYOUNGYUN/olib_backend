from django.db import models


class Library(models.Model):
    """ describes a library

    relationship with Book model

    """

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return '%d:%s' % (self.id, self.name)


class Book(models.Model):
    """ describes each books in a library

    relationship with Library, BookInfo model


    """

    library = models.ForeignKey("Library", on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    book_info = models.ForeignKey("BookInfo", on_delete=models.CASCADE)


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

    def __str__(self):
        return '%d:%s' % (self.id, self.title)
