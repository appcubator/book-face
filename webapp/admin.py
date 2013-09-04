

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin as exportadmin
from webapp.models import Friendship, FriendshipDataResource, User, UserDataResource, Wall_post, Wall_postDataResource


class Wall_postModelAdmin(exportadmin):
    pass


admin.site.register(Wall_post, Wall_postModelAdmin)


class FriendshipModelAdmin(exportadmin):
    pass


admin.site.register(Friendship, FriendshipModelAdmin)


admin.site.register(User, UserAdmin)
