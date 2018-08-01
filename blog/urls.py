#coding:utf-8
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name ="post_detail"),
    url(r'^category/(?P<pk>\d+)/$', views.CategoryView.as_view(), name="category"),
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'tag/(?P<pk>\d+)/$', views.TagView.as_view(), name='tag'),
    ]
