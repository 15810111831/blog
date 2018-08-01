# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

#扩展默认的USER模型,增加昵称，头像，以及签名
class User(AbstractUser):
    nickname = models.CharField(max_length = 50, blank = True)
    sign = models.CharField(max_length = 1000, blank = True)
    head_img = models.ImageField(upload_to = 'images',blank = True)

    class Meta(AbstractUser.Meta):
        pass
