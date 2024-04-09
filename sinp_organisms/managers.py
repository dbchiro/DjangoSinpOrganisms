from uuid import UUID

from django.db.models import Manager


class OrganismManager(Manager):
    """Organisms custom manager"""

    def get_by_natural_key(self, uuid: UUID):
        """Get by natural key function for organisms

        Args:
            uuid (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.get(uuid=uuid)


class OrganismMemberManager(Manager):

    def get_by_natural_key(
        self,
        member_username: str,
        organism_uuid: UUID,
        member_level_code: str,
        member_level_type_code: str,
    ):
        return self.get(
            member__username=member_username,
            organism__uuid=organism_uuid,
            member_level__code=member_level_code,
            member_level__type__mnemonic=member_level_type_code,
        )
