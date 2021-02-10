from django.shortcuts import render
from .forms import QuestionCreateForm


# Create your views here.
def home(request):
    myTemplate = 'home.html'
    return render(request, myTemplate, {})


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
    
    
    