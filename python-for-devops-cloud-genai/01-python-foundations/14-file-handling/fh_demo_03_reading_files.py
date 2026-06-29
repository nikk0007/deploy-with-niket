"""
DEMO 03: Reading Files — Four Strategies
Topic: File Handling in Python
Use Case: DevOps/Cloud — Processing Kubernetes event logs, config files,
          and cloud resource inventory files

Demonstrates:
  - read()       → entire file as string (small configs, manifests)
  - readline()   → one line at a time (streaming large logs)
  - readlines()  → all lines as list (small files with random access)
  - for loop     → most memory-efficient (large files, log processing)
"""

import os
import tempfile

DEMO_DIR = tempfile.mkdtemp(prefix="python_fh_demo03_")


def demo_path(name):
    return os.path.join(DEMO_DIR, name)


# ─────────────────────────────────────────────────────────────────────────────
# Setup: Create sample files representing real DevOps artifacts
# ─────────────────────────────────────────────────────────────────────────────

# 1. A small Kubernetes deployment manifest (typical config file)
K8S_MANIFEST = demo_path("deployment.yaml")
with open(K8S_MANIFEST, "w") as f:
    f.write("""\
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api-server
  template:
    spec:
      containers:
        - name: api-server
          image: myorg/api-server:v2.4.1
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
""")

# 2. A simulated Kubernetes event log (large file scenario)
K8S_EVENT_LOG = demo_path("k8s_events.log")
log_entries = [
    "2024-01-15T03:40:00Z INFO  pod/api-server-abc Starting container",
    "2024-01-15T03:40:02Z INFO  pod/api-server-abc Container started",
    "2024-01-15T03:40:10Z WARN  pod/redis-xyz High memory usage: 89%",
    "2024-01-15T03:40:15Z ERROR pod/nginx-abc OOMKilled: container exceeded memory limit",
    "2024-01-15T03:40:20Z INFO  pod/api-server-def Readiness probe passed",
    "2024-01-15T03:40:25Z ERROR pod/db-migration-job BackoffLimitExceeded",
    "2024-01-15T03:40:30Z WARN  pod/cache-abc Liveness probe failed (attempt 2/3)",
    "2024-01-15T03:40:35Z ERROR pod/cache-abc OOMKilled: container exceeded memory limit",
    "2024-01-15T03:40:40Z INFO  node/ip-10-0-1-5 Node condition Ready=True",
    "2024-01-15T03:40:45Z INFO  pod/api-server-ghi Container started",
]
with open(K8S_EVENT_LOG, "w") as f:
    f.write("\n".join(log_entries) + "\n")

# 3. A cloud resource inventory (random access needed)
RESOURCE_INVENTORY = demo_path("ec2_inventory.txt")
instances = [
    "i-0abc123 | ap-south-1a | t3.medium  | running  | api-server-1",
    "i-0def456 | ap-south-1b | t3.large   | running  | api-server-2",
    "i-0ghi789 | ap-south-1a | m5.xlarge  | stopped  | batch-worker",
    "i-0jkl012 | ap-south-1b | t3.micro   | running  | monitoring",
    "i-0mno345 | ap-south-1a | c5.2xlarge | running  | ml-inference",
]
with open(RESOURCE_INVENTORY, "w") as f:
    f.write("\n".join(instances) + "\n")


# ─────────────────────────────────────────────────────────────────────────────
# STRATEGY 1: read() — Entire file as a single string
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("STRATEGY 1: read() — Entire file as a string")
print("Best for: Small config files, YAML manifests, prompt templates")
print("=" * 60)

with open(K8S_MANIFEST, "r", encoding="utf-8") as f:
    manifest_content = f.read()

print(f"[OK] Loaded entire manifest: {len(manifest_content)} characters")
print(f"[Type] {type(manifest_content)}")
print()

# Common use: check something in the manifest
if "OOMKilled" not in manifest_content:
    print("[Check] No OOMKilled mentions in manifest ✅")

# Practical use: pass to a YAML parser
import re
replicas_match = re.search(r"replicas:\s*(\d+)", manifest_content)
if replicas_match:
    print(f"[Parsed] Replica count from manifest: {replicas_match.group(1)}")

print()
print("⚠️  DO NOT use read() for large files (multi-GB logs)")
print("    It loads the entire file into RAM at once.")


# ─────────────────────────────────────────────────────────────────────────────
# STRATEGY 2: readline() — One line at a time
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("STRATEGY 2: readline() — One line at a time")
print("Best for: Large files where you process and possibly stop early")
print("=" * 60)

def find_first_critical_event(log_path):
    """
    Reads a log file line by line.
    Stops as soon as the first OOMKilled event is found.
    Useful for large log files where early termination saves time.
    """
    with open(log_path, "r") as f:
        line_num = 0
        line = f.readline()
        while line:
            line_num += 1
            if "OOMKilled" in line:
                print(f"  [Found at line {line_num}] {line.strip()}")
                return line.strip()
            line = f.readline()
    return None

print("[Scanning for first OOMKilled event...]")
first_oom = find_first_critical_event(K8S_EVENT_LOG)
print(f"[Result] First critical event: {first_oom}")


# ─────────────────────────────────────────────────────────────────────────────
# STRATEGY 3: readlines() — All lines as a list
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("STRATEGY 3: readlines() — All lines as a list")
print("Best for: Small files where you need index-based access")
print("=" * 60)

with open(RESOURCE_INVENTORY, "r") as f:
    raw_lines = f.readlines()

# Clean up trailing newlines
instances = [line.strip() for line in raw_lines if line.strip()]
print(f"[OK] Loaded {len(instances)} EC2 instances from inventory")

# Access specific instances by index
print(f"\n[Instance 0 - first]  {instances[0]}")
print(f"[Instance -1 - last]  {instances[-1]}")

# Filter: find stopped instances
print("\n[Stopped instances]:")
stopped = [i for i in instances if "stopped" in i]
for inst in stopped:
    print(f"  → {inst}")

print(f"\n⚠️  readlines() loads all lines into memory.")
print("    Safe for small-to-medium files (MBs), not for multi-GB logs.")


# ─────────────────────────────────────────────────────────────────────────────
# STRATEGY 4: for loop — Most memory-efficient (recommended for large files)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("STRATEGY 4: for loop — Memory-efficient, line by line")
print("Best for: Large log files, streaming processing, audit pipelines")
print("=" * 60)

def analyze_k8s_events(log_path):
    """
    Scans the entire event log for issues.
    Uses a for loop — Python reads one line at a time internally.
    Handles files of any size without memory pressure.
    """
    summary = {"total": 0, "errors": [], "warnings": [], "oom_events": []}

    with open(log_path, "r") as f:
        for line in f:           # Python reads one line at a time
            line = line.strip()
            if not line:
                continue
            summary["total"] += 1
            if "ERROR" in line:
                summary["errors"].append(line)
            if "WARN" in line:
                summary["warnings"].append(line)
            if "OOMKilled" in line:
                summary["oom_events"].append(line)

    return summary

print("[Analyzing Kubernetes event log...]")
report = analyze_k8s_events(K8S_EVENT_LOG)
print(f"\n[Event Analysis Report]")
print(f"  Total events   : {report['total']}")
print(f"  ERROR events   : {len(report['errors'])}")
print(f"  WARN  events   : {len(report['warnings'])}")
print(f"  OOMKilled      : {len(report['oom_events'])}")
print(f"\n[OOMKilled Events]:")
for event in report["oom_events"]:
    print(f"  → {event}")

print()
print("✅ for loop is the most Pythonic and memory-safe approach.")
print("   Use it as your default for any file processing in production.")


# ─────────────────────────────────────────────────────────────────────────────
# Quick comparison summary
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("COMPARISON: When to use which strategy")
print("=" * 60)
print("read()      → Small files (<10 MB). Need full content at once.")
print("             Example: Kubernetes manifest, Terraform vars file,")
print("             LLM prompt template, Docker Compose file")
print()
print("readline()  → Any file size. Need early exit / streaming.")
print("             Example: Find first error in a massive CI log")
print()
print("readlines() → Small files. Need index access to specific lines.")
print("             Example: List of hostnames, IP list, failed pod names")
print()
print("for loop    → ANY file size. Most memory-efficient.")
print("             Example: Multi-GB cloud audit log, large CSV, access logs")

import shutil
shutil.rmtree(DEMO_DIR)
print(f"\n[Cleanup] Removed demo directory.")
print("[Done] Demo 03 complete.")
