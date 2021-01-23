from django.shortcuts import render

# Create your views here.
def home(request):
    myTemplate = 'pages/home.html'
    return render (request, myTemplate, {})
