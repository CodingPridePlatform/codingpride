from uuid import uuid4

from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from question.models import *

User = settings.AUTH_USER_MODEL


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = RichTextUploadingField(blank=False)
    slug = models.SlugField(max_length=250)
    date_answered = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True)

    def __str__(self):
        return str(self.id)
    

    def get_absolute_url(self):
        return reverse('question:question-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify('answer - '+ self.question.title) + "-" + str(uuid4())
        return super().save(*args, **kwargs)
