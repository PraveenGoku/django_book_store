from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('-rating')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating')) # rating__avg, rating__min, rating__max
    
    return render(request, 'book_outlet/index.html',{
        'books': books,
        "total_books": num_books,
        "avg_rating": avg_rating['rating__avg'],
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id) #pk=primary key
    # except:
    #     raise Http404("Book not found")
    book = get_object_or_404(Book, slug=slug) # This is a shortcut to handle the exception
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestselling': book.is_bestselling
    })