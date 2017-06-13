from django.conf.urls import url
from django.contrib.auth import views as auth_views # Here dJango 1.11 introduces a login in vew and a logout view
from accounts import views #My own views

app_name = 'accounts' #in case I want to use the url templates

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),
                name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), # the logout view has a default one
                name='logout'), #this will essentially come back to the home page when we logout
    url(r'signup/$', views.SingUp.as_view(),name='signup'),

]
