from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser


class MyUser(EmailAbstractUser):

	objects = EmailUserManager()
