# Architecture

The platform separates HTTP, application orchestration, AI providers and persistence.

## AI pipeline
Request → validation → prompt construction → model provider → typed structured output → persistence → audit/usage telemetry.

## Production roadmap
- Prompt registry with immutable versions and evaluation datasets
- Streaming generation over SSE
- pgvector ingestion/retrieval for RAG
- Celery jobs for embeddings and long-running generations
- Workspace RBAC, API keys, throttling and idempotency
- Cost/latency dashboards and distributed tracing
- CI quality gates and deployment manifests
