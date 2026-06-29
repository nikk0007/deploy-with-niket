# SECTION 9 DEMO — Best Practices

# ── Rule 1: Ek function, ek kaam ──
# BAD — ek function mein teen kaam thunse hue hain
def validate_and_deploy_and_notify(service_name):
    pass  # this is doing too much — split it!

# GOOD — har function ka apna ek kaam
def validate_service_config(service_name):
    print(f"Validating config for {service_name}...")
    return True

def deploy_service(service_name):
    print(f"Deploying {service_name}...")

def notify_team(service_name):
    print(f"Notifying team: {service_name} deployment complete.")

# Ab inhe orchestrate karo
def run_deployment_pipeline(service_name):
    if validate_service_config(service_name):
        deploy_service(service_name)
        notify_team(service_name)

run_deployment_pipeline("payment-service")


# ── Rule 2: Naam se kaam pata chale ──

# Bad
def proc(x, flag):
    pass

# Good
def calculate_autoscaling_threshold(current_load, is_peak_hours):
    pass

# Code comment ki zaroorat tab padti hai jab naam clear nahi hota.
# Naam clear ho to comment ki zaroorat hi nahi.


# ── Rule 3: Functions chhote rakho ──
# 20-25 lines se zyada ka function usually do ya teen kaam kar raha hota hai. Split karo.


# ── Rule 4: Docstring likho ──

def calculate_monthly_cloud_bill(compute_hours, hourly_rate, storage_gb, storage_rate_per_gb):
    """
    Calculate estimated monthly cloud infrastructure bill.

    compute_hours: Total compute hours used in the month
    hourly_rate: Cost per compute hour in Rs.
    storage_gb: Total storage used in GB
    storage_rate_per_gb: Cost per GB of storage in Rs.
    Returns: Total estimated bill in Rs., rounded to 2 decimal places
    """
    compute_cost = compute_hours * hourly_rate
    storage_cost = storage_gb * storage_rate_per_gb
    return round(compute_cost + storage_cost, 2)

bill = calculate_monthly_cloud_bill(720, 2.5, 500, 0.10)
print(f"Estimated monthly bill: Rs.{bill}")


# ── Rule 5: Side effects se bachao ──
# Function jo sirf apne inputs use kare aur output return kare —
# predictable hai, testable hai, trustworthy hai.
#
# Function jo silently global variables modify kare, files likhe, ya
# external systems ko touch kare bina caller ko bataye — debugging nightmare hai.

# THE MINDSET SHIFT:
# Jab bhi ek kaam do jagah likhte ho — ruko. Function banao.
# Jab bhi function 30 lines se zyada ho — ruko. Todoo.
# Jab bhi function ka naam clear nahi ho raha — ruko. Naam sochne mein time lagao.
# Agar naam nahi soch pa rahe to matlab function ka kaam hi clear nahi hai.
