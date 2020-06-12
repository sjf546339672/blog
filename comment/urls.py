# coding: utf-8
from django.urls import path

from comment.views import index, SumbitComment

app_name = 'comments'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', SumbitComment.as_view(), name='submit_comment'),
]


