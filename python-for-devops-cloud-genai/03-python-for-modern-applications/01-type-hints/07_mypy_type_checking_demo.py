# ============================================================
# FILE 07 — mypy Demo: Catching Errors Before Runtime
# Video Section: "Type Checking Tools"
# ============================================================
#
# HOW TO RUN THIS FILE WITH mypy:
# Step 1: pip install mypy
# Step 2: mypy 07_mypy_demo.py
#
# mypy will flag all the intentional type errors below.
# Python itself will NOT flag them.
# ============================================================


# ---- CORRECT USAGE ----

def calculate_discount(price: float, percent: float) -> float:
    return price - (price * percent / 100)

discount_price = calculate_discount(2000.0, 10.0)
print(discount_price)   # 1800.0   ← mypy: OK


# ---- INTENTIONAL ERRORS FOR mypy TO CATCH ----

# Error 1: Wrong argument type
bad_result = calculate_discount("two thousand", 10.0)
# mypy: error — Argument 1 to "calculate_discount" has incompatible type "str"; expected "float"
# Python: Will raise TypeError when it tries to do string math


# Error 2: Wrong return type used
def get_active_users() -> int:
    return "forty two"          # Wrong return type
    # mypy: error — Incompatible return value type (got "str", expected "int")


# Error 3: Type mismatch in variable assignment
user_count: int = "one hundred"
# mypy: error — Incompatible types in assignment (expression has type "str", variable has type "int")


# Error 4: None not handled
def find_order(order_id: int) -> str | None:
    orders = {1: "Laptop", 2: "Phone"}
    return orders.get(order_id)

order = find_order(99)           # Returns None
upper_order = order.upper()      # mypy: error — Item "None" of "str | None" has no attribute "upper"
# Python: Will crash with AttributeError at runtime


# ---- HOW TO FIX THAT NONE ERROR ----

order_safe = find_order(99)
if order_safe is not None:
    print(order_safe.upper())    # mypy: OK — None is handled
else:
    print("Order not found")


# ---- CORRECT FULL EXAMPLE ----

class DeploymentJob:
    def __init__(self, job_id: str, service: str, target_env: str):
        self.job_id = job_id
        self.service = service
        self.target_env = target_env
        self.status: str = "pending"

def trigger_deployment(job: DeploymentJob, initiated_by: str) -> bool:
    job.status = "running"
    print(f"Deploying {job.service} to {job.target_env} — by {initiated_by}")
    return True

def get_job_status(job: DeploymentJob) -> str:
    return job.status


job = DeploymentJob("JOB-001", "payment-service", "production")
trigger_deployment(job, "Ankit Sharma")
print(get_job_status(job))   # running


# ============================================================
# WHAT mypy CATCHES:
#
# ✅ Wrong argument types passed to functions
# ✅ Wrong return types from functions
# ✅ Wrong types assigned to annotated variables
# ✅ Forgetting to handle None from Optional returns
# ✅ Calling methods that don't exist on a type
#
# WHEN TO RUN mypy:
# - Before every commit (add to pre-commit hooks)
# - In CI/CD pipeline as a quality gate
# - Locally during development
#
# COMMAND: mypy your_file.py --strict
# (--strict enables all optional checks)
# ============================================================
