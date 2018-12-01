from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'holder', 'user', 'published_date', 'purchased_date', 'isbn', 'comment',)
