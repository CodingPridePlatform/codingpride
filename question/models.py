from uuid import uuid4

from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

User = settings.AUTH_USER_MODEL


class Question(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)
    description = RichTextUploadingField(blank=False)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="date updated")
    tags = TaggableManager()
    comments = GenericRelation(Comment)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question:question-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + "-" + str(uuid4())
        return super().save(*args, **kwargs)


class QuestionLike(models.Model):
    question = models.ForeignKey(
        Question, related_name='question_likes', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='upvote_user')
