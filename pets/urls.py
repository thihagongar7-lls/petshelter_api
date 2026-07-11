from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PetsViewSet
# Create your views here.

router = DefaultRouter()

router.register("", PetsViewSet, basename="pets")

urlpatterns = router.urls