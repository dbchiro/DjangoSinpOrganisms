import logging

# from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from .mixins import OrganismsFilteringMixin
from .models import Organism, OrganismMember
from .serializers import OrganismMemberSerializer, OrganismSerializer

logger = logging.getLogger(__name__)


class OrganismViewset(OrganismsFilteringMixin, ModelViewSet):
    serializer_class = OrganismSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Organism.objects.all()


class OrganismMemberViewset(ModelViewSet):
    serializer_class = OrganismMemberSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = OrganismMember.objects.all()
