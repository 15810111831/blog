# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import RegisterForm

def index(request):
    return render(request, 'index.html')

def register(request):
    redirect_to = request.POST.get('next',request.GET.get('next','')) 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print form.is_valid()
        if form.is_valid():#判断form数据是否合法
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
        else:
            error = u'注册失败'
            return render(request, 'users/register.html', context = {'form':form, 'error':error})
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', context = {'form': form, 'next':redirect_to})

