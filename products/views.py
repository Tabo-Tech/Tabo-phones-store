from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt  # Inaruhusu requests hata kama hazina CSRF token
def product_list(request):
    if request.method == "GET":
        products = list(Product.objects.values())  # Rudisha data kama JSON
        return JsonResponse({'products': products}, safe=False)

    elif request.method == "POST":
        return JsonResponse({"message": "Product created"}, status=201)

    return JsonResponse({"error": "Method Not Allowed"}, status=405)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Tabostore!")  # Au unaweza kuredirect kwenye 'products/'
