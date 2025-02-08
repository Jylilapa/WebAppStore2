from django.contrib import admin

from blog.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
