from django.shortcuts import render
from django.http import HttpResponse
#from appTwo.models import User
from appTwo.forms import FormSubscription
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form = FormSubscription() #instatiate a FormSubscription class
    if request.method == 'POST':
        form = FormSubscription(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request) #this will take you back to the index page
        else:
            print("ERROR FORM INVALID")
    # REMIND: The form dictionary has to match the one in the HTML file!
    return render(request, 'appTwo/users.html',{'form': form})
