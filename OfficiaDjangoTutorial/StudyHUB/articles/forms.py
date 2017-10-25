from django import forms
from django.forms import formset_factory, modelformset_factory
from polls import models as pollsModels
from articles import models as articlesModels

AuthorFormset = modelformset_factory(pollsModels.Author, fields=('name','title'))

class ArticleForm(forms.ModelForm):
    class Meta():
        model = articlesModels.Article
        fields = ['title','pub_date']

class AuthorForm(forms.ModelForm):
    class Meta():
        model = articlesModels.Author
        fields = ['name']


class BaseArticleFormset(forms.BaseFormSet):
    def clean(self):
        """Validade the data"""
        if any(self.errors):
            print("Erros found")
            # Don't bother validating the formset unless each form is valid on its own
        titles = []
        for form in self.forms:
            title = form.cleaned_data['title']
            if title in titles:
                raise forms.ValidationError("Articles in a set must have different titles.")
            titles.append(title)
