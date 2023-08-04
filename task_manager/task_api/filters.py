from django_filters import rest_framework as filters

from task_api.models import Task


class TaskFilterSet(filters.FilterSet):
    class Meta:
        model = Task
        fields = ("completed",)
