from django.contrib import admin

from task_api.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "completed",
        "created_at",
    )
    list_display_links = (
        "pk",
        "title",
    )
    search_fields = ("title",)
    fields = (
        "title",
        "description",
        "completed",
        "created_at",
    )
    readonly_fields = ("created_at",)
    list_editable = ("completed",)
