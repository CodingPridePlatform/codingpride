from django.shortcuts import render
from .forms import QuestionCreateForm
from .models import *

# Create your views here.
def question(request):
    myTemplate = "pages/question-create.html"
    context = {}
    form = QuestionCreateForm(request.POST or None,)
    
    if form.is_valid():
        form.save()
        context['success_message'] = "Your Question Has Been Submitted Successfully"
        form = QuestionCreateForm()
    context['form'] = form
    return render(request,myTemplate,context)


def list_questions(request):
    all_questions = Question.objects.all().order_by('-id')
    myTemplate = "pages/list-questions.html"
    context = {
        'questions': all_questions,
    }
    return render(request, myTemplate, context)