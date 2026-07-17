from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PetsViewSet
from .views import AdoptionViewSet
# Create your views here.

router = DefaultRouter()

router.register("", PetsViewSet, basename="pets")
router.register("adoptions", AdoptionViewSet)

urlpatterns = router.urls