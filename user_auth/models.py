from distutils.command.upload import upload
from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser
# from django.contrib.auth import get_user_model


# User = get_user_model()


class MyUser(EmailAbstractUser):

    phone = models.CharField('phone', max_length=15, blank=True)

    objects = EmailUserManager()
