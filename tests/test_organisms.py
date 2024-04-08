import uuid

from django.test import TestCase
from sinp_nomenclatures.models import Nomenclature

from sinp_organisms.models import Organism

org_uuid = uuid.uuid4()


class OrganismTestCase(TestCase):
    def setUp(self):
        Organism.objects.create(
            uuid=org_uuid,
            administrative_reference="18004417400019",
            label="MUSEUM NATIONAL D'HISTOIRE NATURELLE",
            short_label="MNHN",
            action_scope=Nomenclature.objects.get(
                type__mnemonic="action_scope"
            )[0],
        )

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        org1 = Organism.objects.get(uuid=org_uuid)
        self.assertEqual(org1.short_label, "MNHN")
