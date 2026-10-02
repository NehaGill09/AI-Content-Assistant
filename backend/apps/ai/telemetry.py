import time
from dataclasses import dataclass

@dataclass
class AITelemetry:
    model: str
    latency_ms: int
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    @property
    def estimated_cost_usd(self) -> float:
        return round((self.prompt_tokens / 1_000_000) * 0.15 + (self.completion_tokens / 1_000_000) * 0.60, 8)

class Timer:
    def __enter__(self):
        self.started = time.perf_counter()
        return self
    def __exit__(self, *_):
        self.elapsed_ms = int((time.perf_counter() - self.started) * 1000)
