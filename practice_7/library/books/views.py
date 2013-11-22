# Create your views here.
from books.models import Author
from books.models import Book
from django.views.generic import ListView
from django.views.generic import DetailView
import datetime


class BookList(ListView):
    model = Book
    context_object_name = 'books'


class AuthorList(ListView):
    model = Author
    context_object_name = 'authors'


class BookDetail(DetailView):
    queryset = Book.objects.all()


class AuthorDetail(DetailView):
    queryset = Author.objects.all()
