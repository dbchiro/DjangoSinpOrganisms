import logging

# from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .mixins import OrganismsFilteringMixin
from .models import Organism, OrganismMember
from .serializers import OrganismMemberSerializer, OrganismSerializer

logger = logging.getLogger(__name__)


class OrganismViewset(OrganismsFilteringMixin, ReadOnlyModelViewSet):
    serializer_class = OrganismSerializer
    permission_classes = [IsAuthenticated]
    queryset = Organism.objects.all()


class OrganismMemberViewset(ReadOnlyModelViewSet):
    serializer_class = OrganismMemberSerializer
    permission_classes = [IsAuthenticated]
    queryset = OrganismMember.objects.all()
