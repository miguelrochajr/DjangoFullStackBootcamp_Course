from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='list'),
                                              # This name List is for the URL template tag
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailview.as_view(), name='detail'),
    #   <pk> - primary key
    #   [-\w+] alphanumeric (alphabetic and numeric) characters
    #   primary key followed by one or more alphanumeric number
    url(r'^create/', views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]
