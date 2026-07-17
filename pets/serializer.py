from rest_framework import serializers
from .models import Pet
from .models import AdoptionModel

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionModel
        fields = "__all__"

        def validate_phone(self,value):
            clean_value = value.strip().replace("+95","").lstrip("0")

            if not clean_value.isdigit():
                raise serializers.ValidationError("Phone number must contain only digits.")
            
            if len(clean_value) != 9 :
                raise serializers.ValidationError("Phone number must contain exactly 9 digits after removing the zero.")
            
            return "+95" + clean_value
        
        def validate_message(self,value):
            value = value.strip()

            if len(value) < 15 :
                raise serializers.ValidationError("Message must be at least 15 characters.")
            
            if len(value) > 200 :
                raise serializers.ValidationError("Message cannot exceed 200 characters.")
            
            return value
        
        def validate(self,attrs):
            pet = attrs["pet"]
            email = attrs["adopter_email"]

            if pet.adoption_status == "D" :
                raise serializers.ValidationError("This pet has already been adopted.")
            
            if AdoptionModel.objects.filter(
                pet = pet,
                adopter_email = email,
                adoption_status = "P",
            ).exists():
                raise serializers.ValidationError("You already have a pending adoption request for this pet.")
            
            return attrs
        
class PetsSerializer(serializers.ModelSerializer):
    adoption_requests = AdoptionSerializer(
        many = True,
        read_only = True
    ) 
    class Meta:
        model = Pet
        fields = '__all__'

class PetsRetrieveView(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class PetsCreateView(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class PetsUpdateView(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class PetsDeleteView(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

# AdoptionModel
# class AdoptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdoptionModel
#         fields = '__all__'  

#     def validate_phone(self, value):
#         if not value:
#             raise serializers.ValidationError("Phone number is missing!")
        
#         clean_value = str(value).lstrip('0').replace('+', '')

#         if not clean_value :
#             raise serializers.ValidationError("Phone number is invalid!")
        
#         if not clean_value.isdigit():
#             raise serializers.ValidationError("Phone number must contain only numbers.")

#         if len(clean_value) !=10:
#             raise serializers.ValidationError("Phone number must be exactly 10 digits.") 
        
#         return f"+95{clean_value}"
    
#     def validate_message(self,value):
#         value = value.strip()

#         if len(value) < 15 :
#             raise serializers.ValidationError("Message must be at least 15 characters.")
        
#         if len(value) > 200 :
#             raise serializers.ValidationError("Message cannot exceed 200 characters.")
        
#         return value

    
#     def validate_adopter_email(self,value):
#         if not value.endswith('@gmail.com') and not value.endswith('@yahoo.com'):
#             raise serializers.ValidationError("Only Gmail or Yahoo email addresses are allowed.")
#         return value
    
#     def validate(self,data):
#         pet = data.get('pet')

#         if pet.adoption_requests.filter(adoption_status='A').exists():
#             raise serializers.ValidationError("This pet has already been adopted.")
#         return data

