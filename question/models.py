from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from datetime import datetime

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")    
    tags = TaggableManager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.title
    