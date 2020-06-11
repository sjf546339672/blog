# coding: utf-8
from django.db import models

from DjangoBlog import settings


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']