# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from users.models import User
from django.db import models
from django.utils.six import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.urls import reverse
from django.utils.html import strip_tags
#分类表,python_2_unicode_compatible用于兼容python2
@python_2_unicode_compatible
class Category(models.Model):
    cname = models.CharField(max_length = 100)
   
    def __str__(self):
        return self.cname
    
    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = '分类'
#标签表
@python_2_unicode_compatible
class Tag(models.Model):
    tname = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.tname

    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = '标签'
#文章表
@python_2_unicode_compatible
class Post(models.Model):
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank = True)
    title = models.CharField(max_length = 70)
    body = UEditorField('内容', max_length = 20000, imagePath='images/', filePath='files/', default = u'', blank = True, width=600, height=800)
    excerpt = models.CharField(max_length = 200, blank = True)#摘要
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User)
    
    #点击
    clickCount = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs = {'pk':self.pk})

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:54]
            super(Post,self).save(*args,**kwargs)

    class Meta:
        db_table = 'post'
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-create_time']
