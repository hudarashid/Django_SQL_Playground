from faker import Faker


from book import models, serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

faker = Faker()


# TODO: to refactor API View
class BookAPIView(APIView):
    """
    List all book, or create a new book.
    """

    def get(self, request, format=None):
        books = models.Book.objects.all()
        serializer = serializers.BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookSummaryAPIView(APIView):
    """
    Create a new book summary.
    """

    def post(self, request, format=None):
        # Deserialize the request data
        serializer = serializers.BookSerializer(data=request.data)

        if serializer.is_valid():
            # Extract book ID from the request data
            book_id = request.data.get("id")

            if book_id is not None:
                # Retrieve the book by ID
                try:
                    book = models.Book.objects.get(pk=book_id)
                except models.Book.DoesNotExist:
                    return Response(
                        {"error": f"Book with ID {book_id} does not exist."},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                # Check if the book has a summary
                if book.book_summary:
                    # If a summary exists, return the summary data
                    summary_serializer = serializers.BookSummarySerializer(
                        book.book_summary
                    )
                    return Response(summary_serializer.data)

                # If the book does not have a summary, create a new summary
                summary_data = {
                    "title": book.title,
                    "description": faker.text(),
                    "created_by": book.author.id,  # Assuming 'created_by' refers to the author ID
                }

                # Create a new BookSummary instance
                summary_serializer = serializers.BookSummarySerializer(
                    data=summary_data
                )
                if summary_serializer.is_valid():
                    summary_serializer.save()
                    return Response(
                        summary_serializer.data, status=status.HTTP_201_CREATED
                    )
                    ###
                    ### TODO: get the book id and save the book_summary
                    ###

                return Response(
                    summary_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

            # If the request data does not include a book ID, create a new book without a summary
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
