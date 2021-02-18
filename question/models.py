import uuid
from uuid import uuid4
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from datetime import datetime

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField(blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")    
    tags = TaggableManager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(default="",max_length=250,editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + "/" + str(uuid.uuid4())
        return super().save(*args, **kwargs)
    