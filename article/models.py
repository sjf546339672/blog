# coding: utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100)
    content = RichTextUploadingField()
    comments = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
