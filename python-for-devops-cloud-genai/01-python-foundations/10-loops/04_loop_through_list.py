# You do not need range() to loop through a list.
# Pass the list directly after 'in' and Python handles the rest.

# ---- Example 1: Multi-region deployment ----
servers = [
    "api-server-mumbai",
    "api-server-singapore",
    "api-server-frankfurt",
    "api-server-virginia"
]

print("=== Multi-Region Deployment ===")
for server in servers:
    print(f"Deploying build to: {server}")

print(f"\nTotal deployments: {len(servers)}")

# ---- Example 2: Microservices health check ----
print("\n=== Microservices Health Check ===")
microservices = [
    "auth-service",
    "payment-service",
    "notification-service",
    "user-profile-service",
    "analytics-service"
]

for service in microservices:
    print(f"Health check passed for {service}")

# The code never changes — only the list does.
# 4 servers  → 4 iterations
# 40 servers → 40 iterations
# Zero code changes. This is the real power of loops.
