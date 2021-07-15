import logging

# from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Organism, OrganismMember
from .serializers import (
    OrganismSerializer, OrganismMemberSerializer
)


logger = logging.getLogger(__name__)

class OrganismViewset(ReadOnlyModelViewSet):
    serializer_class = OrganismSerializer
    permission_classes = [IsAuthenticated]
    queryset = Organism.objects.all()

class OrganismMemberViewset(ReadOnlyModelViewSet):
    serializer_class= OrganismMemberSerializer
    permission_classes = [IsAuthenticated]
    queryset = OrganismMember.objects.all()