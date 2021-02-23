from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

from .forms import QuestionCreateForm
from .models import *


@login_required
def create_edit_question(request, id=None):

	user = request.user

	if id:
		obj = get_object_or_404(Question, id=id)
		if obj.author != user:
			return HttpResponseForbidden()
	else:
		obj = Question(author=user)

	if request.POST:
		form = QuestionCreateForm(request.POST, instance=obj)

		if form.is_valid():
			obj = form.save(commit=False)
			obj.author_id = user.id
			obj.save()

			form.save_m2m() #save tags into db
					
			messages.success(request, 'Your Question Has Been Submitted Successfully', extra_tags='alert alert-success')

			return redirect(to='question:qn-create')

		else:
			messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')
	else:
		form = QuestionCreateForm(instance=obj)
	
	context = {
		'form': form,
	}

	template_name = 'pages/question_create.html'

	return render(request, template_name, context=context)


def list_questions(request):
	all_questions = Question.objects.all().order_by('-id')
	myTemplate = "pages/list_questions.html"
	context = {
		'questions': all_questions,
	}
	return render(request, myTemplate, context)


class QuestionDetailView(DetailView):
	model = Question
