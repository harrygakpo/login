from django.db import models

# Create your models here.
class Product(models.Model):
    card_id = models.CharField(max_length = 600)
    card_price = models.DecimalField(max_digits=5, decimal_places=2)
    card_description = models.CharField(max_length = 600)
    card_type = models.CharField(max_length = 600)
    #card_image = models.ImageField()
    
class Card_number(models.Model):
    number = models.IntegerField()