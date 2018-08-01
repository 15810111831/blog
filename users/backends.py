#coding:utf-8
#增加自定义的验证方式,可以通过邮箱进行验证

from models import User

class EmailBackend(object):
    def authenticate(self, request, **credentials):
        email = credentials.get('email', credentials.get('username'))
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(credentials['password']):
                return user

    def get_user(self, user_id):
        #这个方法是必须的
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNoExist:
            return None

        
