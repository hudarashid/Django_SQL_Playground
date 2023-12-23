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


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    book_summary = models.OneToOneField(
        BookSummary, on_delete=models.DO_NOTHING, blank=True, null=True
    )

    def book_summary_created(self, **kwargs):
        is_new_book_summary = kwargs.get("is_new_book_summary", False)

        if self.book_summary and is_new_book_summary:
            print(f"📚 New book summary {self.book_summary} is created!")

    def save(self, *args, **kwargs):
        is_new_book_summary = kwargs.pop("is_new_book_summary", not bool(self.pk))

        super().save(*args, **kwargs)

        self.book_summary_created(is_new_book_summary=is_new_book_summary)
