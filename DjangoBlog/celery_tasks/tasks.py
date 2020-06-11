# coding: utf-8
import time
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery


app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/8')


@app.task
def send_register_active_email(email, title):
    subject = "博客之家欢迎信息"
    message = ""
    sender = settings.EMAIL_FROM
    receiver = [email]
    html_message = "<h1>恭喜您创建了名称叫做{}的博文</h1>".format(title)
    send_mail(subject, message, sender, receiver, html_message=html_message)
