from django.contrib import admin
from .models import Feedback
from import_export.admin import ImportExportModelAdmin

@admin.register(Feedback)
class FeedbackAdmin(ImportExportModelAdmin):
    list_fields = ('Name','CityName','Desc')

