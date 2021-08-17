from django.shortcuts import render
from .models import Book, Review


# Create your views here.


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        print(reviews)
    total_books = Book.objects.count()
    return render(request, 'base.html')
