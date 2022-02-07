from django.urls import path
from . import views


app_name = 'books'
urlpatterns = [
    path('books/',views.BooksListView.as_view(), name='book_all'),
    path('books/<int:id>/', views.BooksDeteilView.as_view(), name='book_deteil'),
    path('books/<int:id>/update/', views.BooksUpdateView.as_view(), name='book_update'),
    path('books/<int:id>/delete/', views.BooksDeleteView.as_view(), name='book_delete'),
    path('add-book/',views.BooksCreateView.as_view(), name='add-book'),
]