Developer notes

- Run locally: pip install -r requirements.txt
- Start: uvicorn honeytoken_service.main:app --reload
- Run tests: pytest

Seeding guidance
- Seed API keys into CI jobs as environment variables with short TTLs and monitor usage.
