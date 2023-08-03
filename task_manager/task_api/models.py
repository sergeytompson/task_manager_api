from django.db import models

from task_api.managers import SortTaskByDateTimeManager


class Task(models.Model):
    title = models.CharField(
        "заголовок",
        max_length=255
    )
    description = models.TextField(
        "описание задачи",
    )
    completed = models.BooleanField(
        "сделано",
        default=False,
    )
    created_at = models.DateTimeField(
        "дата и время создания",
        auto_now_add=True,
    )

    objects = SortTaskByDateTimeManager()
    unsorted_objects = models.Manager()

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"

    def __str__(self) -> str:
        return self.title
