from django.urls import path

from book import views

urlpatterns = [
    path("book/<int:pk>/", views.BookDetailAPIView.as_view()),
    path("book-summary/<int:pk>/", views.BookSummaryAPIView.as_view()),
]
