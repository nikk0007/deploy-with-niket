# SECTION 7 DEMO — Use Case 2: Kubernetes Pod Status & Auto-Restart
# NOTE: requires `pip install kubernetes` and a valid kubeconfig to actually run.
# This demonstrates the PATTERN — code structure is real and production-accurate.

from kubernetes import client, config

def get_pod_status(namespace, pod_name):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
    return pod.status.phase   # "Running", "Pending", "Failed"

def heal_failed_pod(namespace, pod_name):
    status = get_pod_status(namespace, pod_name)
    if status == "Failed":
        print(f"Pod {pod_name} has failed. Initiating restart sequence...")
        v1 = client.CoreV1Api()
        v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
        print(f"Pod {pod_name} deleted — Kubernetes will recreate it automatically.")
    elif status == "Running":
        print(f"Pod {pod_name} is healthy. No action needed.")
    else:
        print(f"Pod {pod_name} status: {status}. Manual review recommended.")

heal_failed_pod("production", "payment-service-pod-7f9b")

# Notice karo — heal_failed_pod function get_pod_status function ko call kar raha hai.
# Ek function doosre ka building block ban gaya.
# Yahi hai real-world function composition.
