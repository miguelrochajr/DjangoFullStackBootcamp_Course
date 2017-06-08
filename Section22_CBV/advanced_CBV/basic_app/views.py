from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                    ListView, DetailView,
                                    CreateView, UpdateView,
                                    DeleteView)
from basic_app import models
from django.core.urlresolvers import reverse_lazy

# Create your views here.

# def index(request):
#     return render(request, 'index.html')

class SchoolListView(ListView):
    # The ListView is creating a school_list for us and returning
    # It takes the model you called (School), lower cases everythhing
    #and returns a list with school_list
    context_object_name = 'schools' # This will make the class no longer return school_list but
                                    #a object calld schools
    model = models.School

class SchoolDetailview(DetailView):
    #   Differently of the ListView, the DetailView just returns the name in
    #lower case. Here, just school
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolCreateView(CreateView):
    fields = ('name','principal', 'location')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")


class IndexView(TemplateView):

    # This probably happens because, I think, TemplateView is an abstract class.
    template_name = 'index.html' #this is the name of our tamplate. Remmember: this variable HAS to be named template_name !!!!


    # The **kwargs isa call that receives a dictionary of any size.
    # Here it is receiveing all the tags in the HTML file pointed by the variable 'template_name' as the kwargs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) #calls a method from the parent function (super()) called super.context.data()
    #     context['injectme'] = 'BASIC INJECTION!'
    #     return context
