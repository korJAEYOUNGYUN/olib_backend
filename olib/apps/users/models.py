from django.contrib.auth.models import User
from django.db import models


class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('libraries.Book', on_delete=models.CASCADE)
    borrowed_at = models.DateField(auto_now_add=True)
    due = models.DateField(null=True, blank=True)
    returned_at = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
