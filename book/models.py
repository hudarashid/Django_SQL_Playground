from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=10)
    iso_code = models.CharField(max_length=6)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=10)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    description = models.TextField()

    class Meta:
        constraints = [
                models.UniqueConstraint(
                    fields=['author', 'language'],
                    name='unique_author_language'
                )
            ]

