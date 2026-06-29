# SECTION 3 DEMO — Parameters, Arguments, and Return

# ── Parameter vs Argument ──
# Parameter — function definition mein jo variable naam likhte ho. Placeholder hai.
# Argument — jab call karte ho to jo actual value dete ho.

def calculate_cloud_cost(instance_type, hours_running):   # ye hain parameters
    hourly_rate = 8.5 if instance_type == "gpu" else 2.0
    return hourly_rate * hours_running

cost = calculate_cloud_cost("gpu", 6)   # ye hain arguments
print(f"Your cloud cost: Rs.{cost}")    # Rs.51.0


# ── Return value ke bina ──
# Jaise ek kaam kar diya aur result dustbin mein phenk diya.

def log_deployment(service_name):
    print(f"Deployment recorded: {service_name}")
    # kuch return nahi kiya

result = log_deployment("auth-service")
print(result)   # None — kuch nahi mila


# ── Return value ke saath ──

def is_pod_healthy(restart_count):
    return restart_count == 0

check = is_pod_healthy(0)
print(check)   # True

if is_pod_healthy(3):
    print("Pod is stable")
else:
    print("Pod needs investigation")

# GOLDEN RULE:
# Agar output baad mein use karna hai — return likho.
# Agar function sirf ek action perform karta hai aur result ki zaroorat nahi — return optional hai.
