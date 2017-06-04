from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NEED TO START WITH Z!")

class FormName(forms.Form):
    # name = forms. CharField(validators=[check_for_z]) # this will send the validator to the CharField.
    name = forms.CharField()
    email = forms.EmailField()
    # email checking. Like when the website asks you to validade your email
    verify_email = forms.EmailField(label='Enter your email again')

    text = forms.CharField(widget=forms.Textarea)


    #you want to clear the entire form
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure your emails match")

    # # The botcatcher will not be shown to the user. It is just an HTML that bots can read
    # # but human users cannot
    # botcatcher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)]) #django built in validadors
    #                             # this validators parameter will replace all the code we made on the method clean_botcatcher
    #                             # you can pass more than one validaros. Note that it receives an Array of validadors


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
