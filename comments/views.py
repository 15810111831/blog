# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, get_object_or_404
from .forms import CommentForm
from blog.models import Post

def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    
    if request.method == 'POST':
        print 'POST方法进入'
        if form.is_valid():
            print '评论成功'
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            #这里redirect重定向，可以接收模型对象，但是该
            #模型对象必须实现get_absolute_url方法,redirect
            #会自动调用该方法
            return redirect(post)
        else:
            '评论验证未通过'
            #如果数据验证不通过，则重新渲染页面
            comment_list = post.comment_set.all()
            context = {
                    'post':post,
                    'comment_list':comment_list,
                    'form':form
                    }
            return render(request, 'blog/detail.html', context)
    
    return redirect(post)
