# Honeytoken-as-a-Service

Lightweight service to generate and seed realistic honeytokens (API keys, fake user accounts, DB rows) and emit high-fidelity alerts when a token is used.

Features
- Generate ephemeral or persistent honeytokens
- Simple webhook alerting and logging
- Dockerized FastAPI app

Quick start
1. Build: docker build -t honeytoken-service .
2. Run: docker run -p 8000:8000 honeytoken-service
3. POST /generate to get a token; any request using the token should hit /webhook on this service (or forward alerts).

Files
- src/honeytoken_service: app code
- examples/: seeding scripts
- .github/workflows: CI

License: MIT
