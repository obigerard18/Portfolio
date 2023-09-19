from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Junies_Cars.urls')),
    path('', include('contact.urls')),
    path('admin/', admin.site.urls),
]
