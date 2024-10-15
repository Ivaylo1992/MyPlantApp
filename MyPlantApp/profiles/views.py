
from django.urls import reverse_lazy
from django.views import generic as views

from MyPlantApp.core.helpers import get_profile
from MyPlantApp.core.views_mixins import HasProfileMixin
from MyPlantApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from MyPlantApp.profiles.models import Profile


class CreateProfileView(views.CreateView):
    model = Profile
    template_name = "profiles/create-profile.html"
    form_class = ProfileCreateForm
    success_url = reverse_lazy("details_profile")


class ProfileDetailsView(HasProfileMixin, views.DetailView):
    model = Profile
    template_name = "profiles/profile-details.html"
    context_object_name = "profile"
    count_of_stars = get_profile().plants.count()
    # we don't need more than 3 stars
    count_of_stars = count_of_stars if count_of_stars <= 3 else 3

    def get_object(self, queryset=None):
        return get_profile()

    extra_context = {
        # creating a range for the loop in the template
        "stars_range": range(count_of_stars),
        "count_of_stars": count_of_stars
    }


class ProfileEditView(HasProfileMixin, views.UpdateView):
    model = Profile
    template_name = "profiles/edit-profile.html"
    form_class = ProfileEditForm
    success_url = reverse_lazy("details_profile")

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(HasProfileMixin, views.DeleteView):
    model = Profile
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
