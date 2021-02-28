from django.shortcuts import render
from django.core.paginator import Paginator

from question.models import Question


# Create your views here.
def home(request):
    all_questions = Question.objects.all().order_by('-id')
    paginator = Paginator(all_questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
		'questions': page_obj,
	}

    myTemplate = 'home.html'

    return render(request, myTemplate, context)
    