from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User

def user(request):
    users = User.objects.order_by('date')
    users_dict = {'all_users': users}
    return render(request,'first_app/users.html', context=users_dict)
