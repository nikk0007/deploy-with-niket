"""
DEMO 04: Writing and Appending Files
Topic: File Handling in Python
Use Case: DevOps/Cloud/GenAI — Pipeline logs, scan reports, LLM outputs,
          failed resource lists

Demonstrates:
  - write()      → writing a string to a file
  - writelines() → writing a list of strings
  - "w" mode     → fresh file every run (reports, exports)
  - "a" mode     → accumulating data (logs, audit trails)
  - encoding     → why utf-8 matters in production
  - flush()      → forcing buffer to disk immediately
"""

import os
import json
import tempfile
from datetime import datetime, timezone

DEMO_DIR = tempfile.mkdtemp(prefix="python_fh_demo04_")


def demo_path(name):
    return os.path.join(DEMO_DIR, name)


def utcnow():
    return datetime.now(timezone.utc).isoformat()


# ─────────────────────────────────────────────────────────────────────────────
# PART 1: write() — Writing a string to a file
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("PART 1: write() — Writing a single string to a file")
print("=" * 60)

scan_report = {
    "scan_id": "sec-scan-2024-001",
    "target": "prod-cluster",
    "timestamp": utcnow(),
    "critical_findings": 2,
    "high_findings": 7,
    "passed_checks": 143,
    "findings": [
        {"id": "CVE-2024-0001", "severity": "CRITICAL", "resource": "nginx:1.21"},
        {"id": "CVE-2024-0002", "severity": "CRITICAL", "resource": "redis:6.2"},
    ]
}

report_path = demo_path("security_scan_report.json")

with open(report_path, "w", encoding="utf-8") as f:
    f.write(json.dumps(scan_report, indent=2))

print(f"[OK] Security scan report written to: {os.path.basename(report_path)}")

# Verify
with open(report_path, "r") as f:
    loaded = json.load(f)
print(f"[Verify] critical_findings: {loaded['critical_findings']}")
print(f"[Verify] passed_checks: {loaded['passed_checks']}")
print()
print("✅ 'w' mode is correct here — we generate a fresh report on every scan run.")
print("⚠️  If we used 'a', we'd get malformed JSON (multiple JSON objects concatenated).")


# ─────────────────────────────────────────────────────────────────────────────
# PART 2: writelines() — Writing a list of strings
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 2: writelines() — Writing a list of strings")
print("=" * 60)

failed_pods = [
    "pod/nginx-gateway-abc123",
    "pod/redis-cache-def456",
    "pod/ml-worker-ghi789",
    "pod/api-server-jkl012",
]

failed_pods_file = demo_path("failed_pods.txt")

with open(failed_pods_file, "w") as f:
    # writelines() does NOT add newlines — you must add them yourself
    f.writelines([pod + "\n" for pod in failed_pods])

print(f"[OK] Failed pods list written: {len(failed_pods)} pods")

with open(failed_pods_file, "r") as f:
    content = f.read()
print(f"[Content]\n{content}")
print("⚠️  writelines() does NOT add '\\n' automatically. Always add it explicitly.")


# ─────────────────────────────────────────────────────────────────────────────
# PART 3: "a" mode — Appending to a log file across multiple "runs"
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("PART 3: Append mode — Simulating multiple deployment runs")
print("=" * 60)

deployment_log = demo_path("deployment_history.log")

def log_deployment(cluster, namespace, image, status):
    """Appends a deployment record to the audit log."""
    entry = (
        f"[{utcnow()}] "
        f"cluster={cluster} namespace={namespace} "
        f"image={image} status={status}\n"
    )
    with open(deployment_log, "a", encoding="utf-8") as f:
        f.write(entry)

# Simulate 4 deployment events happening over time
deployments = [
    ("prod-cluster", "production",  "myapp/api:v2.3.0",    "SUCCESS"),
    ("prod-cluster", "production",  "myapp/worker:v1.8.1",  "SUCCESS"),
    ("prod-cluster", "staging",     "myapp/api:v2.4.0-rc1", "FAILED"),
    ("prod-cluster", "production",  "myapp/api:v2.3.1",    "SUCCESS"),
]

for cluster, ns, image, status in deployments:
    log_deployment(cluster, ns, image, status)

print(f"[OK] {len(deployments)} deployment events logged.")

with open(deployment_log, "r") as f:
    all_entries = f.readlines()

print(f"[Log has {len(all_entries)} entries — all preserved]")
print()
for entry in all_entries:
    status_marker = "✅" if "SUCCESS" in entry else "❌"
    print(f"  {status_marker} {entry.strip()}")

print()
print("✅ All entries preserved — 'a' mode never erases existing content.")


# ─────────────────────────────────────────────────────────────────────────────
# PART 4: The "w" vs "a" danger demo — side by side
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 4: The 'w' vs 'a' Danger — Side by Side")
print("=" * 60)

bad_log = demo_path("bad_log_w_mode.log")
good_log = demo_path("good_log_a_mode.log")

# Simulating 3 script runs
for run in range(1, 4):
    # BAD: Using "w" mode for a log
    with open(bad_log, "w") as f:
        f.write(f"[Run {run}] Pipeline completed at {utcnow()}\n")

    # GOOD: Using "a" mode for a log
    with open(good_log, "a") as f:
        f.write(f"[Run {run}] Pipeline completed at {utcnow()}\n")

with open(bad_log, "r") as f:
    bad_content = f.readlines()
with open(good_log, "r") as f:
    good_content = f.readlines()

print(f"[BAD  - 'w' mode] Entries in log after 3 runs: {len(bad_content)}")
print(f"  Content: {bad_content[0].strip()}")
print(f"  ⚠️  Only the LAST run is visible. Runs 1 and 2 were silently erased.")

print()
print(f"[GOOD - 'a' mode] Entries in log after 3 runs: {len(good_content)}")
for entry in good_content:
    print(f"  ✅ {entry.strip()}")


# ─────────────────────────────────────────────────────────────────────────────
# PART 5: Encoding matters — GenAI LLM output with Unicode
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 5: Encoding — Always specify utf-8 in production")
print("=" * 60)

# LLM outputs often contain Unicode characters — arrows, bullets, special chars
llm_output = """\
## Deployment Analysis

✅ Pod api-server is healthy (3/3 replicas running)
⚠️  Pod redis-cache is using 89% memory — consider scaling up
❌ Pod nginx-gateway has CrashLoopBackOff — check container logs
→ Recommended action: kubectl describe pod nginx-gateway -n production
"""

llm_output_file = demo_path("llm_deployment_analysis.txt")

with open(llm_output_file, "w", encoding="utf-8") as f:
    f.write(llm_output)

print(f"[OK] LLM output with Unicode written successfully.")

# Read it back
with open(llm_output_file, "r", encoding="utf-8") as f:
    content = f.read()

print("[Content read back]:")
print(content)

print("✅ Always use encoding='utf-8' when writing LLM outputs, YAML, or any")
print("   content that may contain non-ASCII characters.")
print("   Without it, Python uses the system's default encoding — which")
print("   may differ between your laptop, CI server, and production container.")


# ─────────────────────────────────────────────────────────────────────────────
# PART 6: flush() — Force buffer to disk immediately
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 6: flush() — Force write to disk without closing")
print("=" * 60)

progress_log = demo_path("migration_progress.log")

# Simulating a long-running database migration that logs progress
steps = [
    "Starting migration: 10,000 records",
    "Progress: 2,500 records migrated (25%)",
    "Progress: 5,000 records migrated (50%)",
    "Progress: 7,500 records migrated (75%)",
    "Migration complete: 10,000 records migrated (100%)",
]

with open(progress_log, "w") as f:
    for step in steps:
        f.write(f"[{utcnow()}] {step}\n")
        f.flush()  # ← Force Python to write buffer to OS immediately
        # Without flush(), progress may sit in Python's internal buffer
        # and not appear in the file if the process crashes mid-migration

print(f"[OK] Migration log with flush() written: {len(steps)} steps")
print("     Each line was flushed to disk immediately after writing.")
print("     If the process had crashed at step 3, steps 1-3 would still be on disk.")

with open(progress_log, "r") as f:
    for line in f:
        print(f"  {line.strip()}")

import shutil
shutil.rmtree(DEMO_DIR)
print(f"\n[Cleanup] Removed demo directory.")
print("[Done] Demo 04 complete.")
