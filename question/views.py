from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden,JsonResponse
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
    template_name = 'pages/question_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView,self).get_context_data(**kwargs)
        id = self.kwargs.get(self.pk_url_kwarg,None)
        question = Question.objects.get(id=id)
        question_like = QuestionLike.objects.filter(question=question).count()    
        context["question_like"] = question_like
        return context

def save_question_like(request):
    if request.method=='POST':
        questionid=request.POST['questionId']
        question=Question.objects.get(pk=questionid)
        user=request.user
        check=QuestionLike.objects.filter(question=question,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            QuestionLike.objects.create(
                question=question,
                user=user
            )
            return JsonResponse({'bool':True})