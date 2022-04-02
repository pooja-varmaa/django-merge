from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from blog.models import MyUser

class EmailBackend(ModelBackend):
    def authenticate(self, request,email=None, password=None, **kwargs):
        MyUser= get_user_model()
        print(email,password,'ruuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
        try:
            user = MyUser.objects.get(email=email)
            if user:
                return user
            print(user,'retttttttrtre')
        except MyUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                 return user
                 print(user,'ooooooooooooooooo')
        return None