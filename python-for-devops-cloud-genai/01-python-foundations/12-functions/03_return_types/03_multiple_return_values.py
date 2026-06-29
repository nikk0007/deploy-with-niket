# Section 5: MULTIPLE RETURN VALUES - Python's secret
# Example: a server metrics check that needs to report several
# numbers and a status, all in one go.

def get_server_metrics(server_id):
    cpu_usage = 73.4       # simulated data
    memory_usage = 61.2
    disk_usage = 45.8
    status = "healthy"
    return cpu_usage, memory_usage, disk_usage, status


cpu, memory, disk, status = get_server_metrics("prod-server-01")
print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}% | Status: {status}")

# ---------------------------------------------------------------
# What's actually happening under the hood:
# Python automatically packs the multiple values into a tuple.
# ---------------------------------------------------------------
result = get_server_metrics("prod-server-01")
print("Type of result:", type(result))   # <class 'tuple'>
print("Result:", result)                  # (73.4, 61.2, 45.8, 'healthy')

# ---------------------------------------------------------------
# Underscore convention - take what you need, ignore the rest
# ---------------------------------------------------------------
cpu, _, _, status = get_server_metrics("prod-server-01")
print(f"\nOnly CPU and status needed -> CPU: {cpu}% | Status: {status}")

# The underscore (_) is a widely used Python convention meaning:
# "I know this value exists, but I don't need it."
