from MyPlantApp.core.helpers import get_profile


class HasProfileMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_profile'] = get_profile()
        return context