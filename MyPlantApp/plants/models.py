from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.plants.validators import validate_plant_name
from MyPlantApp.profiles.models import Profile


class Plant(models.Model):
    class PlantTypeChoices(models.TextChoices):
        OUTDOOR_PLANTS = "Outdoor Plants"
        INDOOR_PLANTS = "Indoor Plants"

    PLANT_TYPE_MAX_LENGTH = max(len(x) for _, x in PlantTypeChoices.choices)
    NAME_MAX_LENGTH = 20
    NAME_MIN_LENGTH = 2

    plant_type = models.CharField(
        max_length=PLANT_TYPE_MAX_LENGTH,
        choices=PlantTypeChoices.choices,
        blank=False,
        null=False,
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
        validators=[
            validate_plant_name,
            MinLengthValidator(NAME_MIN_LENGTH),
        ],
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )

    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="plants",
        blank=False,
        null=False,
    )