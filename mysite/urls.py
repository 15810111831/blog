#coding:utf-8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
#from users import views
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'users/', include('users.urls')),
    #引入django auth中的url
    url(r'users/', include('django.contrib.auth.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'ueditor/', include('DjangoUeditor.urls')),
    url(r'blog/',include('blog.urls',namespace = 'blog')),
    url(r'', include('comments.urls', namespace = 'comment')),
    url(r'^search/$', include('haystack.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
