"""
DEMO 06: Complete Real-World Pipeline — JSON, YAML, CSV with File Handling
Topic: File Handling in Python
Use Case: DevOps/GenAI — End-to-end pipeline that reads a Kubernetes YAML
          manifest, checks it against a policy JSON, generates a CSV report,
          and appends to an audit log.

This demo ties together everything from the series:
  ✅ File modes (r, w, a)
  ✅ with statement
  ✅ Reading with for loop and read()
  ✅ Writing and appending
  ✅ pathlib for all paths
  ✅ JSON, YAML, CSV libraries
  ✅ Exception handling in file operations
  ✅ encoding="utf-8" everywhere
"""

import json
import csv
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# Try importing yaml — install with: pip install pyyaml
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False
    print("⚠️  pyyaml not installed. YAML demo will use raw text parsing.")
    print("    Install with: pip install pyyaml\n")


# ─────────────────────────────────────────────────────────────────────────────
# Setup: Simulated project workspace
# ─────────────────────────────────────────────────────────────────────────────

WORKSPACE = Path(tempfile.mkdtemp(prefix="python_fh_demo06_"))
(WORKSPACE / "manifests").mkdir()
(WORKSPACE / "policies").mkdir()
(WORKSPACE / "reports").mkdir()
(WORKSPACE / "logs").mkdir()


def utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: Write sample Kubernetes manifests (simulating what a developer provides)
# ─────────────────────────────────────────────────────────────────────────────

manifests = {
    "api-server.yaml": {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "api-server", "namespace": "production"},
        "spec": {
            "replicas": 5,
            "template": {
                "spec": {
                    "containers": [{
                        "name": "api-server",
                        "image": "myorg/api-server:v2.4.1",
                        "resources": {
                            "requests": {"memory": "256Mi", "cpu": "250m"},
                            "limits":   {"memory": "512Mi", "cpu": "500m"}
                        }
                    }]
                }
            }
        }
    },
    "worker.yaml": {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "ml-worker", "namespace": "production"},
        "spec": {
            "replicas": 12,  # Over-replicated — policy violation
            "template": {
                "spec": {
                    "containers": [{
                        "name": "ml-worker",
                        "image": "myorg/ml-worker:latest",  # 'latest' tag — policy violation
                        "resources": {
                            "requests": {"memory": "512Mi", "cpu": "500m"},
                            # No limits defined — policy violation
                        }
                    }]
                }
            }
        }
    },
    "redis.yaml": {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "redis-cache", "namespace": "production"},
        "spec": {
            "replicas": 1,
            "template": {
                "spec": {
                    "containers": [{
                        "name": "redis",
                        "image": "redis:7.2.3",
                        "resources": {
                            "requests": {"memory": "128Mi", "cpu": "100m"},
                            "limits":   {"memory": "256Mi", "cpu": "200m"}
                        }
                    }]
                }
            }
        }
    }
}

print("=" * 60)
print("STEP 1: Writing Kubernetes manifests")
print("=" * 60)

for filename, manifest_data in manifests.items():
    manifest_path = WORKSPACE / "manifests" / filename
    with open(manifest_path, "w", encoding="utf-8") as f:
        if YAML_AVAILABLE:
            yaml.dump(manifest_data, f, default_flow_style=False)
        else:
            # Fallback: write as JSON (for demo purposes)
            json.dump(manifest_data, f, indent=2)
    print(f"  [Written] {filename}")


# ─────────────────────────────────────────────────────────────────────────────
# STEP 2: Write deployment policy (JSON)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("STEP 2: Writing deployment policy (JSON)")
print("=" * 60)

policy = {
    "policy_version": "1.3",
    "description": "Production deployment policy for all services",
    "rules": {
        "max_replicas": 10,
        "forbidden_image_tags": ["latest", "dev", "test", "unstable"],
        "require_resource_limits": True,
        "require_namespace": "production"
    }
}

policy_path = WORKSPACE / "policies" / "deployment_policy.json"
with open(policy_path, "w", encoding="utf-8") as f:
    json.dump(policy, f, indent=2)
print(f"  [Written] {policy_path.name}")


# ─────────────────────────────────────────────────────────────────────────────
# STEP 3: Policy checker — reads manifests + policy, produces violations list
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("STEP 3: Running policy checks on all manifests")
print("=" * 60)


def load_policy(policy_file: Path) -> dict:
    with open(policy_file, "r", encoding="utf-8") as f:
        return json.load(f)


def load_manifest(manifest_file: Path) -> dict:
    with open(manifest_file, "r", encoding="utf-8") as f:
        if YAML_AVAILABLE:
            return yaml.safe_load(f)
        else:
            return json.load(f)


def check_manifest(manifest: dict, policy: dict) -> list:
    """Returns a list of policy violations found in the manifest."""
    violations = []
    rules = policy["rules"]

    name = manifest.get("metadata", {}).get("name", "unknown")
    spec = manifest.get("spec", {})
    containers = spec.get("template", {}).get("spec", {}).get("containers", [])

    # Check 1: Replica count
    replicas = spec.get("replicas", 1)
    if replicas > rules["max_replicas"]:
        violations.append({
            "check": "max_replicas",
            "detail": f"replicas={replicas} exceeds max={rules['max_replicas']}"
        })

    # Check 2: Namespace
    namespace = manifest.get("metadata", {}).get("namespace", "")
    if namespace != rules["require_namespace"]:
        violations.append({
            "check": "namespace",
            "detail": f"namespace='{namespace}', required='{rules['require_namespace']}'"
        })

    # Container-level checks
    for container in containers:
        image = container.get("image", "")
        image_tag = image.split(":")[-1] if ":" in image else "latest"

        # Check 3: Forbidden image tags
        if image_tag in rules["forbidden_image_tags"]:
            violations.append({
                "check": "forbidden_image_tag",
                "detail": f"image='{image}' uses forbidden tag='{image_tag}'"
            })

        # Check 4: Resource limits
        if rules["require_resource_limits"]:
            limits = container.get("resources", {}).get("limits")
            if not limits:
                violations.append({
                    "check": "missing_resource_limits",
                    "detail": f"container='{container.get('name')}' has no resource limits defined"
                })

    return violations


# Load policy once
policy_data = load_policy(policy_path)
manifests_dir = WORKSPACE / "manifests"
all_results = []

for manifest_file in sorted(manifests_dir.glob("*.yaml" if YAML_AVAILABLE else "*.json")):
    try:
        manifest_data = load_manifest(manifest_file)
        violations = check_manifest(manifest_data, policy_data)
        service_name = manifest_data.get("metadata", {}).get("name", manifest_file.stem)

        result = {
            "manifest": manifest_file.name,
            "service": service_name,
            "status": "PASS" if not violations else "FAIL",
            "violation_count": len(violations),
            "violations": violations,
            "checked_at": utcnow()
        }
        all_results.append(result)

        status_icon = "✅" if not violations else "❌"
        print(f"  {status_icon} {service_name}: {result['status']} ({len(violations)} violations)")
        for v in violations:
            print(f"       → [{v['check']}] {v['detail']}")

    except Exception as e:
        print(f"  ⚠️  Error processing {manifest_file.name}: {e}")


# ─────────────────────────────────────────────────────────────────────────────
# STEP 4: Write a JSON summary report (fresh on each run → "w" mode)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("STEP 4: Writing JSON summary report (fresh each run)")
print("=" * 60)

summary = {
    "scan_timestamp": utcnow(),
    "policy_version": policy_data["policy_version"],
    "total_manifests": len(all_results),
    "passed": sum(1 for r in all_results if r["status"] == "PASS"),
    "failed": sum(1 for r in all_results if r["status"] == "FAIL"),
    "results": all_results
}

report_json = WORKSPACE / "reports" / "policy_scan_summary.json"
with open(report_json, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)
print(f"  [Written] {report_json.name}")
print(f"  Passed: {summary['passed']} | Failed: {summary['failed']}")


# ─────────────────────────────────────────────────────────────────────────────
# STEP 5: Write a CSV report for the team (easy to open in Excel/Sheets)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("STEP 5: Writing CSV report for team review")
print("=" * 60)

report_csv = WORKSPACE / "reports" / "policy_violations.csv"

with open(report_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["service", "status", "violation_count", "check", "detail", "checked_at"])
    writer.writeheader()

    for result in all_results:
        if result["violations"]:
            for v in result["violations"]:
                writer.writerow({
                    "service": result["service"],
                    "status": result["status"],
                    "violation_count": result["violation_count"],
                    "check": v["check"],
                    "detail": v["detail"],
                    "checked_at": result["checked_at"]
                })
        else:
            writer.writerow({
                "service": result["service"],
                "status": result["status"],
                "violation_count": 0,
                "check": "NONE",
                "detail": "All checks passed",
                "checked_at": result["checked_at"]
            })

print(f"  [Written] {report_csv.name}")

# Show CSV content
with open(report_csv, "r") as f:
    print("\n  CSV content:")
    for line in f:
        print(f"    {line.strip()}")


# ─────────────────────────────────────────────────────────────────────────────
# STEP 6: Append to audit log (never overwrite → "a" mode)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("STEP 6: Appending pipeline run to audit log")
print("=" * 60)

audit_log = WORKSPACE / "logs" / "pipeline_audit.log"

total = summary["total_manifests"]
passed = summary["passed"]
failed = summary["failed"]

audit_entry = (
    f"[{utcnow()}] policy_scan "
    f"| policy_version={policy_data['policy_version']} "
    f"| manifests={total} passed={passed} failed={failed} "
    f"| report={report_json.name}\n"
)

with open(audit_log, "a", encoding="utf-8") as f:
    f.write(audit_entry)

print(f"  [Appended] Entry written to {audit_log.name}")
print(f"  Content: {audit_entry.strip()}")


# ─────────────────────────────────────────────────────────────────────────────
# FINAL: Show workspace output
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("PIPELINE COMPLETE — Files generated:")
print("=" * 60)

for f in sorted(WORKSPACE.rglob("*")):
    if f.is_file():
        rel = f.relative_to(WORKSPACE)
        size = f.stat().st_size
        print(f"  📄 {rel}  ({size} bytes)")

import shutil
shutil.rmtree(WORKSPACE)
print(f"\n[Cleanup] Removed demo workspace.")
print("[Done] Demo 06 complete.")
