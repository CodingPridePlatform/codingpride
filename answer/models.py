from uuid import uuid4

from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from question.models import *

User = settings.AUTH_USER_MODEL


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    description = RichTextUploadingField(blank=False)
    slug = models.SlugField(max_length=250)
    date_answered = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.question.title + " - " + "Answer" + " - " + str(self.id)

    def save(self, *args, **kwargs):
        self.slug = slugify(
            'answer - ' + self.question.title) + "-" + str(uuid4())
        return super().save(*args, **kwargs)
