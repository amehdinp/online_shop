from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, fullname, password):
        if not email:
            raise ValueError('User must insert email address')
        if not fullname:
            raise ValueError('user must chose full name')
        user = self.model(email=self.normalize_email(email), fullname=fullname,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password):
        user = self.create_user(email, fullname, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user
