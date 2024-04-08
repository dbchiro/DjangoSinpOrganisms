from rest_framework.serializers import ModelSerializer
from sinp_nomenclatures.serializers import NomenclatureSerializer

from .models import Organism, OrganismMember


class OrganismMemberSerializer(ModelSerializer):
    member_level = NomenclatureSerializer(read_only=True)

    class Meta:
        model = OrganismMember
        fields = [
            "id",
            "member",
            "member_level",
        ]


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


class OrganismDetailledSerializer(OrganismSerializer):
    action_scope = NomenclatureSerializer(read_only=True)
    geographic_area = NomenclatureSerializer(read_only=True, many=True)
    status = NomenclatureSerializer(read_only=True)
    type = NomenclatureSerializer(read_only=True)
    # members = OrganismMemberSerializer(many=True)
