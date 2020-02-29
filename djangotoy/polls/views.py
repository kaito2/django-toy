from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request: HttpRequest, question_id: str) -> HttpResponse:
    # TODO: learn how to execute.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', question)


def results(request: HttpRequest, question_id: str) -> HttpResponse:
    return HttpResponse(
        f"You're looking at the results of question {question_id}.")


def vote(request: HttpRequest, question_id: str) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}.")
