# api/urls.py
from django.urls import path
from .views import BookAPIView, BookDetail, BookList
from books import views

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),
]