# ============================================================
# SECTION 5 — PURE vs IMPURE FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

print("=" * 55)
print("  PURE vs IMPURE FUNCTIONS")
print("=" * 55)

# ---- PURE FUNCTION ----

def calculate_monthly_cost(instances: int, hours_per_day: int, cost_per_hour: float) -> float:
    """Pure function — same inputs ALWAYS give same output. No side effects."""
    return instances * hours_per_day * 30 * cost_per_hour


print("\n📌 PURE function — calculate_monthly_cost():")
print(f"  Call 1: ${calculate_monthly_cost(10, 8, 0.096):.2f}")
print(f"  Call 2: ${calculate_monthly_cost(10, 8, 0.096):.2f}  ← Same result, always!")
print(f"  Call 3: ${calculate_monthly_cost(10, 8, 0.096):.2f}  ← Predictable. Testable.")

# Pure: another example
def is_pod_healthy(pod: dict) -> bool:
    """Pure — just reads input, returns a bool, touches nothing else."""
    return pod.get("status") == "Running" and pod.get("restart_count", 0) < 5

pods = [
    {"name": "api-pod",    "status": "Running",  "restart_count": 0},
    {"name": "worker-pod", "status": "Running",  "restart_count": 7},
    {"name": "db-pod",     "status": "Pending",  "restart_count": 0},
]

print("\n📌 PURE function — is_pod_healthy():")
for pod in pods:
    result = is_pod_healthy(pod)
    icon = "🟢" if result else "🔴"
    print(f"  {icon} {pod['name']}: healthy={result}")


# ---- IMPURE FUNCTION ----

print("\n" + "-" * 55)

total_api_calls = 0   # Global state — danger zone!

def call_llm_api_impure(prompt):
    """Impure — modifies global state as a SIDE EFFECT."""
    global total_api_calls
    total_api_calls += 1   # Side effect: secretly modifying global var
    return f"AI response for: {prompt}"


print("\n📌 IMPURE function — call_llm_api_impure():")
call_llm_api_impure("Explain Kubernetes")
call_llm_api_impure("Explain Docker")
print(f"  total_api_calls (global) = {total_api_calls}")
print("  ⚠️  This global state can get corrupted in multi-threaded code!")


# ---- BETTER: Refactored Pure Version ----

print("\n" + "-" * 55)

def call_llm_api_pure(prompt: str, current_count: int) -> tuple:
    """
    Pure version — takes count in, returns updated count out.
    No global state modified.
    """
    response = f"AI response for: {prompt}"
    new_count = current_count + 1
    return response, new_count


print("\n📌 REFACTORED to PURE — call_llm_api_pure():")
api_calls = 0
response1, api_calls = call_llm_api_pure("Explain Kubernetes", api_calls)
response2, api_calls = call_llm_api_pure("Explain Docker", api_calls)
print(f"  Response 1: {response1}")
print(f"  Response 2: {response2}")
print(f"  Total calls: {api_calls}")
print("  ✅ No global state touched. Predictable. Thread-safe.")


print("\n" + "=" * 55)
print("  RULES TO REMEMBER:")
print("  ✅ Default: Pure functions likhne ki koshish karo")
print("  ⚠️  Impure: Sirf I/O ke liye — DB, API, Files")
print("  ❌ Impure functions ACCIDENTALLY mat likho")
print("=" * 55)
