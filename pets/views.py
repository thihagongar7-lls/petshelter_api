from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Pets
from .serializer import PetsSerializer

class PetsViewSet(ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer

    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]


    filterset_fields = ['species','gender','adoption_status']

    search_fields = ['name','species','breed','description',]
    ordering_fields = ['name','age','created_at',]

    ordering = ['-created_at']