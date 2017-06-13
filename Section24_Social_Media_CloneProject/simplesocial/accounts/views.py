from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy #Reverse lazy we user to say, if someone is logged in or loggin out, where he should actually go
from django.views.generic import CreateView

from accounts import forms
# Create your views here.

class SingUp(CreateView):

    #   Note here that we are NOT instantiating the class. Just passing the reference
    #All we are doing here is that this attritube is equals to that class.
    form_class = forms.UserCreateForm

    # Once somene has signed up for our website. Then, with a succesfull
    #signup, he will be reversed to the login page.
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"
