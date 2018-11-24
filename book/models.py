from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    NATIONAL = '国立図書館'
    PREFECTURAL = '県立図書館'
    CITY = '市立図書館'
    LIBRARY_CHOICES = (
        (NATIONAL, '国立図書館'),
        (PREFECTURAL, '県立図書館'),
        (CITY, '市立図書館'),
    )
    holder = models.CharField(
        max_length=10,
        choices=LIBRARY_CHOICES,
    )

    user = models.CharField(max_length=50, default='admin')
    published_date = models.DateField(
        blank=True, null=True)
    purchased_date = models.DateField(
        blank=True, null=True)
    isbn = models.BigIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
