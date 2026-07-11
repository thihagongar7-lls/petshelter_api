from django.db import models

# Create your models here.

class Pets(models.Model):
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
