from django import forms
from django.core import validators

# Custom validor with django built-in validatin
def check_for_z(value):
    if value[0] != 'z':
        raise forms.ValidationError('THE NAME NEEDS TO START WITH Z!')

class CreateOS(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter you email again')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])# Django built in valitadors

    # Custom validador
    # Note that django looks for a matehod written as clean_attribute
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        # If the botcatcher field was filled
        if len(botcatcher) > 0:
            raise forms.ValidationError("GO TO HELL, BOT!")


    # Grab all clean data at once
    # Note that this method is called automatically by django. The code does not raise it.
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Make sure the emails match!")
