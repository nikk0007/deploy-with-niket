# Section 7 - Use Case 2: Kubernetes Namespace Health Summary
#
# Same approach as the S3 file: a real version using the kubernetes
# client (needs a real cluster/kubeconfig), and a simulated version
# with the identical return signature for a live, no-cluster-needed demo.

# ---------------------------------------------------------------
# 1) REAL VERSION (uncomment to use with a real Kubernetes cluster)
# ---------------------------------------------------------------
#
# from kubernetes import client, config
#
# def get_namespace_health(namespace):
#     config.load_kube_config()
#     v1 = client.CoreV1Api()
#
#     pods = v1.list_namespaced_pod(namespace=namespace)
#     total_pods = len(pods.items)
#     running = sum(1 for p in pods.items if p.status.phase == "Running")
#     failed = sum(1 for p in pods.items if p.status.phase == "Failed")
#     pending = sum(1 for p in pods.items if p.status.phase == "Pending")
#
#     services = v1.list_namespaced_service(namespace=namespace)
#     total_services = len(services.items)
#
#     return total_pods, running, failed, pending, total_services


# ---------------------------------------------------------------
# 2) SIMULATED VERSION - same return signature, runs anywhere
# ---------------------------------------------------------------
def get_namespace_health(namespace):
    """Simulated namespace health check for live demo purposes."""
    fake_namespace_data = {
        "production": {"total_pods": 24, "running": 21, "failed": 2, "pending": 1, "services": 8},
        "staging": {"total_pods": 10, "running": 10, "failed": 0, "pending": 0, "services": 4}
    }

    info = fake_namespace_data.get(
        namespace, {"total_pods": 0, "running": 0, "failed": 0, "pending": 0, "services": 0}
    )
    return info["total_pods"], info["running"], info["failed"], info["pending"], info["services"]


total, running, failed, pending, services = get_namespace_health("production")

print(f"Total Pods : {total}")
print(f"Running    : {running}")
print(f"Failed     : {failed}")
print(f"Pending    : {pending}")
print(f"Services   : {services}")

if failed > 0:
    print(f"\nALERT: {failed} failed pod(s) in production namespace!")
