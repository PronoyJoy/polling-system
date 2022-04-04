from multiprocessing import context
from urllib import response
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader
# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([a.question_text for a in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    # template = loader.get_template('polls\index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context,request))
    #shotcut render
    return render(request,'polls/index.html',context)



def owner(request):
       return HttpResponse("Hello, world. 077bc03b is the polls index.")


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)

    # except Question.DoesNotExist:
        
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'polls/detail.html', context)



def results(request, question_id):
    responsed = "You're looking at the results of question %s."
    return HttpResponse(responsed % question_id)

def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse( response % question_id)




