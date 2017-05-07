from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em> My second Project! </em>")

def help(request):
    helpdict = {'help_insert': 'HELP PAGE!'}
    return render(request, 'appTwo/help.html', context=helpdict)

def maria(request):
    mariaDict = {'help_insert': 'Esta é a página de Maria!!'}
    return render(request, 'appTwo/help.html', context=mariaDict)
