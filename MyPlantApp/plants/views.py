from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from MyPlantApp.core.helpers import get_profile
from MyPlantApp.core.views_mixins import HasProfileMixin
from MyPlantApp.plants.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from MyPlantApp.plants.models import Plant


class PlantCreateView(HasProfileMixin, views.CreateView):
    model = Plant
    template_name = "plants/create-plant.html"
    form_class = PlantCreateForm
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        form.instance.profile = get_profile()
        return super().form_valid(form)


class PlantDetailsView(HasProfileMixin, views.DetailView):
    model = Plant
    template_name = "plants/plant-details.html"
    context_object_name = "plant"

    pk_url_kwarg = "plant_id"


class PlantEditView(HasProfileMixin, views.UpdateView):
    model = Plant
    template_name = "plants/edit-plant.html"
    form_class = PlantEditForm
    success_url = reverse_lazy("catalogue")
    pk_url_kwarg = "plant_id"


class PlantDeleteView(HasProfileMixin, views.DeleteView):
    model = Plant
    template_name = "plants/delete-plant.html"
    form_class = PlantDeleteForm
    success_url = reverse_lazy("catalogue")
    pk_url_kwarg = "plant_id"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs