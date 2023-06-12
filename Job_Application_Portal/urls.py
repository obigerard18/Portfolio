from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Job_Portal.urls')),
    path('admin/', admin.site.urls),
]
