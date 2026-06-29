# ============================================================
# 06_first_class_functions.py
# Topic: Functions as First-Class Objects
# ============================================================

# In Python, a function is an object — just like a string or integer.
# That means you can:
#   1. Store a function in a variable
#   2. Pass a function as an argument to another function
#   3. Return a function from a function
#
# This unlocks patterns used in every serious production codebase.

# ---- 1. Storing a function in a variable ----

def validate_aws_instance_id(instance_id):
    """Instance IDs start with 'i-' followed by 8 or 17 hex characters."""
    if not instance_id.startswith("i-"):
        return False
    suffix = instance_id[2:]
    return len(suffix) in (8, 17) and all(c in "0123456789abcdef" for c in suffix)

# Store the function in a variable — no parentheses (that would call it)
checker = validate_aws_instance_id

print("=== Storing a function in a variable ===")
print(checker("i-0abc12345678"))     # True
print(checker("i-0abc1234"))         # False
print(checker("ec2-instance-001"))   # False
print()

# ---- 2. Passing a function as an argument ----
# This is the most commonly used pattern in real production code.

def run_pre_deployment_check(resource_id, validation_fn):
    """
    Generic pre-deployment gate.
    Accepts any validation function — the logic is pluggable.
    """
    if validation_fn(resource_id):
        print(f"  [{resource_id}] Validation passed. Deployment approved.")
    else:
        print(f"  [{resource_id}] Validation FAILED. Deployment blocked.")

def validate_ecr_image_tag(tag):
    """ECR image tags must not be 'latest' in production."""
    return tag != "latest" and len(tag) > 0

def validate_s3_bucket_name(name):
    """S3 bucket names must be 3-63 chars, lowercase, no underscores."""
    return 3 <= len(name) <= 63 and name.islower() and "_" not in name

print("=== Passing functions as arguments ===")

# Same run_pre_deployment_check function — different validators plugged in
run_pre_deployment_check("i-0abc1234567890abc", validate_aws_instance_id)
run_pre_deployment_check("latest",              validate_ecr_image_tag)
run_pre_deployment_check("v1.4.2-stable",       validate_ecr_image_tag)
run_pre_deployment_check("my_prod_bucket",      validate_s3_bucket_name)
run_pre_deployment_check("my-prod-bucket",      validate_s3_bucket_name)

print()

# ---- 3. A list of functions — running a full validation pipeline ----
# This pattern powers middleware chains, CI/CD gate pipelines, and plugin systems.

def check_replicas(config):
    return config.get("replicas", 0) >= 2

def check_health_probe(config):
    return "health_probe_path" in config

def check_resource_limits(config):
    return "cpu_limit" in config and "memory_limit" in config

def check_image_tag(config):
    return config.get("image_tag", "latest") != "latest"

print("=== Running a validation pipeline ===\n")

deployment_config = {
    "service": "payment-service",
    "replicas": 3,
    "health_probe_path": "/healthz",
    "cpu_limit": "500m",
    "memory_limit": "512Mi",
    "image_tag": "v2.1.4",
}

validation_pipeline = [
    ("Replica count >= 2",     check_replicas),
    ("Health probe defined",   check_health_probe),
    ("Resource limits set",    check_resource_limits),
    ("No 'latest' image tag",  check_image_tag),
]

all_passed = True
for check_name, check_fn in validation_pipeline:
    passed = check_fn(deployment_config)
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] {check_name}")
    if not passed:
        all_passed = False

print()
if all_passed:
    print("All checks passed. Deployment approved.")
else:
    print("One or more checks failed. Deployment blocked.")

print("""
This pattern is everywhere in production:
  - Web frameworks    → middleware chains
  - Data pipelines    → transformation steps
  - CI/CD systems     → gate checks before promotion
  - Testing frameworks → fixture and hook injection
""")
