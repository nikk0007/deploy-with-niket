# ============================================================
# 05_scope.py
# Topic: Scope — Where Variables Live and Die
# ============================================================

# Scope = the area of your code where a variable exists and is accessible.
#
# Local scope  → variable created INSIDE a function.
#                It lives only for the duration of that function call.
#                When the function ends, the variable is destroyed.
#
# Global scope → variable created OUTSIDE any function.
#                It lives for the entire life of the script.

# ---- Local scope ----

cloud_provider = "AWS"   # global variable — accessible everywhere

def deploy_service(service_name):
    region = "ap-south-1"   # local variable — only exists inside this function
    print(f"Deploying {service_name} on {cloud_provider} in {region}")

deploy_service("payment-service")
deploy_service("auth-service")

print(f"\ncloud_provider is accessible here: {cloud_provider}")

# This would cause a NameError — 'region' does not exist outside the function:
# print(region)   # NameError: name 'region' is not defined

print()

# ---- global keyword — modifying a global variable from inside a function ----
# By default, a function cannot modify a global variable — it can only read it.
# To modify it, you must explicitly declare it with the 'global' keyword.

deployment_count = 0

def trigger_deployment(service):
    global deployment_count          # tell Python: use the global variable, not a local one
    deployment_count += 1
    print(f"Deployment #{deployment_count}: {service} deployed successfully")

trigger_deployment("user-service")
trigger_deployment("auth-service")
trigger_deployment("notification-service")

print(f"\nTotal deployments recorded: {deployment_count}")

print()

# ---- Why global is considered a code smell ----
# Using global creates hidden shared state — hard to track, hard to test, hard to debug.
# The professional alternative: pass data in as parameters and return results.

print("=== Professional alternative to global state ===\n")

def trigger_deployment_clean(service, current_count):
    """
    Takes the current count as input, returns the updated count.
    No hidden shared state. Predictable. Testable.
    """
    current_count += 1
    print(f"Deployment #{current_count}: {service} deployed successfully")
    return current_count

count = 0
count = trigger_deployment_clean("user-service", count)
count = trigger_deployment_clean("auth-service", count)
count = trigger_deployment_clean("notification-service", count)

print(f"\nTotal deployments: {count}")

print("""
Rule of thumb:
  Use global sparingly — only for true application-wide constants.
  For anything that changes — pass it in as a parameter and return it.
  Clean functions depend only on their inputs. No hidden state.
""")
