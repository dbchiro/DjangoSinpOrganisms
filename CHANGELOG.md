# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

<!-- ## Unreleased [{version_tag}](https://github.com/opengisch/qgis-plugin-ci/releases/tag/{version_tag}) - YYYY-MM-DD -->

## unreleased

## 1.3.1 - 2024-04-24

### Changed

* Recreate inpn organisms fixture

## 1.3.0 - 2024-04-22

### Changed

* Reset migrations (as in dj-sinp-nomenclatures)
* Update dependencies

### Version note

* Please update to module to 1.2.1 version and Execute SQL query on database:

```sql
DELETE FROM django_migrations WHERE app LIKE 'sinp%' AND name NOT LIKE '0001_%';
```

## 1.2.0 - 2024-04-10

* Fix natural keys
* Improve tests

## 1.1.0 - 2024-03-23

* Remove logging actions (created by, updated by and timestamps)

## 1.0.0 - 2024-03-22

* First release
* Specify models
* Basic API routes
* Basic readonly viewsets
* Editing can be done through Django admin
