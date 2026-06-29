# ============================================================
# 08_devops_usecase_kubernetes.py
# Topic: Real DevOps Use Case — Kubernetes Pod Self-Healing
# ============================================================

# In production Kubernetes clusters, pods fail.
# A self-healing script checks pod status and restarts failed pods automatically.
#
# Key concept: one function calls another — function composition.
# get_pod_status() feeds its result into heal_failed_pod().
# Each function does one job. Together they form a complete workflow.
#
# NOTE: Simulated without a live cluster. In production, replace the
#       simulated data with real kubernetes-client API calls (shown in comments).

# ---- Simulated cluster state ----

SIMULATED_PODS = {
    ("production", "payment-service-pod-7f9b"):   "Failed",
    ("production", "auth-service-pod-3a2c"):       "Running",
    ("production", "notification-pod-9d1e"):       "Pending",
    ("staging",    "search-service-pod-4b8f"):     "Running",
    ("staging",    "analytics-pod-2c6a"):          "Failed",
}

# ---- Function 1: Get pod status ----

def get_pod_status(namespace, pod_name):
    """
    Return the current phase of a Kubernetes pod.
    Possible values: 'Running', 'Pending', 'Failed', 'Succeeded', 'Unknown'

    In production, replace the simulated lookup with:
        from kubernetes import client, config
        config.load_kube_config()
        v1 = client.CoreV1Api()
        pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
        return pod.status.phase
    """
    return SIMULATED_PODS.get((namespace, pod_name), "Unknown")


# ---- Function 2: Restart a pod ----

def restart_pod(namespace, pod_name):
    """
    Delete a failed pod so Kubernetes recreates it automatically.
    Kubernetes will spin up a new pod as per the Deployment spec.

    In production:
        from kubernetes import client, config
        config.load_kube_config()
        v1 = client.CoreV1Api()
        v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
    """
    print(f"    Deleting pod '{pod_name}' from namespace '{namespace}'...")
    print(f"    Kubernetes will recreate the pod automatically via the Deployment controller.")
    # Update simulated state so subsequent calls reflect the change
    SIMULATED_PODS[(namespace, pod_name)] = "Pending"


# ---- Function 3: Self-healing orchestrator — calls the two above ----

def heal_failed_pod(namespace, pod_name):
    """
    Check a pod's status and take action:
      - Failed  → restart it automatically
      - Pending → flag for monitoring
      - Running → no action needed
      - Unknown → escalate for manual review
    """
    print(f"  Checking pod: {pod_name} | Namespace: {namespace}")
    status = get_pod_status(namespace, pod_name)   # calls function 1
    print(f"  Current status: {status}")

    if status == "Failed":
        print(f"  Pod has failed. Initiating automatic restart...")
        restart_pod(namespace, pod_name)            # calls function 2
        print(f"  Restart triggered successfully.\n")

    elif status == "Running":
        print(f"  Pod is healthy. No action needed.\n")

    elif status == "Pending":
        print(f"  Pod is pending. Will monitor — no action yet.\n")

    else:
        print(f"  Status '{status}' is unexpected. Escalating to on-call SRE.\n")


# ---- Run the self-healing sweep ----

pods_to_check = [
    ("production", "payment-service-pod-7f9b"),
    ("production", "auth-service-pod-3a2c"),
    ("production", "notification-pod-9d1e"),
    ("staging",    "search-service-pod-4b8f"),
    ("staging",    "analytics-pod-2c6a"),
]

print("=" * 55)
print("  Kubernetes Self-Healing Sweep — Starting")
print("=" * 55 + "\n")

for namespace, pod_name in pods_to_check:
    heal_failed_pod(namespace, pod_name)

print("=" * 55)
print("  Sweep complete.")
print("=" * 55)

print("""
Key lesson — function composition:
  heal_failed_pod() calls get_pod_status() and restart_pod().
  Each function does exactly one job.
  The orchestrator function combines them into a complete workflow.
  Add logging, alerting, or Slack notifications?
  Write a new function — plug it in. Nothing else changes.
""")
