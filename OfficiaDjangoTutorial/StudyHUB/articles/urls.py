from django.conf.urls import url

from articles import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
