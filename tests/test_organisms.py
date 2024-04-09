import uuid

from django.test import TestCase
from sinp_nomenclatures.models import Nomenclature

from sinp_organisms.models import Organism

org_uuid = uuid.uuid4()


class OrganismTestCase(TestCase):
    fixtures = ["sinp_organisms/fixtures/nomenclatures.json"]

    def setUp(self):
        Organism.objects.create(
            uuid=org_uuid,
            administrative_reference="18004417400019",
            label="MUSEUM NATIONAL D'HISTOIRE NATURELLE",
            short_label="MNHN",
            action_scope=Nomenclature.objects.get(
                type__mnemonic="action_scope", code="nat"
            ),
            status=Nomenclature.objects.get(
                type__mnemonic="organism_status", code="pub"
            ),
        )

    def organismExists(self):
        """Animals that can speak are correctly identified"""
        org1 = Organism.objects.get(uuid=org_uuid)
        self.assertEqual(org1.short_label, "MNHN")
        self.assertEqual(org1.natural_key(), (org_uuid,))
