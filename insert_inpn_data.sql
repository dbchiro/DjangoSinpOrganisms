BEGIN;

TRUNCATE sinp_organisms_organism RESTART IDENTITY CASCADE;

/* INSERT ORGANISMS */

INSERT INTO sinp_organisms_organism (timestamp_create, timestamp_update, uuid, label, short_label,
                                     geographic_area_details, address, postal_code, municipality, email, phone_number,
                                     url, extra_data, action_scope_id, created_by_id, status_id,
                                     type_id, updated_by_id, parent_id, administrative_reference, enabled)
SELECT now(),
       now(),
       ref_organismes_export_20230809.code::UUID,
       ref_organismes_export_20230809.libelle_long,
       ref_organismes_export_20230809.libelle_court,
       zone_detailles,
       ref_organismes_export_20230809.adresse,
       cp,
       ville,
       mail,
       length(replace(split_part(telephone, 'ou', 1), ' ', '')),
       url,
       '{}'::JSONB,
       action_scope.id,
       1,
       status.id,
       type_organisme.id,
       1,
       NULL,
       siret,
       FALSE
FROM ref_organismes_export_20230809
         JOIN sinp_nomenclatures_nomenclature action_scope
              ON action_scope.type_id = 9 AND
                 lower(unaccent(replace(action_scope.label, ' ', ''))) = lower(unaccent(perimetre))
         LEFT JOIN sinp_nomenclatures_nomenclature AS status
                   ON status.type_id = 2 AND
                      lower(unaccent(replace(statut_organisme, ' ', ''))) = lower(unaccent(status.label))

         JOIN sinp_nomenclatures_nomenclature AS type_organisme
              ON type_organisme.type_id = 13 AND lower(unaccent(replace(type_organisme, ' ', ''))) =
                                                 lower(unaccent(replace(type_organisme.label, ' ', '')))
WHERE (NOT lower(ref_organismes_export_20230809.description) ILIKE '%fermé%')
   OR status.description IS NULL
    AND ref_organismes_export_20230809.id NOT IN (2491, 2946)
ORDER BY ref_organismes_export_20230809.id DESC
ON CONFLICT DO NOTHING
;

/* INSERT ORGANISMS GEOGRAPHIC AREAS */

WITH t1 AS (SELECT code, trim(unnest(string_to_array(zones, '|'))) zone
            FROM ref_organismes_export_20230809)
INSERT
INTO sinp_organisms_organism_geographic_area(organism_id, nomenclature_id)
SELECT sinp_organisms_organism.id, sinp_nomenclatures_nomenclature.id
FROM t1
         JOIN sinp_organisms_organism ON t1.code::UUID = sinp_organisms_organism.uuid
         LEFT JOIN public.sinp_nomenclatures_nomenclature
                   ON sinp_nomenclatures_nomenclature.label = t1.zone
;

/* SET ORGANISM PARENTS */

WITH child AS (SELECT sinp_organisms_organism.id, ref_organismes_export_20230809.id AS source_id, id_parent, uuid
               FROM ref_organismes_export_20230809
                        JOIN sinp_organisms_organism
                             ON ref_organismes_export_20230809.code::UUID = sinp_organisms_organism.uuid
               WHERE id_parent IS NOT NULL),
     parent AS (SELECT child.id,
                       sinp_organisms_organism.id AS parent_id
                FROM ref_organismes_export_20230809
                         JOIN child ON child.id_parent = ref_organismes_export_20230809.id
                         JOIN sinp_organisms_organism
                              ON ref_organismes_export_20230809.code::UUID = sinp_organisms_organism.uuid)
UPDATE sinp_organisms_organism
SET parent_id = parent.parent_id
FROM parent
WHERE parent.id = sinp_organisms_organism.id;

COMMIT;
