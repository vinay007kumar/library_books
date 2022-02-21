# books/urls.py
from django.urls import path
from books import views

from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view()),
  
]