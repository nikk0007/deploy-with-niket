# ============================================================
# SECTION 4 — LAMBDA + HIGHER-ORDER FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

print("=" * 55)
print("  LAMBDA + HIGHER-ORDER FUNCTIONS")
print("=" * 55)

# ---- LAMBDA FUNCTIONS ----

# filter() — Sirf Running pods chahiye
pods = [
    {"name": "api-pod-1",    "status": "Running"},
    {"name": "db-pod-1",     "status": "Pending"},
    {"name": "cache-pod-1",  "status": "Running"},
    {"name": "worker-pod-1", "status": "CrashLoopBackOff"},
]

print("\n📌 filter() + lambda — Running pods only:")
running_pods = list(filter(lambda pod: pod["status"] == "Running", pods))
for pod in running_pods:
    print(f"  ✅ {pod['name']} — {pod['status']}")

print("\n📌 filter() + lambda — Pods NOT Running (for alert):")
unhealthy_pods = list(filter(lambda pod: pod["status"] != "Running", pods))
for pod in unhealthy_pods:
    print(f"  🔴 {pod['name']} — {pod['status']}")


# map() — CPU readings pe 10% overhead add karna (e.g., monitoring headroom)
cpu_readings = [40, 65, 80, 55, 70]
print("\n📌 map() + lambda — CPU scaled by 1.1x:")
scaled = list(map(lambda x: round(x * 1.1, 2), cpu_readings))
print(f"  Original: {cpu_readings}")
print(f"  Scaled:   {scaled}")


# sorted() with lambda — Instances ko CPU se sort karna
instances = [
    {"id": "i-001", "cpu": 75},
    {"id": "i-002", "cpu": 45},
    {"id": "i-003", "cpu": 90},
    {"id": "i-004", "cpu": 30},
]
print("\n📌 sorted() + lambda — Instances sorted by CPU (ascending):")
sorted_asc = sorted(instances, key=lambda x: x["cpu"])
for inst in sorted_asc:
    print(f"  {inst['id']} → {inst['cpu']}%")

print("\n📌 sorted() + lambda — Sorted by CPU (descending — highest load first):")
sorted_desc = sorted(instances, key=lambda x: x["cpu"], reverse=True)
for inst in sorted_desc:
    print(f"  {inst['id']} → {inst['cpu']}%")


# ---- HIGHER-ORDER FUNCTIONS ----

print("\n" + "=" * 55)
print("  HIGHER-ORDER FUNCTIONS")
print("=" * 55)

# A function that takes another function as argument
def execute_with_retry(func, retries=3):
    """Execute a function with automatic retry on failure."""
    for attempt in range(1, retries + 1):
        try:
            print(f"  Attempt {attempt}/{retries}...")
            return func()
        except Exception as e:
            print(f"  ❌ Failed: {e}")
    print("  ⛔ All attempts exhausted. Giving up.")
    return None


def fetch_aws_token():
    """Simulates a flaky AWS token endpoint."""
    raise ConnectionError("AWS endpoint unreachable")


print("\n📌 execute_with_retry() — Higher-order function:")
result = execute_with_retry(fetch_aws_token, retries=3)
print(f"  Result: {result}")


# A function that RETURNS another function
def make_alert_checker(threshold):
    """Returns a function that checks if a value exceeds a threshold."""
    def check(value):
        if value > threshold:
            return f"🔴 ALERT! Value {value} exceeds threshold {threshold}"
        return f"🟢 OK — Value {value} is within threshold {threshold}"
    return check

print("\n📌 make_alert_checker() — Function returning a function:")
cpu_alert  = make_alert_checker(80)
mem_alert  = make_alert_checker(90)

print(cpu_alert(91))
print(cpu_alert(55))
print(mem_alert(95))

print("\n✅ Higher-Order Functions = Functions joh functions ko IN/OUT karte hain")
print("✅ Yeh Decorators ki neenv hai — agle section mein dekhenge!")
