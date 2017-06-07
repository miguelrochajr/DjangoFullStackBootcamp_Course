from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return render(request, 'index.html')

class CBView(View):
    def get(self,request):
        return HttpResponse("LASS BASED VIEWS ARE COOL!")
