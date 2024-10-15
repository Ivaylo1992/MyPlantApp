
from django.urls import path
from MyPlantApp.plants import views

urlpatterns = [
    path("create/", views.PlantCreateView.as_view(), name="create_plant"),
    path("details/<int:plant_id>/", views.PlantDetailsView.as_view(), name="details_plant"),
    path("edit/<int:plant_id>/", views.PlantEditView.as_view(), name="edit_plant"),
    path("delete/<int:plant_id>/", views.PlantDeleteView.as_view(), name="delete_plant"),
]
