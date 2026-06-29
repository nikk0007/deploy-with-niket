# ============================================================
# SECTION 11 — TYPE-HINTED FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

from typing import List, Dict, Optional, Tuple, Union

print("=" * 55)
print("  TYPE-HINTED FUNCTIONS — Modern Python Standard")
print("=" * 55)


# ---- Without type hints (old style) ----

def deploy_container_no_hints(image_name, replicas, environment, labels=None):
    """Without hints — IDE can't help you. What type is 'labels'? Who knows!"""
    if labels is None:
        labels = {}
    return {
        "image":       image_name,
        "replicas":    str(replicas),
        "environment": environment,
        "labels":      str(labels),
    }


# ---- With type hints (modern Python) ----

def deploy_container(
    image_name:  str,
    replicas:    int,
    environment: str,
    labels:      Optional[Dict[str, str]] = None
) -> Dict[str, str]:
    """
    With type hints:
    - IDE knows 'labels' is Optional[Dict[str, str]]
    - mypy can catch type errors before runtime
    - Auto-documentation in FastAPI
    """
    if labels is None:
        labels = {}
    return {
        "image":       image_name,
        "replicas":    str(replicas),
        "environment": environment,
        "labels":      str(labels),
    }


print("\n📌 deploy_container() — Type-hinted deployment function:")
result = deploy_container(
    image_name  = "myapp:v2.1",
    replicas    = 3,
    environment = "production",
    labels      = {"team": "backend", "app": "payment"}
)
for key, value in result.items():
    print(f"  {key}: {value}")


# ---- Type hints with List ----

def get_healthy_pods(pods: List[Dict[str, str]]) -> List[str]:
    """Returns names of healthy pods from a pod list."""
    return [
        pod["name"]
        for pod in pods
        if pod.get("status") == "Running"
    ]


pods = [
    {"name": "api-pod-1",    "status": "Running"},
    {"name": "db-pod-1",     "status": "Pending"},
    {"name": "cache-pod-1",  "status": "Running"},
    {"name": "worker-pod-1", "status": "CrashLoopBackOff"},
]

print("\n📌 get_healthy_pods() — List type hints:")
healthy = get_healthy_pods(pods)
print(f"  Healthy pods: {healthy}")


# ---- Type hints with Tuple return ----

def check_deployment_status(
    deployment_name: str,
    ready_replicas:  int,
    total_replicas:  int
) -> Tuple[bool, str]:
    """
    Returns (is_healthy: bool, message: str)
    Tuple hints tell caller exactly what to expect.
    """
    is_healthy = ready_replicas == total_replicas
    message = (
        f"✅ {deployment_name}: {ready_replicas}/{total_replicas} ready"
        if is_healthy
        else f"⚠️  {deployment_name}: Only {ready_replicas}/{total_replicas} ready"
    )
    return is_healthy, message


print("\n📌 check_deployment_status() — Tuple return type hint:")
ok, msg = check_deployment_status("payment-service", 3, 3)
print(f"  {msg}")
ok, msg = check_deployment_status("auth-service", 1, 3)
print(f"  {msg}")


# ---- Union type: parameter that accepts multiple types ----

def scale_service(
    service_name: str,
    replicas:     Union[int, str]   # Could be 3 or "auto"
) -> Dict[str, str]:
    """
    Union[int, str] — replicas can be a number OR "auto".
    Common in Kubernetes HPA (Horizontal Pod Autoscaler).
    """
    return {
        "service":  service_name,
        "replicas": str(replicas),
        "mode":     "auto-scale" if replicas == "auto" else "fixed"
    }


print("\n📌 scale_service() — Union type hint:")
print(f"  {scale_service('api-service', 5)}")
print(f"  {scale_service('ml-service', 'auto')}")


# ---- Type hints with Python 3.10+ syntax (modern shorthand) ----

def get_instance_cost(
    instance_type: str,
    hours:         int,
    discount:      float | None = None   # Python 3.10+ — same as Optional[float]
) -> float:
    base_rate = {"t3.micro": 0.0104, "c5.large": 0.085, "m5.xlarge": 0.192}
    rate = base_rate.get(instance_type, 0.10)
    cost = rate * hours
    if discount:
        cost = cost * (1 - discount)
    return round(cost, 4)


print("\n📌 get_instance_cost() — Python 3.10+ type hint syntax:")
print(f"  t3.micro  × 720h          = ${get_instance_cost('t3.micro',  720)}")
print(f"  c5.large  × 720h          = ${get_instance_cost('c5.large',  720)}")
print(f"  m5.xlarge × 720h (20% off)= ${get_instance_cost('m5.xlarge', 720, 0.20)}")


print("\n✅ WHY TYPE HINTS?")
print("   1️⃣  IDE auto-complete & error highlighting in VS Code / PyCharm")
print("   2️⃣  mypy / pyright se production se pehle bugs pakdo")
print("   3️⃣  FastAPI mein type hints se automatic API docs banti hai")
print("   4️⃣  Code zyada readable hota hai — parameters ka purpose clear")
print("\n✅ RULE: Naya code ALWAYS type hints ke saath likho!")
