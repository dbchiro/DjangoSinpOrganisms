from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from sinp_nomenclatures.serializers import NomenclatureSerializer

from .models import Organism, OrganismMember

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class OrganismSerializer(ModelSerializer):

    class Meta:
        model = Organism
        fields = [
            "id",
            "uuid",
            "label",
            "short_label",
            "action_scope",
            "geographic_area",
            "geographic_area_details",
            "status",
            "type",
            "address",
            "postal_code",
            "municipality",
            "email",
            "phone_number",
            "url",
        ]
        read_only_fields = [
            "uuid",
        ]


class OrganismMemberSerializer(ModelSerializer):
    member_level = NomenclatureSerializer(read_only=True, many=True)
    organism = OrganismSerializer(read_only=True)
    member = UserSerializer(read_only=True)

    class Meta:
        model = OrganismMember
        fields = [
            "organism",
            "member",
            "member_level",
        ]


class OrganismDetailledSerializer(OrganismSerializer):
    action_scope = NomenclatureSerializer(read_only=True)
    geographic_area = NomenclatureSerializer(read_only=True, many=True)
    status = NomenclatureSerializer(read_only=True)
    type = NomenclatureSerializer(read_only=True)
    members = OrganismMemberSerializer(many=True)
