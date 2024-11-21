from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("toys.urls")),
    path("api/", include("drones.urls")),
    path("auth/", include("rest_framework.urls")),
]
