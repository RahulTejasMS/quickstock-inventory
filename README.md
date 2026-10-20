# QuickStock

A backend-first inventory management system designed around the operational challenges of quick-commerce dark stores.

## Problem

Quick-commerce operations need accurate inventory across multiple stores, reliable stock reservations, and visibility into stock movements. Incorrect stock counts and concurrent order requests can cause overselling, failed orders, and poor customer experiences.

QuickStock aims to model these problems and implement reliable solutions incrementally.

## Planned Features

- Product and SKU management
- Inventory tracking by store
- Auditable stock movements
- Stock reservation and release
- Concurrency control to prevent overselling
- Low-stock alerts and replenishment workflows
- Batch and expiry tracking
- Automated testing and continuous integration

## Planned Technology Stack

- Python and FastAPI
- PostgreSQL
- SQLAlchemy and database migrations
- Pytest
- Docker and Docker Compose
- Redis and background jobs when justified by requirements
- GitHub Actions

## Engineering Principles

- Understandable, maintainable code
- Explicit data integrity rules
- Automated tests
- Small, reviewable Git commits
- Documented design decisions and trade-offs

## Project Status

Stage 1: Repository setup and requirements.
