from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=10)
    iso_code = models.CharField(primary_key=True, unique=True, max_length=6)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    # language_iso = models.CharField(max_length=6, null=True)
    description = models.TextField()


