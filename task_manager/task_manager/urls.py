from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("sergey/admin/", admin.site.urls),
    path("sergey/api/", include("task_api.urls")),
]
