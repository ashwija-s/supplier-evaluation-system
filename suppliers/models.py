from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    delivery_time = models.IntegerField() #in days
    quality_rating = models.FloatField(validators = [MinValueValidator(1.0), MaxValueValidator(5.0)])

def __str__(self):
    return self.name
