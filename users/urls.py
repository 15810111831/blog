#coding:utf-8
from django.conf.urls import url
from .import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
        ]
