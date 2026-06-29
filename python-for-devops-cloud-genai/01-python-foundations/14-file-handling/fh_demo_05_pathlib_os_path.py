"""
DEMO 05: File Paths — os.path vs pathlib
Topic: File Handling in Python
Use Case: DevOps/Cloud — Writing portable scripts that work on any machine,
          container, or CI/CD runner

Demonstrates:
  - The hardcoded path anti-pattern
  - os.path: classic approach
  - pathlib.Path: modern, recommended approach
  - Checking existence, creating directories
  - Globbing (finding files by pattern)
  - pathlib shortcut methods: read_text(), write_text(), glob()
"""

import os
import tempfile
from pathlib import Path

DEMO_DIR = tempfile.mkdtemp(prefix="python_fh_demo05_")
print(f"Demo root: {DEMO_DIR}\n")


# ─────────────────────────────────────────────────────────────────────────────
# Setup: Simulate a DevOps project directory structure
# ─────────────────────────────────────────────────────────────────────────────

# Create a simulated project directory structure
project_root = Path(DEMO_DIR) / "infra-automation"
(project_root / "configs").mkdir(parents=True)
(project_root / "logs").mkdir(parents=True)
(project_root / "manifests" / "production").mkdir(parents=True)
(project_root / "manifests" / "staging").mkdir(parents=True)
(project_root / "reports").mkdir(parents=True)

# Create sample files
(project_root / "configs" / "backend.conf").write_text(
    'bucket = "terraform-state-prod"\nregion = "ap-south-1"\n'
)
(project_root / "configs" / "variables.tfvars").write_text(
    'environment = "production"\nreplicas = 3\n'
)
(project_root / "manifests" / "production" / "api-deployment.yaml").write_text(
    "kind: Deployment\nmetadata:\n  name: api-server\n"
)
(project_root / "manifests" / "production" / "redis-deployment.yaml").write_text(
    "kind: Deployment\nmetadata:\n  name: redis-cache\n"
)
(project_root / "manifests" / "staging" / "api-deployment.yaml").write_text(
    "kind: Deployment\nmetadata:\n  name: api-server\n"
)

print("Simulated project structure created:")
for item in sorted(project_root.rglob("*")):
    depth = len(item.relative_to(project_root).parts) - 1
    prefix = "  " * depth + ("📁 " if item.is_dir() else "📄 ")
    print(f"  {prefix}{item.name}")
print()


# ─────────────────────────────────────────────────────────────────────────────
# ANTI-PATTERN: Hardcoded absolute paths
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("ANTI-PATTERN: Hardcoded Absolute Paths")
print("=" * 60)

print("# Example of what NOT to do:")
print('  config = open("/home/ubuntu/infra-automation/configs/backend.conf")')
print()
print("Why this breaks:")
print("  ❌ On another machine → different home directory → FileNotFoundError")
print("  ❌ In a Docker container → /home/ubuntu doesn't exist")
print("  ❌ On a CI/CD runner → runner uses /home/runner or /workspace")
print("  ❌ On macOS dev machine → path is /Users/yourname/...")
print()


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 1: os.path — Classic approach
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("APPROACH 1: os.path — Classic (still valid, widely used)")
print("=" * 60)

# Simulate __file__ being inside the project root
script_location = str(project_root / "main.py")  # pretend this is our script

base_dir = os.path.dirname(os.path.abspath(script_location))
config_dir = os.path.join(base_dir, "configs")
backend_conf = os.path.join(config_dir, "backend.conf")
log_dir = os.path.join(base_dir, "logs")
deploy_log = os.path.join(log_dir, "deploy.log")

print(f"base_dir     : {os.path.relpath(base_dir, DEMO_DIR)}")
print(f"config_dir   : {os.path.relpath(config_dir, DEMO_DIR)}")
print(f"backend_conf : {os.path.relpath(backend_conf, DEMO_DIR)}")
print()

# Check existence
if os.path.exists(backend_conf):
    print(f"[OK] Config file exists: {os.path.basename(backend_conf)}")
else:
    print(f"[MISSING] Config file not found.")

# Create log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)
print(f"[OK] Log directory ready: {os.path.relpath(log_dir, DEMO_DIR)}")

# Write using joined path
with open(deploy_log, "w") as f:
    f.write("Deployment started via os.path approach\n")
print(f"[OK] Deploy log written: {os.path.basename(deploy_log)}")

# Common os.path utilities
print()
print("[os.path utilities]")
print(f"  os.path.basename : {os.path.basename(backend_conf)}")
print(f"  os.path.dirname  : {os.path.relpath(os.path.dirname(backend_conf), DEMO_DIR)}")
print(f"  os.path.exists   : {os.path.exists(backend_conf)}")
print(f"  os.path.isfile   : {os.path.isfile(backend_conf)}")
print(f"  os.path.isdir    : {os.path.isdir(config_dir)}")
print(f"  os.path.getsize  : {os.path.getsize(backend_conf)} bytes")


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 2: pathlib — Modern, recommended approach
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("APPROACH 2: pathlib.Path — Modern (recommended for all new code)")
print("=" * 60)

# Simulate __file__ inside the project root
base = project_root

config_path = base / "configs" / "backend.conf"
log_path = base / "logs" / "pipeline.log"
reports_dir = base / "reports"

print(f"base         : {base.relative_to(DEMO_DIR)}")
print(f"config_path  : {config_path.relative_to(DEMO_DIR)}")
print(f"log_path     : {log_path.relative_to(DEMO_DIR)}")
print()

# Check existence and read in one line
if config_path.exists():
    content = config_path.read_text(encoding="utf-8")
    print(f"[OK] Config loaded ({len(content)} chars):")
    for line in content.splitlines():
        print(f"       {line}")

# Write in one line — no need for open/close
log_path.write_text("Pipeline started via pathlib approach\n", encoding="utf-8")
print(f"\n[OK] Log written: {log_path.name}")

# Create directories safely
reports_dir.mkdir(parents=True, exist_ok=True)
print(f"[OK] Reports dir ready: {reports_dir.relative_to(DEMO_DIR)}")

# Path properties
print()
print("[pathlib.Path properties]")
print(f"  .name      : {config_path.name}")
print(f"  .stem      : {config_path.stem}")
print(f"  .suffix    : {config_path.suffix}")
print(f"  .parent    : {config_path.parent.relative_to(DEMO_DIR)}")
print(f"  .exists()  : {config_path.exists()}")
print(f"  .is_file() : {config_path.is_file()}")
print(f"  .is_dir()  : {config_path.is_dir()}")
print(f"  .stat().st_size : {config_path.stat().st_size} bytes")


# ─────────────────────────────────────────────────────────────────────────────
# GLOB — Finding files by pattern (very useful in DevOps scripts)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("GLOB — Finding Files by Pattern (pathlib)")
print("Use case: Process all Kubernetes manifests in a directory")
print("=" * 60)

manifests_dir = base / "manifests"

# Find all YAML files in all subdirectories
yaml_files = list(manifests_dir.rglob("*.yaml"))

print(f"[Found {len(yaml_files)} YAML manifests under manifests/]")
for yaml_file in sorted(yaml_files):
    print(f"  → {yaml_file.relative_to(base)}")

# Process only production manifests
print()
print("[Processing production manifests only]")
prod_manifests = list((manifests_dir / "production").glob("*.yaml"))
for manifest in sorted(prod_manifests):
    content = manifest.read_text()
    kind = "Unknown"
    name = "Unknown"
    for line in content.splitlines():
        if line.startswith("kind:"):
            kind = line.split(":")[1].strip()
        if "name:" in line:
            name = line.split(":")[1].strip()
    print(f"  {manifest.name}: kind={kind}, name={name}")


# ─────────────────────────────────────────────────────────────────────────────
# Comparison table
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("os.path vs pathlib — Quick Comparison")
print("=" * 60)
print()
print("Task                         | os.path                    | pathlib")
print("-" * 75)
print("Build path                   | os.path.join(a, b, c)     | a / b / c")
print("Get filename                 | os.path.basename(p)       | p.name")
print("Get directory                | os.path.dirname(p)        | p.parent")
print("Check exists                 | os.path.exists(p)         | p.exists()")
print("Check is file                | os.path.isfile(p)         | p.is_file()")
print("Create dirs                  | os.makedirs(p, exist_ok)  | p.mkdir(parents=True)")
print("Read text file               | open(p).read()            | p.read_text()")
print("Write text file              | open(p,'w').write(s)      | p.write_text(s)")
print("Find files by pattern        | glob.glob(pattern)        | p.glob('*.yaml')")
print("Find files recursively       | os.walk(...)              | p.rglob('*.yaml')")
print()
print("✅ Recommendation: Use pathlib for all new Python scripts.")
print("   os.path is still valid — you will encounter it in older codebases.")

import shutil
shutil.rmtree(DEMO_DIR)
print(f"\n[Cleanup] Removed demo directory.")
print("[Done] Demo 05 complete.")
