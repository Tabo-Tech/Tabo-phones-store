from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product  # Import model ya bidhaa

admin.site.register(Product)  # Sasa bidhaa zitaonekana kwenye admin panel

