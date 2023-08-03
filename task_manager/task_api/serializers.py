from rest_framework import serializers

from task_api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d/%m/%y %H:%M:%S",
        read_only=True,
    )

    class Meta:
        model = Task
        fields = (
            "pk",
            "title",
            "description",
            "completed",
            "created_at",
        )
