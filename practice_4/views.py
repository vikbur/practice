#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from library.models import Book, Author
from django.template import Context, Template

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def books(request):
    books = Book.objects.all()
    return render_to_response('books.html', {'books': books})


def book(request, book_id):
    book_card = Book.objects.get(id=book_id)
    return render_to_response('book_card.html', {'book_card': book_card})


def authors(request):
    authors = Author.objects.all()
    return render_to_response('authors.html', {'authors': authors})


def author(request, author_id):
    author = Author.objects.get(id=author_id)
    return render_to_response('author_card.html', {'author': author})