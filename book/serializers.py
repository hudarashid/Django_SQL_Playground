from book import models
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class BookSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookSummary
        fields = "__all__"
