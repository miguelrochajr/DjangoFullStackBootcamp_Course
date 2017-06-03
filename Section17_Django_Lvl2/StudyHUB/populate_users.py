import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','StudyHUB.settings')

import django
django.setup()


# FAKE POPULATION SCRIPTS

import random
from app_courses.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5): #Remmember that N=5 is just the default value. You can put whaever you want here.
    for entry in range(N):

        #create fake data for that entry
        fake_firstname= fakegen.first_name()
        fake_lastname=  fakegen.last_name()
        fake_email = fakegen.email()

        # An alternative to filling the name is to split a name:
        # fake_name = fakegen.name().split()
        # fake_firstname= fake_name[0]
        # fake_lastname=  fake_name[1]

        #create fake Users
        users = User.objects.get_or_create(first_name=fake_firstname, last_name=fake_lastname, email=fake_email)[0]

if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete')
