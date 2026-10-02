# AI Content Assistant

Production-oriented AI content platform using Django REST Framework, React + TypeScript, PostgreSQL/pgvector, Redis, Celery, and OpenAI.

## Implemented
- Structured AI generation with typed Pydantic outputs
- Prompt registry, versioning, and deterministic evaluation cases
- AI telemetry: tokens, latency, model and estimated cost
- Server-sent event streaming generation
- RAG knowledge ingestion with OpenAI embeddings, pgvector storage, similarity retrieval primitives, and Celery indexing
- JWT authentication plus hashed, revocable API keys
- Workspace/document/version data model and audit foundation
- Usage analytics endpoint
- Redis cache and Celery worker integration
- Database and Redis health checks
- Django migrations including pgvector extension setup
- Strict React TypeScript/Vite build configuration
- Backend tests and CI quality gates

## API highlights
- `POST /api/ai/generate/`
- `POST /api/ai/stream/`
- `GET /api/ai/usage/`
- `POST /api/ai/knowledge/`
- `POST /api/ai/evals/{case_id}/run/`
- `POST /api/auth/api-keys/create/`
- `GET /api/auth/api-keys/`
- `GET /health/`

## Run

Copy `.env.example` to `.env`, set `OPENAI_API_KEY`, then run `docker compose up --build`.

See `docs/architecture.md` for the system design.
