# Generated by Django 3.1.6 on 2021-02-10 07:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
