from django import forms
# from .models import Book


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ('isbn', 'comment',)

LIBRARIES_CHOICES = (
    ('国立図書館', '国立図書館'),
    ('県立図書館', '県立図書館'),
    ('市立図書館', '市立図書館'),
)


class BooksForm(forms.Form):
    title = forms.CharField(
        label='タイトル',
        max_length=200,
        required=True,
    )

    author = forms.CharField(
        label='著者',
        max_length=50,
        required=True,
    )

    holder = forms.ChoiceField(
        label='所有者',
        widget=forms.Select,
        choices=LIBRARIES_CHOICES,
        required=True,
    )

    user = forms.CharField(
        label='貸出先',
        max_length=50,
        required=True,
    )

    published_date = forms.DateTimeField(
        label='発刊日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )

    purchased_date = forms.DateTimeField(
        label='購入日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )

    isbn = forms.IntegerField(
        label='isbn',
        required=False,
    )

    comment = forms.CharField(
        label='備考',
        max_length=1000,
        required=False,
        widget=forms.TextInput()
    )
