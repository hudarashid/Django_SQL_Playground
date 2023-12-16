from django.contrib import admin
from book import models


# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    model = models.Language

    list_display = ("name",)


class AuthorAdmin(admin.ModelAdmin):
    model = models.Author


class BookAdmin(admin.ModelAdmin):
    model = models.Book


class BookSummary(admin.ModelAdmin):
    model = models.BookSummary


admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.BookSummary)
admin.site.register(models.Language)
