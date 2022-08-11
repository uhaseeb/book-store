from django.shortcuts import render, get_object_or_404
from .models import Books
from django.db.models import Avg


def index(request):
    all_books = Books.objects.all().order_by('-rating')
    total_books = all_books.count()
    average_book_rating = all_books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {"all_books": all_books, "total_books": total_books,
                                                      "average_book_rating": average_book_rating})


def book_details(request, slug):
    # book = Books.objects.get(pk=id)
    book = get_object_or_404(Books, slug=slug)
    return render(request, 'book_outlet/book-details.html', {"author": book.author, "title": book.title,
                                                             "rating": book.rating,
                                                             "is_bestselling": book.is_bestselling})
