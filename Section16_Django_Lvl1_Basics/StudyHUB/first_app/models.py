from django.db import models

class Topic(models.Model):                                      #the name of the class is the name of the table on the database
    top_name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)                            #this is essentialy the pages on the top of the Webpage
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()
    def __str__(self):
        return str(self.date) #since the date has its own scruture, it has to be casted to a string.

class User(models.Model):
    email = models.CharField(max_length=264, unique=True)
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)

    def __str__(self):
        return self.first_name


# to save these modifications you must type the following commands:
#
# $ python manage.py migrate
#
# this will create your sqlite database using the models definede here at models.py
# To also save this changes to our applications, type the following command:
#
# python manage.py makemigrations <your app name>
#
# after the makemigrations, just run the manage.py migrate again
