from rest_framework.viewsets import ModelViewSet

from task_api.filters import filters, TaskFilterSet
from task_api.models import Task
from task_api.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilterSet
