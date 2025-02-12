# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.3.4] - 2025-02-12
Update dependencies to support HTTP/2 in httpx

## [2.3.1] - 2024-08-01
Fix hash in poetry lock

## [2.3.1] - 2024-08-01
Fix bug in response content handling

## [2.3.0] - 2024-08-01
Fallback deserialization logic to deal with magicbell issue + new list push subscription endpoint

## [2.2.2] - 2024-07-18
Make logging of magic bell errors a warning. Log error response content

## [2.2.1] - 2024-07-08
Add logging around communication point with MagicBell

## [2.2.0] - 2024-03-12
Update to support push subscription endpoint

## [2.1.4] - 2024-03-01
Update the api endpoint

## [2.1.3] - 2024-02-21
Move off of orjson in favor of pydantic

## [2.1.1] - 2024-02-19
Fix pydantic 2 req version

## [2.1.0] - 2023-09-24
Support Pydantic v2 + new magicbell endpoints

## [1.2.1] - 2023-01-19
### Changed
- Fix endpoint

## [1.2.0] - 2023-01-19
### Changed
- Updated to belfry_magicbell package
- Moved to broadcast endpoint


## [2.0.0] - 2023-09-24
Support Pydantic v2

## [1.1.1] - 2022-08-01
### Changed
- Update contributing for clarity for project
- Update flake8 checks

### Added
- Code coverage collection with codecov.io

## [1.1.0] - 2022-07-07
### Added
- Add `MagicBell.connect` and `MagicBell.disconnect` methods for more ergonomic connection management.

### Fixed
- Reorder `Notification` types to avoid forward ref issue in pydantic validation

## [1.0.0] - 2022-07-05
First open source release of the SDK.

### Added
- Initial repo setup with basic client and CI
- APIs supported:
  - Create notification
  - Create user
  - Update user
  - Delete user
  - List projects
  - Get project
  - Create project
  - Update project
  - Delete project
  - Updating channel configuration for a project (undocumented)
  - Retrieve channel configuration for a project (undocumented)
  - GraphQL queries