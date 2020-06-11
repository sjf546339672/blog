# coding: utf-8
from django.urls import path
from .views import (test, IndexView, HomeView,
                    DetailView, ArchiversView, WriteView, DeleteView, SearchTagView
                    )

urlpatterns = [
    path('test/', test, name='test'),
    path('index/', IndexView.as_view(), name='index'),
    path('', HomeView.as_view(), name='home'),
    path('<int:id>/', DetailView.as_view(), name='detail'),
    path('archives/', ArchiversView.as_view(), name='archives'),
    path('write/', WriteView.as_view(), name='write'),
    path('delete/<int:id>', DeleteView.as_view(), name='delete'),
    path('search/', SearchTagView.as_view(), name='search'),
]
