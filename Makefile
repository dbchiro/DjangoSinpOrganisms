MANAGE = poetry run python -m manage


install :
	poetry install

build :
	poetry build

dumpdata :
	$(MANAGE) dump_object --natural-foreign --natural-primary  --query '{"type__mnemonic__in": ["action_scope", "geographic_area", "organism_status","organism_type","member_level"]}' sinp_nomenclatures.nomenclature > sinp_organisms/fixtures/nomenclatures.json
	$(MANAGE) dumpdata --natural-foreign --natural-primary --indent=2 sinp_organisms.organism > sinp_organisms/fixtures/inpn_organims.json

runserver:
	$(MANAGE) runserver
