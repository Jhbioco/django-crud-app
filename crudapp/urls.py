from django.urls import path
from .views import book_list_view, book_add_view, book_update_view, book_delete_view


urlpatterns = [
    path('', book_list_view, name='book-list'),
    path('books/add/', book_add_view, name='book-add'),
    path('books/update/<int:pk>', book_update_view, name='book-update'),
    path('books/delete/<int:pk>', book_delete_view, name='book-delete'),
]
