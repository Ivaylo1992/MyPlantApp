from django.core.exceptions import ValidationError


def validate_plant_name(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")
