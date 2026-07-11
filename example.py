# from django.contrib import admin
# from .models import Pets

# # Register your models here.

# admin.site.register(Pets)

# from django.db import models

# # Create your models here.

# class Pets(models.Model):
#     GENDER_CHOICES =[
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('U', 'Unknown'),
#     ]

#     name = models.CharField(max_length=100)
#     species = models.CharField(max_length=100)
#     breed = models.CharField(max_length=50,blank=True,null=True)
#     age = models.PositiveIntegerField()
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     description = models.TextField()
#     adoption_status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} ({self.species})"

# from rest_framework import serializers
# from .models import Pets

# class PetsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pets
#         fields = '__all__'

# class PetsRetrieveView(serializers.ModelSerializer):
#     class Meta:
#         model = Pets
#         fields = '__all__'

# class PetsCreateView(serializers.ModelSerializer):
#     class Meta:
#         model = Pets
#         fields = '__all__'

# class PetsUpdateView(serializers.ModelSerializer):
#     class Meta:
#         model = Pets
#         fields = '__all__'

# class PetsDeleteView(serializers.ModelSerializer):
#     class Meta:
#         model = Pets
#         fields = '__all__'

# from django.urls import path
# from .views import PetsListView,PetsRetrieveView,PetsCreateView,PetsUpdateView,PetsDeleteView
# # Create your views here.

# urlpatterns = [
#    path("", PetsListView.as_view(), name='pets-list'),
#    path("<int:pk>/retrieve/",PetsRetrieveView.as_view(),name='pets-retrieve'),
#    path("create/",PetsCreateView.as_view(),name='pets-create'),
#    path("<int:pk>/update/",PetsUpdateView.as_view(),name='pets-update'),
#    path("<int:pk>/delete/",PetsDeleteView.as_view(),name='pets-delete'),
# ]

# from rest_framework.generics import (ListAPIView, RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView)
# from .models import Pets
# from .serializer import PetsSerializer

# class PetsListView(ListAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializer

# class PetsRetrieveView(RetrieveAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializer

# class PetsCreateView(CreateAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializer

# class PetsUpdateView(UpdateAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializer

# class PetsDeleteView(DestroyAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializer

# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('pets/', include('pets.urls'))
# ]