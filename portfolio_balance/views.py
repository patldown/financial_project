from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

def index(request):
    ### Add latest_question_list to grab last 5 questions after ordering
    # by date
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    ### Here we add reference to template, which we do not need
    #template = loader.get_template('portfolio_balance/index.html')
    context = {
            'latest_question_list': latest_question_list,
            }
    ### The below comment shows the HttpResponse v. the next used line
    # return HttpResponse(template.render(context, request))
    return render(request, 'portfolio_balance/index.html', context)
    # Commented out the bottom line as we are adding more
    #return HttpResponse("<h1>Portfolio (Re)Balancing Application</h1>")

def detail(request, question_id):
    ### Error handling has been done here:
    
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist.")
    
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'portfolio_balance/detail.html', {'question': question})

def results(request, question_id):
    response = "<h1>You're looking at the results of question %s.</h1>"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'portfolio_balance/detail.html', {
                'question':question,
                'error_message':"You didn't select a choice.",
                })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('portfolio_balance:results', args=(question.id,)))


