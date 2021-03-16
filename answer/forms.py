from django import forms
from .models import *


class AnswerQuestionForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['description']
