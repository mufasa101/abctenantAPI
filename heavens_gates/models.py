from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


# Create your models here.
class SaintPeter(BaseUserManager):

    def createUser(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Kindly enter an email address to begin')
        user = self.model(
            username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Kinly enter a password')
        if email is None:
            raise TypeError('Kindly enter an email address to begin')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
