"""StudyHUB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from first_app import views


# The include() function allows us to look for a match with regular expressions and link back to our application’s own urls.py file.
# That wey, each application has its own urls.py file. We will have to manually create an urls.py file on each application.
urlpatterns = [
    url(r'^$', views.index, name='index'),          #here, when it finds a empty line, calls the views.index function
    url(r'^first_app/', include('first_app.urls')),
    url(r'^help/', include('first_app.urls')),
    url(r'^admin/', admin.site.urls),
]


# see video at 2.16 to see explanation of include()
