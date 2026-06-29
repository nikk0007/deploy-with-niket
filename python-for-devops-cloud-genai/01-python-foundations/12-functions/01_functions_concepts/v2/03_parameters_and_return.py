# ============================================================
# 03_parameters_and_return.py
# Topic: Parameters, Arguments, and Return Values
# ============================================================

# Parameters vs Arguments — people use these interchangeably, but there is a difference:
#
#   Parameter → the variable name in the function DEFINITION (a placeholder)
#   Argument  → the actual value you pass when CALLING the function
#
# Think of a parameter as a blank form field. An argument is what you fill in.

# ---- Parameters in the definition ----
def calculate_cloud_cost(instance_type, hours_running, cost_per_hour):   # <-- parameters
    total = hours_running * cost_per_hour
    return f"{instance_type} ran for {hours_running}h — Cost: Rs.{round(total, 2)}"

# ---- Arguments in the call ----
print(calculate_cloud_cost("t3.medium", 720, 8.50))    # <-- arguments
print(calculate_cloud_cost("c5.xlarge", 168, 34.20))
print(calculate_cloud_cost("p3.2xlarge", 48, 280.00))
print()

# ============================================================
# RETURN VALUES — why return matters
# ============================================================

# Without return — function acts but gives nothing back.
# Like a job that does the work but throws the result in the bin.

def log_deployment_no_return(service, environment):
    message = f"[DEPLOY] {service} deployed to {environment}"
    print(message)
    # No return — result is lost after the function ends

result = log_deployment_no_return("auth-service", "production")
print(f"Return value without return: {result}")   # None
print()

# With return — the caller gets the result and can use it.

def check_pod_health(pod_name, cpu_usage, memory_usage):
    """
    Returns 'healthy', 'warning', or 'critical' based on resource usage.
    """
    if cpu_usage > 90 or memory_usage > 90:
        return "critical"
    elif cpu_usage > 70 or memory_usage > 70:
        return "warning"
    else:
        return "healthy"

# The return value can be stored, printed, or used in a condition.
pods = [
    ("payment-pod-01", 45, 60),
    ("auth-pod-02",    78, 55),
    ("search-pod-03",  95, 88),
]

for pod_name, cpu, mem in pods:
    status = check_pod_health(pod_name, cpu, mem)   # return value stored here
    print(f"Pod: {pod_name:<20} CPU: {cpu}%  MEM: {mem}%  Status: {status.upper()}")

print()
print("Golden rule:")
print("  If you need the result later → write return.")
print("  If the function only performs an action and result is not needed → return is optional.")
