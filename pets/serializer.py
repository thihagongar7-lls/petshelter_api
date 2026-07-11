from rest_framework import serializers
from .models import Pets

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class PetsRetrieveView(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class PetsCreateView(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class PetsUpdateView(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class PetsDeleteView(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'