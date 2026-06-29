# SECTION 5 DEMO — Scope: Local vs Global

cloud_provider = "AWS"   # global

def deploy_service(service_name):
    region = "ap-south-1"   # local — sirf yahan exist karta hai
    print(f"Deploying {service_name} on {cloud_provider} in {region}")

deploy_service("payment-service")
print(cloud_provider)   # chalega — global hai
# print(region)         # NameError — region yahan exist hi nahi karta (uncomment to test)


# ── global keyword — jab global variable ko function ke andar modify karna ho ──

deployment_count = 0

def trigger_deployment(service):
    global deployment_count
    deployment_count += 1
    print(f"Deployment #{deployment_count}: {service} deployed successfully")

trigger_deployment("user-service")
trigger_deployment("auth-service")
trigger_deployment("notification-service")
print(f"Total deployments: {deployment_count}")   # 3

# PROFESSIONAL ADVICE:
# global use karna ek code smell hai — iska matlab hai tum shared state use kar
# rahe ho jo debugging mein pain deta hai.
# Jab bhi ho sake — data parameters mein pass karo aur return karo.
# Clean functions apne inputs pe depend karti hain, hidden global state pe nahi.
