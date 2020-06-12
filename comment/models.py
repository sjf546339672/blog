from django.db import models

from article.models import Article


class CommentModel(models.Model):
    content = models.CharField(max_length=500)
    comment_id = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = verbose_name

