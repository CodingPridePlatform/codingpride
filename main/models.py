from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")    
    tags = TaggableManager()

    def __str__(self):
        return self.title