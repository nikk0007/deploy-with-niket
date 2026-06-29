# ============================================================
# 10_best_practices.py
# Topic: 5 Best Practices — What Separates Professional Code
# ============================================================

# ============================================================
# RULE 1 — One function, one job
# ============================================================
# If your function name has "and" in it — it is doing two jobs. Split it.

# Bad — does three things at once
def validate_and_deploy_and_notify(service, config):
    # validation logic...
    # deployment logic...
    # notification logic...
    pass

# Good — three focused functions, each doing one job
def validate_deployment_config(service, config):
    """Returns True if the deployment config passes all checks."""
    required_keys = ["image_tag", "replicas", "health_probe_path"]
    return all(key in config for key in required_keys)

def deploy_service(service, config):
    """Triggers the deployment for a validated config."""
    print(f"Deploying {service} with image {config['image_tag']} — {config['replicas']} replica(s)")

def notify_deployment(service, status, channel="#deployments"):
    """Sends a deployment status notification to Slack."""
    print(f"[Slack → {channel}] {service} deployment: {status.upper()}")

# Orchestrate them in sequence — clean and readable
service = "payment-service"
config  = {"image_tag": "v2.1.4", "replicas": 3, "health_probe_path": "/healthz"}

if validate_deployment_config(service, config):
    deploy_service(service, config)
    notify_deployment(service, "success")
else:
    notify_deployment(service, "failed — invalid config")

print()

# ============================================================
# RULE 2 — Name should tell you what it does
# ============================================================

# Bad names — you have to read the body to understand what it does
def proc(x, flag):
    pass

def check(v):
    pass

# Good names — the name tells the whole story
def calculate_monthly_ec2_cost(instance_type, hours_running, hourly_rate):
    return round(hours_running * hourly_rate, 2)

def is_pod_in_crashloop(restart_count, threshold=5):
    return restart_count >= threshold

def rotate_iam_access_key(username, region="ap-south-1"):
    print(f"Rotating IAM key for {username} in {region}...")

print("=== Rule 2: Descriptive names ===")
cost = calculate_monthly_ec2_cost("t3.medium", 720, 8.50)
print(f"Monthly EC2 cost: Rs.{cost}")
print(f"Pod in crashloop: {is_pod_in_crashloop(7)}")
print()

# ============================================================
# RULE 3 — Keep functions short
# ============================================================
# A function longer than 20-25 lines is usually doing more than one job.
# If you cannot see the whole function on one screen — it needs splitting.

print("=== Rule 3: Keep functions short — split when needed ===")

def get_instance_metadata(instance_id):
    """Step 1: Fetch instance data."""
    return {"id": instance_id, "type": "t3.medium", "region": "ap-south-1", "state": "running"}

def format_cost_report_line(metadata, cost):
    """Step 2: Format a single cost report line."""
    return f"{metadata['id']} | {metadata['type']} | {metadata['region']} | Rs.{cost}"

def generate_cost_report(instance_ids):
    """Step 3: Orchestrate — calls the two focused functions above."""
    print("Monthly EC2 Cost Report")
    print("-" * 55)
    for iid in instance_ids:
        meta = get_instance_metadata(iid)
        cost = calculate_monthly_ec2_cost(meta["type"], 720, 8.50)
        print(format_cost_report_line(meta, cost))

generate_cost_report(["i-0abc001", "i-0abc002", "i-0abc003"])
print()

# ============================================================
# RULE 4 — Write docstrings
# ============================================================
# A docstring lives inside the function and explains what it does,
# what its parameters mean, and what it returns.
# It is read by your team, IDEs, and documentation generators.

def calculate_emi(principal, annual_rate, months):
    """
    Calculate the monthly EMI for a loan.

    principal   : Loan amount in Rs.
    annual_rate : Annual interest rate as a percentage (e.g. 8.5 for 8.5%)
    months      : Repayment tenure in months
    Returns     : Monthly EMI amount rounded to 2 decimal places.

    Formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    where r = monthly interest rate, n = number of months
    """
    monthly_rate = annual_rate / (12 * 100)
    emi = principal * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
    return round(emi, 2)

print("=== Rule 4: Docstrings ===")
emi = calculate_emi(500000, 8.5, 60)
print(f"Loan EMI for Rs.5,00,000 at 8.5% over 60 months: Rs.{emi}/month")
print()

# ============================================================
# RULE 5 — Avoid side effects; depend only on inputs
# ============================================================
# A "pure" function:
#   - depends only on its parameters
#   - returns a result
#   - does not silently modify global state or external systems
#
# Side effects are fine (writing logs, sending alerts) — but they
# should be explicit, named clearly, and isolated to dedicated functions.

# Bad — silently modifies a global list as a hidden side effect
all_alerts = []

def check_cpu_bad(instance_id, cpu_usage):
    if cpu_usage > 90:
        all_alerts.append(f"HIGH CPU on {instance_id}")   # hidden side effect

# Good — pure check function + explicit action function, separated
def is_cpu_critical(cpu_usage, threshold=90):
    """Pure function — no side effects. Always returns the same result for the same inputs."""
    return cpu_usage > threshold

def trigger_cpu_alert(instance_id, cpu_usage):
    """Explicit side effect — name makes clear this does something external."""
    print(f"[ALERT] High CPU on {instance_id}: {cpu_usage}% — paging on-call team")

print("=== Rule 5: Avoid hidden side effects ===")
instances = [("i-001", 45), ("i-002", 95), ("i-003", 78), ("i-004", 92)]
for iid, cpu in instances:
    if is_cpu_critical(cpu):
        trigger_cpu_alert(iid, cpu)

print()
print("=" * 55)
print("The mindset shift:")
print("  Typing same logic twice?     → Write a function.")
print("  Function over 25 lines?      → Split it.")
print("  Function name unclear?       → Rename it. If you cannot name it,")
print("                                  the function's job is not clear yet.")
print("=" * 55)
