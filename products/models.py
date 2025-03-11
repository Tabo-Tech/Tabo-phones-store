from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)  # Jina la bidhaa
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Bei ya bidhaa
    description = models.TextField(blank=True, null=True)  # Maelezo ya bidhaa
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Picha ya bidhaa
    created_at = models.DateTimeField(auto_now_add=True)  # Muda wa kuongezwa kwa bidhaa

    def __str__(self):
        return self.name  # Hii itakuwa jina la bidhaa kwenye admin panel
