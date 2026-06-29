"""
DEMO 01: File Modes
Topic: File Handling in Python
Use Case: DevOps/Cloud — Understanding what each file mode does

Run this to see:
  - "r"  → read only (file must exist)
  - "w"  → write (OVERWRITES existing content — dangerous for logs!)
  - "a"  → append (adds to end, never overwrites)
  - "x"  → exclusive create (fails if file exists — safe for lock files)
  - Mode errors and how to handle them
"""

import os
import tempfile

# Use a temp directory so demo files are auto-cleaned up
DEMO_DIR = tempfile.mkdtemp(prefix="python_filehandling_demo_")
print(f"Demo files will be created in: {DEMO_DIR}\n")


def demo_path(filename):
    return os.path.join(DEMO_DIR, filename)


# ─────────────────────────────────────────────────────────────────────────────
# MODE "w" — Write (creates OR overwrites)
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print('MODE "w" — Write (creates file; OVERWRITES if it exists)')
print("=" * 60)

log_file = demo_path("deployment.log")

# First write
with open(log_file, "w") as f:
    f.write("Deployment #1: prod-cluster — SUCCESS\n")
print(f"[Run 1] Wrote first entry.")

# Second write — THIS ERASES the first entry!
with open(log_file, "w") as f:
    f.write("Deployment #2: prod-cluster — SUCCESS\n")
print(f"[Run 2] Wrote second entry with mode 'w'.")

with open(log_file, "r") as f:
    content = f.read()

print(f"[Result] File content after two 'w' writes:")
print(content)
print("⚠️  Only Run 2 is visible. Run 1 was SILENTLY ERASED.")


# ─────────────────────────────────────────────────────────────────────────────
# MODE "a" — Append (creates OR adds to end — correct for logs)
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print('MODE "a" — Append (never overwrites — correct for logs)')
print("=" * 60)

audit_file = demo_path("audit_trail.log")

# Three separate append operations — simulating three separate script runs
for i in range(1, 4):
    with open(audit_file, "a") as f:
        f.write(f"[Run {i}] Terraform apply on workspace=production — OK\n")

with open(audit_file, "r") as f:
    content = f.read()

print("[Result] File content after three 'a' writes:")
print(content)
print("✅ All three entries preserved. This is correct for audit logs.")


# ─────────────────────────────────────────────────────────────────────────────
# MODE "r" — Read only (file must exist)
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print('MODE "r" — Read only (fails if file does not exist)')
print("=" * 60)

# Reading a file that exists
with open(audit_file, "r") as f:
    lines = f.readlines()
print(f"[OK] Successfully read {len(lines)} lines from audit_trail.log")

# Trying to read a file that does NOT exist
nonexistent = demo_path("kubeconfig.yaml")
try:
    with open(nonexistent, "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"[FileNotFoundError] {e}")
    print("    Action: Check if kubectl is configured and kubeconfig is present.")


# ─────────────────────────────────────────────────────────────────────────────
# MODE "x" — Exclusive create (fails if file already exists)
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print('MODE "x" — Exclusive create (safe for distributed lock files)')
print("=" * 60)

lock_file = demo_path("pipeline.lock")

# First process acquires the lock
try:
    with open(lock_file, "x") as f:
        f.write("PID=12345 | pipeline=prod-deploy | acquired=2024-01-15T03:00:00Z\n")
    print("[Process 1] Lock acquired. Created pipeline.lock")
except FileExistsError:
    print("[Process 1] Lock already held by another process. Skipping run.")

# Second process (or second run) tries to acquire the same lock
try:
    with open(lock_file, "x") as f:
        f.write("PID=99999 | pipeline=prod-deploy | acquired=2024-01-15T03:00:01Z\n")
    print("[Process 2] Lock acquired.")
except FileExistsError:
    print("[Process 2] FileExistsError: Lock already held. Will not proceed.")
    print("    ✅ This is correct behaviour — prevents concurrent deployments.")

# Cleanup lock file
os.remove(lock_file)
print("[Cleanup] Lock file removed.")


# ─────────────────────────────────────────────────────────────────────────────
# Summary comparison
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("SUMMARY: Which mode for which use case?")
print("=" * 60)
print('"r"  → Reading Kubernetes manifests, Terraform configs, kubeconfig')
print('"w"  → Writing fresh reports: scan results, cost summaries, generated configs')
print('"a"  → Writing logs, audit trails, deployment histories — NEVER use "w" here')
print('"x"  → Creating lock files, ensuring single-writer in distributed pipelines')
print('"rb" → Reading binary: Docker image layers, compressed artifacts, PDFs')

# Cleanup
import shutil
shutil.rmtree(DEMO_DIR)
print(f"\n[Cleanup] Removed demo directory: {DEMO_DIR}")
print("[Done] Demo 01 complete.")
