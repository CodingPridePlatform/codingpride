from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from answer.forms import *

from .forms import QuestionCreateForm
from .models import *


@login_required
def create_edit_question(request, slug=None):

    user = request.user

    if slug:
        obj = get_object_or_404(Question, slug=slug)
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

            form.save_m2m()  # save tags into db

            messages.success(
                request, 'Your Question Has Been Submitted Successfully',
                extra_tags='alert alert-success'
            )

            return redirect(to='question:question-list')

        else:
            messages.error(request, 'Errors occurred',
                           extra_tags='alert alert-danger')
    else:
        form = QuestionCreateForm(instance=obj)

    context = {
        'form': form,
    }

    template_name = 'pages/question_create.html'

    return render(request, template_name, context=context)


def question_list_view(request):
    all_questions = Question.objects.all().order_by('-id')
    paginator = Paginator(all_questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template_name = "pages/question_list.html"
    context = {
        'questions': page_obj,
    }
    return render(request, template_name, context)


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'pages/question_detail.html'
    extra_context = {
        'answer_form': AnswerQuestionForm()
    }


def save_question_like(request):
    if request.method == 'POST':
        questionid = request.POST['questionId']
        question = Question.objects.get(pk=questionid)
        user = request.user
        check = QuestionLike.objects.filter(

            question=question, user=user).count()
        if check > 0:
            return JsonResponse({'bool': False})
        else:
            QuestionLike.objects.create(
                question=question,
                user=user
            )
            return JsonResponse({'bool': True})


class TagDetailView(ListView):
    template_name = 'pages/question_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        tag = self.kwargs['tag']
        questions = Question.objects.filter(tags__slug=tag)
        return questions.order_by('-date_published')


def search(request):
    query = request.GET.get('q', None)
    search_results = Question.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(tags__name__icontains=query)
    )
    context = {
        'questions': search_results,
        'query': query
    }
    return render(request, 'pages/question_list.html', context)
