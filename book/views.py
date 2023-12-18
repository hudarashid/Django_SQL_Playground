from faker import Faker

from book import models, serializers

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, exceptions

faker = Faker()


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get book detail by id
    """

    response_serializer = serializers.BookSerializer

    def get_book(self, pk):
        try:
            return models.Book.objects.get(pk=pk)
        except models.Book.DoesNotExist:
            raise exceptions.NotFound(detail=f"Book with id: {pk} does not exist.")

    def get(self, request, pk, format=None):
        book = self.get_book(pk)
        serializer = self.response_serializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookSummaryAPIView(RetrieveUpdateDestroyAPIView):
    """
    Create a new book summary.
    """

    response_serializer = serializers.BookSummarySerializer

    def get_book(self, pk):
        try:
            return models.Book.objects.get(pk=pk)
        except models.Book.DoesNotExist:
            raise exceptions.NotFound(detail=f"Book with id: {pk} does not exist.")

    def post(self, request, pk, format=None):
        book = self.get_book(pk)

        # Check if the book has a summary
        if not book.book_summary:
            # If the book does not have a summary, create a new book summary
            book_summary = models.BookSummary.objects.create(
                title=book.title, description=faker.text(), created_by=book.author
            )

            book.book_summary = book_summary
            book.save(is_new_book_summary=True)

        summary_serializer = self.response_serializer(book.book_summary)

        return Response(summary_serializer.data, status=status.HTTP_200_OK)
