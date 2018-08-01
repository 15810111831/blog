# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'create_time', 'update_time', 'clickCount']
    list_per_page = 30
    search_fileds = ['title']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
