import logging

# from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from .mixins import OrganismsFilteringMixin
from .models import Organism, OrganismMember
from .serializers import (
    OrganismDetailledSerializer,
    OrganismMemberSerializer,
    OrganismSerializer,
)

logger = logging.getLogger(__name__)


class OrganismViewset(OrganismsFilteringMixin, ModelViewSet):
    # serializer_class = OrganismDetailledSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = (
        Organism.objects.select_related("action_scope")
        .select_related("parent")
        .select_related("status")
        .select_related("type")
        .select_related("parent")
        .prefetch_related("geographic_area")
        .prefetch_related("members")
        .all()
    )

    def get_serializer_class(self):
        depth = self.request.query_params.get("depth", 0)
        if depth == "1":
            return OrganismDetailledSerializer
        return OrganismSerializer


class OrganismMemberViewset(ModelViewSet):
    serializer_class = OrganismMemberSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = (
        OrganismMember.objects.select_related("member")
        .select_related("member_level")
        .all()
    )
