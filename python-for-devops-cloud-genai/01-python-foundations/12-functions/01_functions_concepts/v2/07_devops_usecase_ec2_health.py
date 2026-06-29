# ============================================================
# 07_devops_usecase_ec2_health.py
# Topic: Real DevOps Use Case — EC2 Health Checker
# ============================================================

# In production you may have dozens or hundreds of EC2 instances.
# Writing health check logic inline every time is unmaintainable.
# One function — call it anywhere: monitoring scripts, Lambda, CI/CD pipelines.
#
# NOTE: This file simulates AWS API responses so it runs without credentials.
#       In production, replace the simulated data with real boto3 calls (shown in comments).

# ---- Simulated AWS response data (replace with boto3 in production) ----

SIMULATED_INSTANCES = {
    "i-0abc123def001": {"state": "running",  "system_status": "ok",       "region": "ap-south-1"},
    "i-0abc123def002": {"state": "running",  "system_status": "impaired", "region": "ap-south-1"},
    "i-0abc123def003": {"state": "stopped",  "system_status": "ok",       "region": "us-east-1"},
    "i-0abc123def004": {"state": "running",  "system_status": "ok",       "region": "eu-west-1"},
}

# ---- The reusable health check function ----

def check_ec2_health(instance_id, region="ap-south-1"):
    """
    Check the health status of a single EC2 instance.

    instance_id : AWS EC2 instance ID (e.g. 'i-0abc123def001')
    region      : AWS region name (default: ap-south-1)
    Returns a dict with instance_id, state, system_status, and health_summary.

    In production, replace the simulated lookup below with:
        import boto3
        ec2 = boto3.client("ec2", region_name=region)
        response = ec2.describe_instance_status(InstanceIds=[instance_id])
        statuses = response["InstanceStatuses"]
    """
    # --- Simulated API call ---
    instance = SIMULATED_INSTANCES.get(instance_id)
    if not instance:
        return {
            "instance_id":    instance_id,
            "state":          "unknown",
            "system_status":  "unknown",
            "health_summary": "Instance not found or stopped",
        }

    state         = instance["state"]
    system_status = instance["system_status"]

    if state != "running":
        health_summary = f"Instance is {state} — no active health data"
    elif system_status == "ok":
        health_summary = "Healthy"
    else:
        health_summary = f"System check FAILED: {system_status}"

    return {
        "instance_id":    instance_id,
        "state":          state,
        "system_status":  system_status,
        "health_summary": health_summary,
    }


def print_health_report(result):
    """Pretty-print a single health check result."""
    print(f"  Instance  : {result['instance_id']}")
    print(f"  State     : {result['state']}")
    print(f"  System    : {result['system_status']}")
    print(f"  Summary   : {result['health_summary']}")
    print()


# ---- Single instance check ----
print("=== Single Instance Check ===\n")
result = check_ec2_health("i-0abc123def001")
print_health_report(result)

# ---- Batch check across a fleet ----
print("=== Fleet-Wide Health Sweep ===\n")

instance_fleet = [
    ("i-0abc123def001", "ap-south-1"),
    ("i-0abc123def002", "ap-south-1"),
    ("i-0abc123def003", "us-east-1"),
    ("i-0abc123def004", "eu-west-1"),
]

critical_instances = []

for instance_id, region in instance_fleet:
    result = check_ec2_health(instance_id, region)
    print_health_report(result)
    if result["health_summary"] != "Healthy":
        critical_instances.append(instance_id)

# ---- Summary ----
print("=" * 45)
if critical_instances:
    print(f"ACTION REQUIRED: {len(critical_instances)} instance(s) need attention:")
    for iid in critical_instances:
        print(f"  - {iid}")
else:
    print("All instances healthy. No action required.")
