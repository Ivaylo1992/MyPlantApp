from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.profiles.validators import name_validator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(USERNAME_MIN_LENGTH),
        ],
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            name_validator,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            name_validator,
        ],
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def get_name(self):
        return f"{self.first_name} {self.last_name}"
