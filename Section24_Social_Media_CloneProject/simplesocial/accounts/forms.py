from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# CAUTION: Double check if your class is NOT the same name
# as UserCreationForm. This would cause confusion on django.
class UserCreateForm(UserCreationForm):
    class Meta:
        #Remmember that the following fields are already defined under
        #contrib.auth
        fields = ('username', 'email', 'password1', 'password2') # These are the fields that our user will have access to type in when signing up
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"
