from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Pet
from .serializer import PetsSerializer

from .models import AdoptionModel
from .serializer import AdoptionSerializer

class PetsViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]


    filterset_fields = ['species','gender','adoption_status']

    search_fields = ['name','species','breed','description',]
    ordering_fields = ['name','age','created_at',]

    ordering = ['-created_at']

class AdoptionViewSet(ModelViewSet):
    queryset = AdoptionModel.objects.all()
    serializer_class = AdoptionSerializer

    filter_backends =[ DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ["adoption_status", "pet"]

    search_fields = [
        "adopter_name",
        "adopter_email",
        "phone",
    ]

    order_fields = [
        "created_at"
    ]

    ordering = ["-created_at"]

    def perform_create(self, serializer):
        pet = serializer.validated_data['pet']

        if pet.adoption_status == 'P':
            raise ValidationError("This pet already has a pending adoption request.")
        if pet.adoption_status == 'D' :
            raise ValidationError("This pet has already been adopted.")

        # Short style
        # if pet.adoption_status in ['P', 'D'] :
        #     raise ValidationError("This pet is not available for adoption.")
        
        serializer.save()

    def perform_update(self, serializer):
        adoption = serializer.save()

        if adoption.adoption_status == 'A' :
            pet = adoption.pet
            pet.adoption_status = 'D'
            pet.save()