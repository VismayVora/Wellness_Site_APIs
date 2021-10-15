from django.db import models

# Create your models here.
class DietLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)

    Solid = 'S'
    Liquid = 'L'
    FOOD_TYPE_CHOICES = [(Solid,'Solid'),(Liquid,'Liquid')]
    food_type = models.CharField(max_length=2, choices = FOOD_TYPE_CHOICES, default = Solid )

    quantity = models.IntegerField()
    consumption_time = models.DateTimeField()
    calories = models.DecimalField(max_digits=6, decimal_places=3)
    notes = models.TextField(max_length = 300)

    class Meta:
        ordering = ['created']

    
