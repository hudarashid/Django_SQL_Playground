from django.contrib import admin
from book import models

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    model = models.Language

    list_display = ("name",)

class BookAdmin(admin.ModelAdmin):
    model = models.Book



admin.site.register(models.Book)
admin.site.register(models.Language)