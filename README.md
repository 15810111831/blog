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
