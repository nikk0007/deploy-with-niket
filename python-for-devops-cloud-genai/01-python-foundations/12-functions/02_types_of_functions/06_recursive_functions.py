# ============================================================
# SECTION 6 — RECURSIVE FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

print("=" * 55)
print("  RECURSIVE FUNCTIONS — DevOps Examples")
print("=" * 55)

# ---- Basic Recursion — Kubernetes binary scaling ----

def calculate_replicas(scale_events):
    """
    Calculate replica count after N scale-up events.
    Each event doubles the replicas. Base: 1 replica.
    """
    if scale_events == 0:          # ← BASE CONDITION (must have this!)
        return 1
    return 2 * calculate_replicas(scale_events - 1)   # ← Recursive call


print("\n📌 calculate_replicas() — Kubernetes binary scaling:")
for n in range(6):
    print(f"  scale_events={n} → replicas={calculate_replicas(n)}")

print("\n📌 Call stack for calculate_replicas(3):")
print("  calculate_replicas(3)")
print("    → 2 * calculate_replicas(2)")
print("         → 2 * calculate_replicas(1)")
print("              → 2 * calculate_replicas(0)")
print("                   → returns 1")
print("  Final result: 2 × 2 × 2 × 1 = 8")


# ---- Real DevOps use case 1: Nested JSON config parser ----

def flatten_config(config, prefix=""):
    """
    Recursively flatten a nested config dict (like Helm values.yaml).
    e.g. {"app": {"port": 8080}} → {"app.port": 8080}
    """
    result = {}
    for key, value in config.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            result.update(flatten_config(value, full_key))   # ← Recursive call
        else:
            result[full_key] = value
    return result


helm_values = {
    "app": {
        "name": "payment-service",
        "port": 8080,
        "replicas": 3,
    },
    "resources": {
        "requests": {
            "cpu": "250m",
            "memory": "256Mi"
        },
        "limits": {
            "cpu": "500m",
            "memory": "512Mi"
        }
    },
    "env": "production"
}

print("\n📌 flatten_config() — Nested Helm values flattened:")
flat = flatten_config(helm_values)
for key, value in flat.items():
    print(f"  {key}: {value}")


# ---- Real DevOps use case 2: Directory tree (simulate) ----

def print_tree(structure, indent=0):
    """Recursively print a directory-like structure."""
    for name, content in structure.items():
        prefix = "  " * indent + ("📁 " if isinstance(content, dict) else "📄 ")
        print(f"{prefix}{name}")
        if isinstance(content, dict):
            print_tree(content, indent + 1)   # ← Recursive call


project_structure = {
    "my-devops-project": {
        "src": {
            "app.py": None,
            "utils.py": None,
        },
        "kubernetes": {
            "deployment.yaml": None,
            "service.yaml": None,
        },
        "Dockerfile": None,
        "requirements.txt": None,
    }
}

print("\n📌 print_tree() — Recursive directory traversal:")
print_tree(project_structure)

print("\n✅ RULE: Recursive functions mein BASE CONDITION zaruri hai!")
print("   Bina base condition ke → RecursionError (infinite loop)")
