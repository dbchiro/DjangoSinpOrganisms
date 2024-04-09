import uuid

from django.test import TestCase
from sinp_nomenclatures.models import Nomenclature

from .models import Organism

org1_uuid = uuid.uuid4()


class OrganismTestCase(TestCase):
    fixtures = [
        "nomenclatures.json",
    ]

    def setUp(self):
        Organism.objects.create(
            label="Organism 1",
            short_label="ORG1",
            uuid=org1_uuid,
            action_scope=Nomenclature.objects.get(
                type__mnemonic="action_scope", code="reg"
            ),
            status=Nomenclature.objects.get(
                type__mnemonic="organism_status", code="pub"
            ),
            type=Nomenclature.objects.get(
                type__mnemonic="organism_type", code="pubestab"
            ),
        )

    def test_organisms(self):
        """Animals that can speak are correctly identified"""
        org1 = Organism.objects.get(short_label="ORG1")
        self.assertEqual(str(org1), "ORG1")
        self.assertEqual(org1.uuid, org1_uuid)
        self.assertEqual(org1.natural_key(), (org1_uuid,))
