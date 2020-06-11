# coding: utf-8
from rest_framework import serializers
from . import models


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = models.Article
        fields = ("title", "category", "date_time", "content")





