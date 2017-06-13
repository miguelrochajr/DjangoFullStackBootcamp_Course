from django.db import models
from django.contrib import auth # authorization tools

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        # This self.username attritube comes built it
        #in the class auth.models.User
        return "@{}".format(self.username)
