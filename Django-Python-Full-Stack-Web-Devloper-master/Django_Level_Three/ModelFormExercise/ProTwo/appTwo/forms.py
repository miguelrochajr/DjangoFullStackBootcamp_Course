from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User # NOTE: THIS IS NOT AN INSTANCE
        fields = '__all__'
