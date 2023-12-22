from django.db import models

# Create your models here.

class BreedType(models.Model):
    breed_type = models.CharField(max_length=64, default=None)

    def __str__(self):
        return self.breed_type

class Breed(models.Model):
    breed_name = models.CharField(max_length=64, unique=True)
    breed_type = models.ForeignKey(BreedType, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.breed_name

class Dog(models.Model):
    dog_name = models.CharField(max_length=128, unique=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1)
    weight = models.FloatField()

    def __str__(self):
        return self.dog_name

