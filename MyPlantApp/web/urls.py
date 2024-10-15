
from django.urls import path
from MyPlantApp.web import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("catalogue/", views.CatalogueView.as_view(), name="catalogue"),
]
