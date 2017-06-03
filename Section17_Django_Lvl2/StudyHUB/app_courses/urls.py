from django.conf.urls import url
from app_courses import views

urlpatterns = [
    url(r'^$', views.users, name='users')
]
