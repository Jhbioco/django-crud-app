from django.shortcuts import render, HttpResponseRedirect
from .models import Book
from .forms import BookForm
from django.http import Http404


def book_list_view(request):
    books = Book.objects.all()
    template = 'crudapp/book-list.html'
    return render(request, template, {'books': books})


def book_add_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BookForm()
    template = 'crudapp/book-add.html'
    button_name = 'Add Book'
    return render(request, template, {'form': form, 'button_name': button_name})


def book_update_view(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404(f'The book with the id {pk} does not exists!')
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BookForm(instance=book)
    template = 'crudapp/book-add.html'
    button_name = 'Update Book'
    return render(request, template, {'form': form, 'button_name': button_name})


def book_delete_view(request, pk):
    try:
        Book.objects.get(id=pk).delete()
    except Book.DoesNotExist:
        raise Http404(f'The book with the id {pk} does not exists!')
    return HttpResponseRedirect('/')
