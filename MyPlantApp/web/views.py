from django.shortcuts import render
from django.views import generic as views

from MyPlantApp.core.views_mixins import HasProfileMixin
from MyPlantApp.plants.models import Plant


class IndexView(HasProfileMixin, views.TemplateView):
    template_name = "web/home-page.html"


class CatalogueView(HasProfileMixin, views.ListView):
    queryset = Plant.objects.all()
    template_name = "web/catalogue.html"

