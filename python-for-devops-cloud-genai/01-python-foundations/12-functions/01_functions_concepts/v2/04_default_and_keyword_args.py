# ============================================================
# 04_default_and_keyword_args.py
# Topic: Default Parameters and Keyword Arguments
# ============================================================

# Default parameters let you define fallback values.
# If the caller does not provide that argument — the default is used.
# If they do provide it — the default is overridden.

# ---- Default parameters in action ----

def send_alert(message, recipient="ops-team@company.com", priority="normal"):
    """
    Send an ops alert. recipient and priority have sensible defaults
    so callers only need to supply them when they differ from the norm.
    """
    print(f"[{priority.upper()}] To: {recipient} | {message}")

# All three arguments supplied — defaults are overridden
send_alert("Database CPU at 95%", "dba-team@company.com", "critical")

# Only message supplied — recipient and priority use defaults
send_alert("Nightly backup completed successfully")

# Only message and priority supplied — recipient uses default
send_alert("SSL certificate expiring in 7 days", priority="high")

print()

# ---- Keyword arguments — pass by name, not position ----
# Normally Python matches arguments left-to-right by position.
# Keyword arguments let you pass them in any order using the parameter name.

send_alert(
    priority="critical",
    message="Payment gateway timeout detected",
    recipient="payments-team@company.com"
)

print()

# ---- A more realistic DevOps example ----

def deploy_service(service_name, environment="staging", replicas=2, rollback_on_fail=True):
    """
    Trigger a deployment with sensible production defaults.
    """
    print(f"Deploying  : {service_name}")
    print(f"Environment: {environment}")
    print(f"Replicas   : {replicas}")
    print(f"Auto-rollback on failure: {rollback_on_fail}")
    print()

# Quick staging deploy — use almost all defaults
deploy_service("auth-service")

# Production deploy — override what differs
deploy_service("payment-service", environment="production", replicas=5)

# Feature branch deploy — disable rollback for testing
deploy_service("search-service", environment="dev", replicas=1, rollback_on_fail=False)

# ---- The rule: default parameters must come AFTER non-default ones ----
print("=== The ordering rule ===")
print("""
CORRECT:
  def func(name, age, city="Delhi"):
      ...

WRONG — SyntaxError:
  def func(city="Delhi", name, age):
      ...

Why? Python matches arguments by position first.
If a default parameter comes first, Python cannot tell
which positional argument belongs to which parameter.
""")
