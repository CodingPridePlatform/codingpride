from django.shortcuts import render

from question.models import Question


# Create your views here.
def home(request):
    all_questions = Question.objects.all().order_by('-id')
    context = {
		'questions': all_questions,
	}

    myTemplate = 'home.html'

    return render(request, myTemplate, context)
    