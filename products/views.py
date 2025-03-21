from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Product

@require_http_methods(["GET", "POST"])  # Inaruhusu GET na POST
def product_list(request):
    if request.method == "POST":
        # Fanya kitu na POST data hapa (kama ku-filter bidhaa)
        pass
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
