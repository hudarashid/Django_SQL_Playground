from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=10)
    iso_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=10)


class BookSummary(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    # whenever this got created(parent), then the book will get updated


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    book_summary = models.OneToOneField(
        BookSummary, on_delete=models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "language"], name="unique_author_language"
            )
        ]
