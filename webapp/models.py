

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from import_export import resources as export


class User(AbstractUser):
    profile_pic = models.TextField(blank=True)
    about_me = models.TextField(blank=True)


class UserDataResource(export.ModelResource):

    class Meta:
        model = User
