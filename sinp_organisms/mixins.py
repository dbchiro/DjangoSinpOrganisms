import logging
from ast import literal_eval

from django.db.models import Q

logger = logging.getLogger(__name__)


def set_if_not_none(mapping, key, value):
    if value is not None:
        mapping[key] = value


class OrganismsFilteringMixin:
    """Mixin used for Place lists filtering"""

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()

        label = self.request.query_params.get("label", None)
        uuid = self.request.query_params.get("uuid", None)
        action_scope = self.request.query_params.get("action_scope", None)
        geographic_area = self.request.query_params.get(
            "geographic_area", None
        )
        status = self.request.query_params.get("status", None)
        organism_type = self.request.query_params.get("type", None)
        enabled = self.request.query_params.get("enabled", None)
        member = self.request.query_params.get("member", None)

        if enabled is not None:
            enabled = enabled.lower().capitalize()
            if enabled in ("True", "False"):
                qs = qs.filter(enabled=literal_eval(enabled))

        qs = (
            qs.filter(
                Q(label__icontains=label) | Q(short_label__icontains=label)
            )
            if label is not None
            else qs
        )

        qs = qs.filter(uuid=uuid) if uuid is not None else qs

        qs = (
            qs.filter(
                Q(action_scope__mnemonic=action_scope)
                | Q(action_scope__code=action_scope)
            )
            if action_scope is not None
            else qs
        )

        qs = (
            qs.filter(
                Q(geographic_area__mnemonic=geographic_area)
                | Q(geographic_area__code=geographic_area)
            )
            if geographic_area is not None
            else qs
        )

        qs = (
            qs.filter(Q(status__mnemonic=status) | Q(status__code=status))
            if status is not None
            else qs
        )

        qs = (
            qs.filter(Q(type__mnemonic=type) | Q(type__code=type))
            if organism_type is not None
            else qs
        )

        qs = qs.filter(members=member) if member else qs
        return qs
