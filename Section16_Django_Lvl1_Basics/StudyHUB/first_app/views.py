from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage, User
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'insert_me': "Hello, I am from fristapp/index.html!", #the key must match the django TAG on the HTML template that we created under the templates folder.
            }
    # Note: for the render function, it is fine to put the forward slash. Because this is what the BROWSER will read it.
    return render(request, 'first_app/index.html', context=date_dict) # the request, the file itself in HTML, contect will link up what we are pasing to the HTML file
    # return HttpResponse("Hello World!") # each view exists in the app as its own individual function
    #                                     # now we just creat one view called index
    #                                     # each view must return an HttpResponse object. And each one of those objects
    #                                     # will take a string paratemetr representing the contets of the page.
    #                                     # In order to see this view, we need to map it into our url.py file.

def help(request):
    helpdic = {'help_insert': "HELP PAGE"}
    return render(request, 'first_app/help.html', context=helpdic)

def information(request):
    helpdic = {'help_insert': "INFO PAGE!"}
    return render(request, 'first_app/help.html', context=helpdic)

def user(request):
    users = User.objects.order_by('date')
    users_dict = {'all_users': users}
    return render(request,'first_app/index.html', context=users_dict)
