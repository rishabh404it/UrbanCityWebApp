from django.contrib import admin
from .models import Users
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Users)
class UsersAdmin(ImportExportModelAdmin):
    list_fields = ('name','desc','img')
    