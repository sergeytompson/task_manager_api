from django.urls import include, path

from rest_framework import routers

from task_api.views import TaskViewSet
from task_manager.yasg import urlpatterns as doc_urls

router = routers.SimpleRouter()
router.register(r"task", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += doc_urls
