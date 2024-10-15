from django import forms

from MyPlantApp.plants.models import Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"
        exclude = ("profile",)
        labels = {
            "image_url": "Image URL",
        }


class PlantCreateForm(PlantBaseForm):
    ...


class PlantEditForm(PlantBaseForm):
    ...


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super(PlantDeleteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["readonly"] = "readonly"

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
