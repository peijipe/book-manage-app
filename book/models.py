from django.db import models


class Book(models.Model):
    LIBRARY_CHOICES = (
        ('国立図書館', '国立図書館'),
        ('県立図書館', '県立図書館'),
        ('市立図書館', '市立図書館'),
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    holder = models.CharField(
        max_length=10,
        choices=LIBRARY_CHOICES,
    )
    user = models.CharField(max_length=50)
    published_date = models.DateField(
        blank=True, null=True)
    purchased_date = models.DateField(
        blank=True, null=True)
    isbn = models.BigIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
