from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.http import HttpResponse, Http404, HttpResponseRedirect

from polls import models as pollsModels

from articles import forms
from articles import models

import datetime

def index(request):
    inlineArticleFormSet = inlineformset_factory(models.Author, models.Article,
                                                fields=('title',))
    ArticleFormSet = formset_factory(forms.ArticleForm,
                                      extra=2,
                                      validate_max=True)

    formset_articles = ArticleFormSet(prefix="articles")
    form_author = forms.AuthorForm(prefix="author")

    if request.method == 'POST':
        print("POST RECEIVED")

    return render(request, 'articles/articles.html',
                    {'form_author':form_author,
                     'formset_articles': formset_articles})
