#coding:utf-8
from ..models import Post,Category,Tag
from django.db.models import Count
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month')

@register.simple_tag
def get_categorys():
    return Category.objects.all()

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
