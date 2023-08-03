from django.db.models import Manager, QuerySet


class SortTaskByDateTimeManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().order_by("-created_at")
