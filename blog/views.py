# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView,DetailView
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from models import *
from django.views.decorators.cache import cache_page
import datetime
from comments.forms import CommentForm
from django.db.models import Q

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 2

class CategoryView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk = self.kwargs.get('pk'))
        return super(CategoryView,self).get_queryset().filter(category=cate)

def post_detail(request, pk):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post,pk=pk)
    #此处可以使用celery异步进行存储
    post.clickCount +=1
    post.save()

    context = {}
    comment_list = post.comment_set.all()
    form = CommentForm()
    categorys = Category.objects.all()
    context['post'] = post
    context['form'] = form
    context['comment_list'] = comment_list
    context['categorys'] = categorys
    return render(request,template_name,context)

#def category_list(request, category_id):
 #   template_name = 'blog/category.html'
    #categorys = Category.objects.all()
  #  cate = get_object_or_404(Category,pk = category_id)
   # post_list = Post.objects.filter(category=cate)
    #context = {}
    #context['categorys'] = categorys
   # context['post_list'] = post_list
   # return render(request, template_name, context)

#归档
class ArchivesView(ListView):
    model = Post
    template_name = 'blog/archives.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return super(ArchivesView,self).get_queryset().filter(create_time__year = self.kwargs.get('year'))

#标签云
class TagView(ListView):
    model = Post
    template_name = 'blog/tag.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag,pk = self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(tags=tag)

#全文检索
def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'index.html', context = {'error_msg':error_msg})
    
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'index.html', context = {'error_msg':error_msg,
        'post_list':post_list
        })
