from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    holder = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="book_holder")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="book_user")
    published_date = models.DateField(
        blank=True, null=True)
    purchased_date = models.DateField(
        blank=True, null=True)
    isbn = models.BigIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
