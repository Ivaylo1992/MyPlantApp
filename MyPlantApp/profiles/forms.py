from django import forms

from MyPlantApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(ProfileBaseForm):

    class Meta(ProfileBaseForm.Meta):
        exclude = ["profile_picture", ]


class ProfileEditForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["readonly"] = "readonly"

