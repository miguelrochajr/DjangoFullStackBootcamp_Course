import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','StudyHUB.settings')

import django
django.setup()


# FAKE POPULATION SCRIPTS

import random
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace','News', 'Games'] #various types for different websites

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] # retreave the topic (if exsits), if not will created
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()

        #create fake data for that entry
        fake_url = fakegen.url()
        fake_date= fakegen.date()
        fake_name= fakegen.company()
        fake_firstname= fakegen.first_name()
        fake_lastname=  fakegen.last_name()
        fake_email = fakegen.email()


        # Create thte new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0] #note that the topic is a ForeignKey, so it is passed then entire instantiated object

        # create fake access record for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        #create fake Users
        users = User.objects.get_or_create(first_name=fake_firstname, last_name=fake_lastname, email=fake_email)[0]

if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete')
