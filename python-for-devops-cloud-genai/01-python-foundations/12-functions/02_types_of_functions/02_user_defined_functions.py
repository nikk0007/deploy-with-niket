# ============================================================
# SECTION 2 — USER-DEFINED FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

print("=" * 55)
print("  USER-DEFINED FUNCTIONS — DevOps Examples")
print("=" * 55)

# ----- Basic user-defined function -----
def check_server_health(server_name, cpu_usage):
    """Check if a server's CPU usage is within safe limits."""
    if cpu_usage > 80:
        return f"🔴 ALERT: {server_name} — CPU at {cpu_usage}%"
    elif cpu_usage > 60:
        return f"🟡 WARN:  {server_name} — CPU at {cpu_usage}%"
    return f"🟢 OK:    {server_name} — CPU at {cpu_usage}%"


print("\n📌 check_server_health() — Server health monitor:")
print(check_server_health("web-01", 91))
print(check_server_health("db-01", 55))
print(check_server_health("cache-01", 68))


# ----- Function with default parameter -----
def restart_service(service_name, reason="manual restart"):
    """Restart a service with an optional reason."""
    print(f"\n🔄 Restarting '{service_name}' — Reason: {reason}")
    return True


print("\n📌 restart_service() — With default parameter:")
restart_service("nginx")
restart_service("postgres", reason="OOMKilled")


# ----- Function with multiple return values -----
def get_instance_summary(instance_id, cpu, memory_gb):
    """Return a summary dict for an EC2 instance."""
    status = "HEALTHY" if cpu < 80 and memory_gb < 14 else "NEEDS_ATTENTION"
    return {
        "instance_id": instance_id,
        "cpu_percent": cpu,
        "memory_gb": memory_gb,
        "status": status,
    }


print("\n📌 get_instance_summary() — Multiple values returned as dict:")
summary = get_instance_summary("i-0abc123", cpu=45, memory_gb=7.2)
for key, value in summary.items():
    print(f"  {key}: {value}")

print("\n✅ Functions ke 3 parts: Parameters | Body | Return Value")
