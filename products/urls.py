from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views  # Hakikisha views zako zipo

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('products/', views.product_list, name='product_list'),  # Route ya kuonyesha bidhaa
]

# Ruhusu Django kuhudumia picha kwenye mode ya development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
