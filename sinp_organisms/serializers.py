from rest_framework.serializers import ModelSerializer

from .models import Organism, OrganismMember


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
            "created_by",
            "updated_by",
            "timestamp_create",
            "timestamp_update",
        ]
        read_only_fields = [
            "created_by",
            "updated_by",
            "timestamp_create",
            "timestamp_update",
            "uuid",
        ]
        depth = 0


class OrganismMemberSerializer(ModelSerializer):
    class Meta:
        model = OrganismMember
        fields = [
            "id",
            "member",
            "member_level",
        ]
        read_only_fields = [
            "created_by",
            "updated_by",
            "timestamp_create",
            "timestamp_update",
        ]
        depth = 1
