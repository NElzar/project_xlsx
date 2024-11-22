from django.contrib import admin
from .models import DataRecord


class DataRecordAdmin(admin.ModelAdmin):
    list_display = ('ne', 'address', 'latitude', 'longitude', 'gsm', 'umts', 'lte', 'status')
    search_fields = ('ne', 'address')
    list_filter = ('status', 'gsm', 'umts', 'lte')


admin.site.register(DataRecord, DataRecordAdmin)
