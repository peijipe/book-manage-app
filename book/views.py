from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BooksForm
from django.contrib.auth.decorators import login_required


def book_list(request):
    books = Book.objects.all().order_by('published_date')
    return render(request, 'book/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})


# def book_new(request):
#     if request.method == "POST":
#         form = BooksForm(request.POST)
#         if form.is_valid():
#             book = form.save()
#             book.save()
#             return redirect('book:book_detail', pk=book.pk)
#
#     else:
#         form = BooksForm()
#     return render(request, 'book/book_new.html', {'form': form})

@login_required
def book_new(request):
    form = BooksForm(request.POST or None)
    if form.is_valid():
        book = Book()
        book.title = form.cleaned_data['title']
        book.author = form.cleaned_data['author']
        book.holder = form.cleaned_data['holder']
        book.user = form.cleaned_data['user']
        book.published_date = form.cleaned_data['published_date']
        book.purchased_date = form.cleaned_data['purchased_date']
        book.isbn = form.cleaned_data['isbn']
        book.comment = form.cleaned_data['comment']

        Book.objects.create(
            title=book.title,
            author=book.author,
            holder=book.holder,
            user=book.user,
            published_date=book.published_date,
            purchased_date=book.purchased_date,
            isbn=book.isbn,
            comment=book.comment,
        )
        return redirect('book:book_list')
    return render(request, 'book/book_new.html', {'form': form})


# def book_edit(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         form = BooksForm(request.POST, instance=book)
#         if form.is_valid():
#             book = form.save()
#             book.save()
#             return redirect('book:book_detail', pk=book.pk)
#     else:
#         form = BooksForm(instance=book)
#     return render(request, 'book/book_edit.html', {'form': form, 'pk': pk})

@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            book = Book()
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.holder = form.cleaned_data['holder']
            book.user = form.cleaned_data['user']
            book.published_date = form.cleaned_data['published_date']
            book.purchased_date = form.cleaned_data['purchased_date']
            book.isbn = form.cleaned_data['isbn']
            book.comment = form.cleaned_data['comment']

            Book.objects.filter(pk=pk).update(
                title=book.title,
                author=book.author,
                holder=book.holder,
                user=book.user,
                published_date=book.published_date,
                purchased_date=book.purchased_date,
                isbn=book.isbn,
                comment=book.comment,
            )
            book = get_object_or_404(Book, pk=pk)
            return render(request, 'book/book_detail.html', {
                'book': book,
                'pk': pk,
            })

    else:
        data = {
            'title': book.title,
            'author': book.author,
            'holder': book.holder,
            'user': book.user,
            'published_date': book.published_date,
            'purchased_date': book.purchased_date,
            'isbn': book.isbn,
            'comment': book.comment,
        }
        form = BooksForm(data)
    return render(request, 'book/book_edit.html', {
        'form': form,
        'pk': pk
    })


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book:book_list')
    return render(request, 'book/book_confirm_delete.html', {'book': book})
