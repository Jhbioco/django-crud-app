from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    page_number = models.IntegerField()
    author = models.CharField(max_length=125)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
