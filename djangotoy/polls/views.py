from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html',
                  {'latest_question_list': latest_question_list})


def detail(request: HttpRequest, question_id: str) -> HttpResponse:
    # TODO: learn how to execute.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: str) -> HttpResponse:
    return HttpResponse(
        f"You're looking at the results of question {question_id}.")


def vote(request: HttpRequest, question_id: str) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}.")
