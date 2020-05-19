from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):

    books = Book.objects.all()

    return render(request, "index.html", {'books': books})

def bookspage(request):

    books = Book.objects.all()

    return render(request, "bookspage.html", {'books': books})

def search(request):

    searchtxt = request.POST['searchtxt']

    books = Book.objects.filter(Q(title__contains=searchtxt) | Q(desc__contains=searchtxt) | Q(category__contains=searchtxt) | Q(author__contains=searchtxt))
    books_count = Book.objects.filter(Q(title__contains=searchtxt) | Q(desc__contains=searchtxt) | Q(category__contains=searchtxt) | Q(author__contains=searchtxt)).count()

    if books_count == 0:    
        messages.info(request, f"Sorry, we couldn't find any results matching '{searchtxt}'")
        # return redirect('bookspage')
        return render(request, "bookspage.html")
       
    else:
        return render(request, "bookspage.html", {'books': books})

def wishlist(request):

    books = Book.objects.all()

    return render(request, "wishlist.html", {'books': books})

