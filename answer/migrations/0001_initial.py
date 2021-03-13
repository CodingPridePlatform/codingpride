# Generated by Django 3.1.7 on 2021-03-13 21:20

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0002_auto_20210313_2326'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(max_length=250)),
                ('date_answered', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question')),
            ],
        ),
    ]