# Generated by Django 3.2.5 on 2021-07-15 21:45

import uuid

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("sinp_nomenclatures", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organism",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp_create", models.DateTimeField(auto_now_add=True)),
                ("timestamp_update", models.DateTimeField(auto_now=True)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="Identifiant unique",
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        max_length=500, unique=True, verbose_name="Nom"
                    ),
                ),
                (
                    "short_label",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Nom court"
                    ),
                ),
                (
                    "geographic_area_details",
                    models.CharField(
                        blank=True,
                        help_text="Information précisant la zone géographique d'action. Exemple : Basse-Terre",
                        max_length=500,
                        null=True,
                        verbose_name="Détails sur la zone géographique",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Adresse",
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Code postal",
                    ),
                ),
                (
                    "municipality",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Commune",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Adresse mail",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Les numéros de téléphones doivent être renseignés avec le format : '+999999999'. jusqu'à 15 chiffres sont autorisés",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                        verbose_name="Numéro de téléphone",
                    ),
                ),
                (
                    "url",
                    models.URLField(blank=True, null=True, verbose_name="URL"),
                ),
                (
                    "extra_data",
                    models.JSONField(
                        blank=True, null=True, verbose_name="Additional datas"
                    ),
                ),
                (
                    "action_scope",
                    models.ForeignKey(
                        help_text="Périmètre d'action de l'organisme (Européen, national, Supra-régional, Régional, Inconnu)",
                        limit_choices_to={"type": "action_scope"},
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="organism_action_scope",
                        to="sinp_nomenclatures.nomenclature",
                        verbose_name="Périmètre d'action",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "geographic_area",
                    models.ForeignKey(
                        blank=True,
                        help_text="Zone d'action géographique de l'organisme",
                        limit_choices_to={"type": "geographic_area"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="organism_geographic_area",
                        to="sinp_nomenclatures.nomenclature",
                        verbose_name="Zone géographique",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "organismes",
            },
        ),
        migrations.CreateModel(
            name="OrganismMember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp_create", models.DateTimeField(auto_now_add=True)),
                ("timestamp_update", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utilisateur",
                    ),
                ),
                (
                    "member_level",
                    models.ForeignKey(
                        limit_choices_to={"type": "member_level"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_level",
                        to="sinp_nomenclatures.nomenclature",
                        verbose_name="Niveau du membre",
                    ),
                ),
                (
                    "organism",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sinp_organisms.organism",
                        verbose_name="Organisme",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Membre des organismes",
                "unique_together": {("member", "organism", "member_level")},
            },
        ),
        migrations.AddField(
            model_name="organism",
            name="members",
            field=models.ManyToManyField(
                blank=True,
                related_name="organism_member",
                through="sinp_organisms.OrganismMember",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Membres",
            ),
        ),
        migrations.AddField(
            model_name="organism",
            name="status",
            field=models.ForeignKey(
                help_text="Permet d'indiquer si l'organisme est public ou privé",
                limit_choices_to={"type": "organism_status"},
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="organism_status",
                to="sinp_nomenclatures.nomenclature",
                verbose_name="Statut",
            ),
        ),
        migrations.AddField(
            model_name="organism",
            name="type",
            field=models.ForeignKey(
                limit_choices_to={"type": "organism_type"},
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="organism_type",
                to="sinp_nomenclatures.nomenclature",
                verbose_name="Type d'organisme",
            ),
        ),
        migrations.AddField(
            model_name="organism",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
