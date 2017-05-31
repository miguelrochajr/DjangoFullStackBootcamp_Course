from django.db import models

class Topic(models.Model): #the name of the class is the name of the table on the database
    top_name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic) #this is essentialy the pages on the top of the Webpage
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date) #since the date has its own scruture, it has to be casted to a string.
