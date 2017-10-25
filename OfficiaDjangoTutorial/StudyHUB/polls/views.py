from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic


from . import models

# def index(request):
#
#     latest_question_list = models.Question.objects.order_by('-pub_date')[:5] #First five ones
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# # Create your views here.
#
# def detail(request, question_id):
#     question = get_object_or_404(models.Question, pk=question_id)
#     # try:
#     #     question = models.Question.objects.get(pk=question_id)
#     # except models.Question.DoesNotExist:
#     #     raise Http404("Question does not exist!")
#
#     return render(request, 'polls/detail.html', {'question':question})
#
# def results(request, question_id):
#     question = get_object_or_404(models.Question, pk=question_id)
#     return render(request, "polls/results.html", {"question":question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id) # Retrieve the Question object
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # If the try does not raise an exception, it will run!
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
