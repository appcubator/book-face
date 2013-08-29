

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin as exportadmin
from webapp.models import User, UserDataResource, Wall_post, Wall_postDataResource


class Wall_postModelAdmin(exportadmin):
    pass


admin.site.register(Wall_post, Wall_postModelAdmin)


admin.site.register(User, UserAdmin)
