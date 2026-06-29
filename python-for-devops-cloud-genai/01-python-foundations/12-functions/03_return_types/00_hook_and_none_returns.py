# HOOK + Section 2: NO RETURN -> None
#
# The story: a deployment health-check function was called, but its
# return value was never captured. The pipeline assumed everything
# was fine and a broken deployment stayed live for hours.

def check_deployment_health(deployment_id):
    error_rate = 42  # simulated metric, in percent
    if error_rate > 5:
        return f"unhealthy: error rate {error_rate}%"
    return "healthy"

print("--- The mistake (return value ignored) ---")
check_deployment_health("deploy-2024-001")   # result is computed, then thrown away
print("Pipeline proceeded anyway - it never saw the health result!\n")

print("--- The fix (return value captured) ---")
health_status = check_deployment_health("deploy-2024-001")
if health_status != "healthy":
    print(f"BLOCKED: deployment is {health_status}. Rolling back.")
else:
    print("Deployment is healthy. Proceeding.")

print()
print("=== Functions with NO return statement -> None ===")


def log_deployment(service_name, version):
    print(f"[LOG] Deploying {service_name} v{version}")
    print(f"[LOG] Triggered by CI/CD pipeline")


result = log_deployment("auth-service", "2.4.1")
print("Return value:", result)   # None

# None is Python's way of saying "nothing" - not zero, not an empty
# string, literally nothing. This is CORRECT behavior for functions
# that only perform an action (logging, alerting, setup) and don't
# need to hand back a result.

print()
print("=== pass: an intentionally empty function (to be implemented later) ===")


def send_slack_alert():
    pass   # will implement later


def trigger_rollback():
    pass   # TODO


send_slack_alert()
trigger_rollback()
print("Both functions ran without errors (they just do nothing yet).")

print()
print("=== When None becomes a problem ===")
result = log_deployment("auth-service", "2.4.1")
try:
    print(result.upper())   # AttributeError: 'NoneType' object has no attribute 'upper'
except AttributeError as e:
    print("AttributeError caught:", e)
    print("Lesson: never assume a function returns something - check first.")
