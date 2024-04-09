import uuid

from django.contrib.auth import get_user_model
from django.test import TestCase
from sinp_nomenclatures.models import Nomenclature

from .models import Organism, OrganismMember

User = get_user_model()

org1_uuid = uuid.uuid4()


class OrganismTestCase(TestCase):
    fixtures = [
        "nomenclatures.json",
    ]

    def setUp(self):
        self.user1 = User.objects.create(
            username="user1", email="user1@test.com", password="user1Pwd!"
        )
        self.user2 = User.objects.create(
            username="user2", email="user2@test.com", password="user2Pwd!"
        )
        self.org1 = Organism.objects.create(
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
        self.org_member1 = OrganismMember.objects.create(
            member=self.user1,
            organism=self.org1,
            member_level=Nomenclature.objects.get(
                type__mnemonic="member_level", code="manager"
            ),
        )

    def test_organisms(self):
        """Animals that can speak are correctly identified"""
        org1_1 = Organism.objects.get(short_label="ORG1")
        org1_2 = Organism.objects.get_by_natural_key(*(org1_uuid,))
        user1 = User.objects.get(username="user1")
        member1 = OrganismMember.objects.get_by_natural_key(
            *(
                "user1",
                org1_uuid,
                "manager",
                "member_level",
            )
        )
        user2 = User.objects.get_by_natural_key(
            username="user2",
        )
        self.assertEqual(str(org1_1), "ORG1")
        self.assertEqual(org1_1.uuid, org1_uuid)
        self.assertEqual(org1_1.natural_key(), (org1_uuid,))
        self.assertIn(user1, org1_1.members.all())
        self.assertNotIn(user2, org1_1.members.all())
        self.assertEqual(org1_1, org1_2)
        self.assertEqual(user1, member1.member)
        self.assertIn(member1, org1_1.organismmember_set.all())
        self.assertEqual(str(member1), f"{user1} [Gestionnaire]")
        self.assertEqual(
            member1.natural_key(),
            (user1.username, org1_1.uuid, "manager", "member_level"),
        )
