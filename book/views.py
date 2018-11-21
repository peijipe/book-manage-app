from django.shortcuts import render
from .models import Book


def book_list(request):
    books = Book.objects.all().order_by('published_date')
    return render(request, 'book/book_list.html', {'books': books})

