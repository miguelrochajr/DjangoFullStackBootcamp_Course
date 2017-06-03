from django.shortcuts import render
from django.http import HttpResponse
from app_courses.models import User

# Create your views here.

def index(request):
    return render(request, 'app_courses/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'app_courses/users.html', context=user_dict)
