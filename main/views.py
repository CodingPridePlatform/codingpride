from django.shortcuts import render
from .forms import QuestionCreateForm



# Create your views here.
def home(request):
    myTemplate = 'home.html'
    return render(request, myTemplate, {})


    
    
    