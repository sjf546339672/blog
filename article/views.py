# coding: utf-8
import json

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article


def test(request):
    return render(request, 'home.html')


class IndexView(APIView):
    def get(self, request):
        return Response("Hello World")


class HomeView(View):
    def get(self, request):
        article_list = Article.objects.all()
        return render(request, "home.html", {"article_list": article_list})


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
        data = request.body.decode().split("&")[:3]
        title = data[0].split("=")[1]
        category = data[1].split("=")[1]
        content = data[2].split("=")[1]
        save_data = Article(title=title, category=category, content=content)
        save_data.save()
        article_list = Article.objects.all()
        return render(request, 'home.html', {"article_list": article_list})

