from django import forms
from appTwo.models import User
from django.core import validators

# Note here that we inherit from a different part of forms. This is
# due to our purpose: to link to an Model class

class FormSubscription(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' #since we are using it all the attributes from the model, we use this special keyword
