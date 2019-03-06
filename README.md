### 安装python 和 pip 
1. [安装教程](https://blog.csdn.net/lijunweiyhn/article/details/79037445)
2. 安装完毕后执行 `pip install -r requirements.txt`

### 安装Git
1. [Git安装教程](https://www.cnblogs.com/wj-1314/p/7993819.html)
2. 创建个项目文件夹, 进入文件夹之后执行 `git clone https://github.com/15810111831/django-project.git`

### 安装mysql数据库,并配置环境变量
1. [mysql 安装教程](https://blog.csdn.net/kan2016/article/details/80876722)

### 进入mysql 
1. `mysql -uroot -p`
2. `create database fruit charset=utf8mb4;` 创建数据库表

### 退出mysql, 进入项目目录, 同级文件有manage.py
3. 退出mysql,执行 `python manage.py migrate` 同步数据库
4. 执行 `python manage.py createsuperuser` 创建超级管理员
5. 执行 `python manage.py runserver 0.0.0.0:8000` 启动服务


django auth 总结

1. 如果需要自定义字段，那么需要继承django.conftrib.auth.models.AbstracUser类
    并且设置默认class Meta(AbstracUser.Meta),最后一定要在settings中重新设置
    AHTO_USER_MODEL = 自定义的model

2. 编写自定义User的表单，因为默认继承的是auth.User需要改为自己自定义的User
    同样django.confrib.auth.forms import UserCreateForm定义了默认表单，但是
    fields默认只有username，如果需要添加别的则可以设置fields字段,并且指定model
    为自定义的User

3. 因为django.auth.user.urls中定义了登陆以及密码修改等视图，所以需要自己定义
    注册视图。
    登陆默认模板为: registration/login.html
    修改密码模板为: registration/password_change_form.html
    密码修改成功为: registration/password_change_done.html
    重置密码模板为: registration/password_reset_form.html,此时会发送邮件给邮箱
    发送邮箱成功为: registration/password_reset_done.html
    编写新密码的为: registration/password_reset_confirm.html
    编写成功模板为: registration/password_reset_complete.html
    其中如果重置密码发送邮箱需要设置settings中EMAIL_BACKEND  

4. 当用户登陆后，通过中间件request中会带有user属性，其中user.is_authenticated是
    判断用户是否登陆。

5. 最后就是自定义验证用户合法性，首先需要自定义个认证类，通用方法。
    from models import User
    class EmailBackend(object):
        def authenticate(self,request,**kwargs):
            email = kwargs.get('email', kwargs.get('username'))
            try:
                user =  User.objects.get(email = email)
            except User.DoesNoExist:
                pass
            else:
                if user.check_password(kwargs.get('password')):
                    return user

        def get_user(self, user_id):
            #此方法为必须
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNoExist:
                return None

    最后在settings文件中设置AUTHENTICATION = (
        'django.confrib.auth.backends.ModelBackend',
        'user.backends.EmailBackend',
            )
