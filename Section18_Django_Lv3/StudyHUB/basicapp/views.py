from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name(request):
    form = forms.FormName()
    if request.method == 'POST': #meaning someone hit the submit button and have it posted here
        form = forms.FormName(request.POST)
        if form.is_valid():
            # DO SOME CODE
            print ("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html',{'form':form})
