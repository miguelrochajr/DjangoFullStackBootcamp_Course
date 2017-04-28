from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]
