#coding:utf-8
from django.contrib.auth.forms import UserCreationForm
from .models import User

#重写form指定的model模型，并修改默认的显示的字段
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
