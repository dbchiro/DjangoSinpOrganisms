#!/usr/bin/python

"""SINP Organisms validators
"""

from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message=(
        "Les numéros de téléphones doivent être renseignés avec le format :"
        "'+999999999'. jusqu'à 15 chiffres sont autorisés"
    ),
)
