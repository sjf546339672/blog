from urllib.parse import unquote

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from comment.models import CommentModel


def index(request):
    return HttpResponse(1111)


class SumbitComment(View):
    def post(self, request, id):
        body = request.body.decode().split("&")[:1]
        comment_info = unquote(body[0].split("=")[1]).replace("+", " ")
        save_data = CommentModel(content=comment_info, comment_id_id=id)
        save_data.save()
        comment_list = CommentModel.objects.filter(comment_id_id=id)
        print("===================comment_list", comment_list)
        return render(request, 'detail.html', {"comment_list": comment_list})

    def get(self, request):
        return redirect(render(request, 'detail.html'))
