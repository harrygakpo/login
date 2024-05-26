from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
  # Get all products
  products = Product.objects.all()

  # Context dictionary to pass data to template
  context = {'products': products}

  # Render the template with data
  return render(request, 'store.html', context)

def store(request):
    return render(request, "authentication/store.html")

def checkout(request):
    return render(request, "authentication/checkout.html")

def add_to_cart(item):
    pass

