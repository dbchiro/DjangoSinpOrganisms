from django.test import TestCase
from sinp_nomenclatures.models import Nomenclature

from .models import Organism


class OrganismTestCase(TestCase):
    fixtures = [
        "initdata.xml",
    ]

    def setUp(self):
        Organism.objects.create(
            label="Organism 1",
            short_label="ORG1",
            action_scope=Nomenclature.objects.filter(
                type__mnemonic="action_scope", code="reg"
            ).first(),
            status=Nomenclature.objects.filter(
                type__mnemonic="organism_status", code="pub"
            ).first(),
            type=Nomenclature.objects.filter(
                type__mnemonic="organism_type", code="pubestab"
            ).first(),
        )

    def test_organisms(self):
        """Animals that can speak are correctly identified"""
        org1 = Organism.objects.get(short_label="ORG1")
        self.assertEqual(str(org1), "ORG1")
