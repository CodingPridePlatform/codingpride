from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from question.models import *
from .forms import *


@login_required
def answer(request, slug):
    
    if get_object_or_404(Question, slug=slug):
        question = get_object_or_404(Question, slug = slug)
        
    user = request.user

    obj = Answer(author=user)

    if request.POST:
        form = AnswerQuestionForm(request.POST, instance=obj)

        if form.is_valid():
            
            obj = form.save(commit=False)
            obj.question_id = question.id
            obj.author_id = user.id
            obj.save()

            messages.success(
                request, 'Your Answer was Submitted Successfully',
                extra_tags='alert alert-success'
            )

            return redirect('question:question-detail', question.slug)

        else:
            messages.error(request, 'Errors occurred',
                           extra_tags='alert alert-danger')
    else:
        form = AnswerQuestionForm(instance=obj)
    
    template_name = 'pages/question_detail.html'
    context = {
        'form': form,
    }
    
    return render(request, template_name, context)
