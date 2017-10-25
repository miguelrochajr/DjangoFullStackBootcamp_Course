from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #?P<question_id> defines the name that will be used to identify the matched pattern;
    #and [0-9]+ is a regular expression to match a sequence of digits (i.e., a number).


    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
