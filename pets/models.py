from django.db import models
# Create your models here.
# from django.contrib.auth import get_user_model

# User = get_user_model()
class Pet(models.Model):
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown'),
    ]

    ADOPTION_STATUS = [
        ('A', 'Available'),
        ('P', 'Pending'),
        ('D', 'Adopted'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=50,blank=True,null=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    description = models.TextField()
    adoption_status = models.CharField(max_length=1, choices=ADOPTION_STATUS, default='A')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.species})"

class AdoptionModel(models.Model):
    ADOPTION_STATUS =[
        ('P','Pending'),
        ('A','Approved'),
        ('R','Rejected'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    adopter_name = models.CharField(max_length=20, blank=False, null=False)
    adopter_email = models.EmailField(max_length=30,blank=False, null=False)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    adoption_status = models.CharField(max_length=1, choices=ADOPTION_STATUS, default='P')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.adopter_name} - {(self.pet.name)}"