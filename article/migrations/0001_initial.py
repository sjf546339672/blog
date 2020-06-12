# Generated by Django 3.0.5 on 2020-06-12 14:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('date_time', models.DateField(auto_now_add=True)),
                ('email', models.CharField(max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]
