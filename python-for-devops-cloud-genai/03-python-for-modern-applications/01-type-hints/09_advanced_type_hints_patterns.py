# ============================================================
# FILE 09 — Bonus: Advanced Type Hints Patterns
# Production-grade patterns used in DevOps, Cloud, GenAI code
# ============================================================

from typing import Callable, Any
from collections.abc import Generator


# ============================================================
# PATTERN 1 — TypeAlias: Give a complex type a readable name
# ============================================================

# Instead of repeating dict[str, int | float | bool] everywhere:
ServerMetrics = dict[str, int | float | bool]

def get_server_metrics(server_id: str) -> ServerMetrics:
    return {
        "cpu_usage": 72.5,
        "memory_gb": 14,
        "is_healthy": True,
        "active_connections": 340
    }

metrics = get_server_metrics("prod-01")
print(metrics)


# ============================================================
# PATTERN 2 — Callable: Type hint for a function parameter
# ============================================================

# When you pass a function as an argument to another function

def run_with_retry(
    operation: Callable[[], bool],   # A function that takes no args and returns bool
    max_retries: int = 3
) -> bool:
    for attempt in range(1, max_retries + 1):
        print(f"Attempt {attempt}...")
        if operation():
            return True
    return False


def deploy_to_production() -> bool:
    print("Deploying...")
    return True   # Simulate success

result = run_with_retry(deploy_to_production, max_retries=3)
print(f"Deployment succeeded: {result}")


# ============================================================
# PATTERN 3 — dict with Any: When values can be anything
# ============================================================

from typing import Any

def parse_api_response(response: dict[str, Any]) -> str:
    status = response.get("status", "unknown")
    return f"API Status: {status}"

api_data: dict[str, Any] = {
    "status": "success",
    "data": [1, 2, 3],
    "meta": {"page": 1, "total": 100},
    "cached": True
}

print(parse_api_response(api_data))


# ============================================================
# PATTERN 4 — Generator type hints
# ============================================================

def read_log_lines(filepath: str) -> Generator[str, None, None]:
    """
    Yields one log line at a time — memory efficient for large files.
    """
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

# Usage would be:
# for line in read_log_lines("/var/log/app.log"):
#     print(line)


# ============================================================
# PATTERN 5 — Full typed function: DevOps automation example
# ============================================================

class AlertConfig(object):
    def __init__(self, channel: str, threshold: float, enabled: bool):
        self.channel = channel
        self.threshold = threshold
        self.enabled = enabled


def evaluate_and_alert(
    service_name: str,
    current_cpu: float,
    alert_configs: list[AlertConfig],
    notify_fn: Callable[[str, str], None]
) -> dict[str, bool]:
    """
    Evaluates CPU usage for a service.
    Fires alerts via notify_fn if any configured threshold is breached.
    Returns a dict mapping channel name to whether alert was sent.
    """
    results: dict[str, bool] = {}

    for config in alert_configs:
        if config.enabled and current_cpu > config.threshold:
            message = f"ALERT: {service_name} CPU at {current_cpu}% — threshold {config.threshold}%"
            notify_fn(config.channel, message)
            results[config.channel] = True
        else:
            results[config.channel] = False

    return results


def send_slack_notification(channel: str, message: str) -> None:
    print(f"[Slack → #{channel}] {message}")


configs = [
    AlertConfig("devops-alerts", 80.0, True),
    AlertConfig("on-call", 90.0, True),
    AlertConfig("management", 95.0, False),
]

outcome = evaluate_and_alert(
    service_name="payment-api",
    current_cpu=87.3,
    alert_configs=configs,
    notify_fn=send_slack_notification
)

print(outcome)


# ============================================================
# PATTERN 6 — Type hints inside class methods
# ============================================================

class PipelineStage:
    def __init__(self, name: str, timeout_seconds: int):
        self.name = name
        self.timeout_seconds = timeout_seconds
        self.logs: list[str] = []
        self.is_complete: bool = False

    def run(self, input_data: dict[str, Any]) -> dict[str, Any]:
        self.logs.append(f"Stage '{self.name}' started")
        # ... process input_data ...
        self.is_complete = True
        self.logs.append(f"Stage '{self.name}' complete")
        return {"stage": self.name, "status": "success"}

    def get_logs(self) -> list[str]:
        return self.logs

    @classmethod
    def create_default(cls, name: str) -> "PipelineStage":
        return cls(name=name, timeout_seconds=300)


stage = PipelineStage.create_default("build")
output = stage.run({"repo": "my-service", "branch": "main"})
print(output)
print(stage.get_logs())


# ============================================================
# QUICK REFERENCE — All patterns in one place
#
# Basic:
#   x: int = 5
#   def fn(a: str) -> bool: ...
#
# Collections:
#   list[int]  |  dict[str, float]  |  tuple[str, int]
#
# Optional / Union:
#   str | None  |  int | str
#
# Type Alias:
#   Metrics = dict[str, int | float]
#
# Callable:
#   Callable[[str, int], bool]   → takes str+int, returns bool
#   Callable[[], None]           → takes nothing, returns nothing
#
# Any:
#   dict[str, Any]   → values can be anything
#
# Generator:
#   Generator[YieldType, SendType, ReturnType]
#
# Self-reference in class:
#   def clone(self) -> "MyClass": ...
# ============================================================
