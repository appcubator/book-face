

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin as exportadmin
from webapp.models import User, UserDataResource

admin.site.register(User, UserAdmin)
