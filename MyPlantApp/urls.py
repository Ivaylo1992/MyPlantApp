
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyPlantApp.web.urls')),
    path('profile/', include('MyPlantApp.profiles.urls')),
    path('plants/', include('MyPlantApp.plants.urls')),
]