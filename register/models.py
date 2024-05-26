from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def Post(models.Model):
    
    title = models.CharField(max_length = 600)
    price = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, unique = True)
    author = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name='post_author'
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        ordering = ("-created_at",)
        
    def __str__(self):
        return self.name
    
class Products(models.Model):
    card_id = models.CharField(max_length = 600)
    card_price = models.DecimalField(max_digits=5, decimal_places=2)
    card_description = models.CharField(max_length = 600)
    card_type = models.CharField(max_length = 600)
    #card_image = models.ImageFeild()