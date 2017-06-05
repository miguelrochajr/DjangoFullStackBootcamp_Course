from django.conf.urls import url
from basic_app import views

# TEMPALTE TAGGING
# This basic_app needs to match the one in the URL tagging.
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
