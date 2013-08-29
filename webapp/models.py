

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from import_export import resources as export


class Wall_post(models.Model):
    text = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='posts_written', null=True, blank=True)
    wall_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='posts_on_wall', null=True, blank=True)


class User(AbstractUser):
    profile_pic = models.TextField(blank=True)
    about_me = models.TextField(blank=True)


class Wall_postDataResource(export.ModelResource):

    class Meta:
        model = Wall_post


class UserDataResource(export.ModelResource):

    class Meta:
        model = User
