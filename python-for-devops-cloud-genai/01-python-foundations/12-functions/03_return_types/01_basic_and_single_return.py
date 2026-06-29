# Section 1: WHY FUNCTIONS RETURN VALUES
# Example: an autoscaler needs to know if a cloud instance type is
# available before it can decide whether to scale up or wait.

def check_instance_availability(instance_type):
    available_types = {"t3.large", "t3.xlarge", "m5.large"}
    return instance_type in available_types


is_available = check_instance_availability("t3.large")
print(f"t3.large available: {is_available}")

if is_available:
    print("Action: launch new instance")
else:
    print("Action: wait and retry, or pick a different instance type")


print()
print("=== Section 3: SINGLE RETURN - one clear answer ===")


def calculate_monthly_cloud_cost(usage_hours, hourly_rate):
    total_cost = usage_hours * hourly_rate
    return round(total_cost, 2)


monthly_bill = calculate_monthly_cloud_cost(720, 0.096)
print(f"Estimated monthly cost: ${monthly_bill}")

# ---------------------------------------------------------------
# return immediately exits the function - code after it never runs
# ---------------------------------------------------------------


def get_server_region(server_code):
    return f"Region: {server_code}-ap-south"
    print("This will NEVER run")   # dead code


print(get_server_region("prod-01"))

# ---------------------------------------------------------------
# Three ways to use a return value
# ---------------------------------------------------------------

# Way 1 - store in a variable
monthly_bill = calculate_monthly_cloud_cost(720, 0.096)
print("Way 1 ->", monthly_bill)

# Way 2 - use directly in a condition
if calculate_monthly_cloud_cost(720, 0.15) > 100:
    print("Way 2 -> Cost alert: consider reserved instances")

# Way 3 - pass directly into another function (here, an f-string)
print(f"Way 3 -> Your bill: ${calculate_monthly_cloud_cost(720, 0.096)}")
