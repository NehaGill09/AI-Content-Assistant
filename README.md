# AI Content Assistant

Production-oriented AI content platform using Django REST Framework, React + TypeScript, PostgreSQL/pgvector, Redis, Celery, and OpenAI.

## Implemented
- Structured AI generation with Pydantic outputs
- Versioned prompt registry foundation
- AI telemetry for latency, tokens, model, and estimated cost
- JWT authentication and DRF throttling
- Workspace/document/version data model
- Redis cache and Celery worker integration
- Database and Redis health checks
- Django migrations and CI checks
- Strict React TypeScript/Vite build configuration

## Run

Copy `.env.example` to `.env`, set `OPENAI_API_KEY`, then run `docker compose up --build`.

See `docs/architecture.md` for the architecture and next extension areas: RAG, prompt evaluation, streaming, RBAC/API keys, and analytics.
