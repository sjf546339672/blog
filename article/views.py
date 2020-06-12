# coding: utf-8
import json

from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from DjangoBlog import settings
from DjangoBlog.celery_tasks.tasks import send_register_active_email
from .models import Article
from urllib.parse import unquote
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def test(request):
    return render(request, 'home.html')


class IndexView(APIView):
    def get(self, request):
        return Response("Hello World")


def check_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class HomeView(View):
    def get(self, request):
        article_list = Article.objects.all()
        pagination = Paginator(article_list, 3)
        page = request.GET.get('page')
        try:
            article_list = pagination.page(page)
        except PageNotAnInteger:
            article_list = pagination.page(1)
        except EmptyPage:
            article_list = pagination.page(pagination.num_pages)
        return render(request, 'home.html', {'article_list': article_list})


class DetailView(View):
    def get(self, request, id):
        try:
            article = Article.objects.get(id=str(id))
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'detail.html', {"article": article})


class ArchiversView(View):
    def get(self, request):
        article_list = Article.objects.all()
        return render(request, 'archives.html', {"article_list": article_list})


class WriteView(APIView):
    def get(self, request):
        return render(request, 'write.html')

    def post(self, request):
        data = request.body.decode().split("&")[:4]
        title = unquote(data[0].split("=")[1]).replace("+", " ")
        category = unquote(data[1].split("=")[1]).replace("+", " ")
        email = unquote(data[2].split("=")[1]).replace("+", " ")
        content = unquote(data[3].split("=")[1])

        result = all([title, category, email, content])
        if result is True:
            if check_email(email) is True:
                save_data = Article(title=title, category=category, content=content, email=email)
                save_data.save()
                article_list = Article.objects.all()
                send_register_active_email(email, title)
                return render(request, 'home.html', {"article_list": article_list})
        return render(request, 'write.html')


class DeleteView(APIView):
    def get(self, request, id):
        Article.objects.filter(id=id).delete()
        article_list = Article.objects.all()
        return render(request, 'home.html', {"article_list": article_list})


class SearchTagView(View):
    def get(self, request):
        category = request.GET.get('kw')
        article_list = Article.objects.filter(category=category)
        if len(article_list) != 0:
            return render(request, 'tag.html', {'article_list': article_list})
        else:
            return redirect('/')
