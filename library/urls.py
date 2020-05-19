from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"), 
path("templates/bookspage", views.bookspage, name="bookspage"),
path("templates/search", views.search, name="search"),
path("templates/wishlist", views.wishlist, name="wishlist")
]
