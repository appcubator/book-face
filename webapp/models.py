

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from import_export import resources as export


class User(AbstractUser):
    pass


class UserDataResource(export.ModelResource):

    class Meta:
        model = User
