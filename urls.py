from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),          # Product listing, detail, cart
    path('users/', include('users.urls')),    # Register, login, logout, profile
    path('orders/', include('orders.urls')),  # Checkout, order history
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)