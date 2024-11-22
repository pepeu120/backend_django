from django.urls import include, path
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

router = SimpleRouter()
router.register(r"drone-categories", DroneCategoryViewSet)

urlpatterns = [
    path("drones/", DroneList.as_view(), name=DroneList.name),
    path("drones/<int:pk>/", DroneDetail.as_view(), name=DroneDetail.name),
    path("pilots/", PilotList.as_view(), name=PilotList.name),
    path("pilots/<int:pk>/", PilotDetail.as_view(), name=PilotDetail.name),
    path(
        "competitions/",
        CompetitionList.as_view(),
        name=CompetitionList.name,
    ),
    path(
        "competitions/<int:pk>/",
        CompetitionDetail.as_view(),
        name=CompetitionDetail.name,
    ),
    path("", include(router.urls)),
    path("", ApiRoot.as_view(), name=ApiRoot.name),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]