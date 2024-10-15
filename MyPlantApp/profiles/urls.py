
from django.urls import path, include
from MyPlantApp.profiles import views

urlpatterns = [
    path("create/", views.CreateProfileView.as_view(), name="create_profile"),
    path("details/", views.ProfileDetailsView.as_view(), name="details_profile"),
    path("edit/", views.ProfileEditView.as_view(), name="edit_profile"),
    path("delete/", views.ProfileDeleteView.as_view(), name="delete_profile"),

]
