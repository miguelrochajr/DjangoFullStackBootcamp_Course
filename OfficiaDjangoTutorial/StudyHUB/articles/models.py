from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=400)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, null=False)
