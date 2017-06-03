from django.db import models

# Create your models here.
#Note here that we aways inherit from models.Model
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.first_name
