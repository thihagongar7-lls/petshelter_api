from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PetsViewSet
from .views import AdoptionViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create your views here.

router = DefaultRouter()

router.register("", PetsViewSet, basename="pets")
router.register("adoptions", AdoptionViewSet, basename="adoptions")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls