from django import forms
from .models import Question


class QuestionCreateForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'description', 'tags']