from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from sinp_nomenclatures.models import Nomenclature

from .validators import phone_regex


class BaseModel(models.Model):
    """Generic base model with standard metadatas"""

    timestamp_create = models.DateTimeField(auto_now_add=True, editable=False)
    timestamp_update = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True


# Create your models here.
class Organism(BaseModel):
    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_("Identifiant unique"),
    )
    parent = models.ForeignKey(
        "Organism",
        verbose_name=_("Organisme parent"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    label = models.CharField(
        max_length=500, unique=True, verbose_name=_("Nom")
    )
    short_label = models.CharField(
        max_length=50, unique=True, verbose_name=_("Nom court")
    )
    action_scope = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "action_scope"},
        related_name="organism_action_scope",
        verbose_name=_("Périmètre d'action"),
        help_text=_("Périmètre d'action de l'organisme"),
    )
    geographic_area = models.ForeignKey(
        Nomenclature,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "geographic_area"},
        related_name="organism_geographic_area",
        verbose_name=_("Zone géographique"),
        help_text=_("Zone d'action géographique de l'organisme"),
    )
    geographic_area_details = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Détails sur la zone géographique"),
        help_text=_("Information précisant la zone géographique d'action."),
    )
    status = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "organism_status"},
        related_name="organism_status",
        verbose_name=_("Statut"),
        help_text=_("Permet d'indiquer si l'organisme est public ou privé"),
    )
    type = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "organism_type"},
        related_name="organism_type",
        verbose_name=_("Type d'organisme"),
    )
    address = models.CharField(
        max_length=500, blank=True, null=True, verbose_name=_("Adresse")
    )
    postal_code = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_("Code postal")
    )
    municipality = models.CharField(
        max_length=250, blank=True, null=True, verbose_name=_("Commune")
    )
    email = models.EmailField(
        blank=True, null=True, verbose_name=_("Adresse mail")
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        verbose_name=_("Numéro de téléphone"),
    )
    url = models.URLField(
        max_length=200, blank=True, null=True, verbose_name=_("URL")
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="OrganismMember",
        through_fields=("organism", "member"),
        blank=True,
        related_name="organism_member",
        verbose_name=_("Membres"),
    )
    extra_data = models.JSONField(
        blank=True, null=True, verbose_name=_("Additional datas")
    )

    class Meta:
        verbose_name_plural = _("organismes")

    def __str__(self):
        return self.short_label


class OrganismMember(BaseModel):
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Utilisateur"),
    )
    organism = models.ForeignKey(
        "Organism", on_delete=models.CASCADE, verbose_name=_("Organisme")
    )
    member_level = models.ForeignKey(
        Nomenclature,
        on_delete=models.CASCADE,
        limit_choices_to={"type__mnemonic": "member_level"},
        related_name="member_level",
        verbose_name=_("Niveau du membre"),
    )

    class Meta:
        verbose_name_plural = _("Membre des organismes")
        unique_together = ("member", "organism", "member_level")

    def __str__(self):
        return f"{self.member.username} [{self.member_level}]"
