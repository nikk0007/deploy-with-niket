# ============================================================
# SECTION 1 — BUILT-IN FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

print("=" * 55)
print("  BUILT-IN FUNCTIONS — DevOps Examples")
print("=" * 55)

servers = ["web-01", "db-01", "cache-01", "api-01"]

# len() — Kitne servers hain?
print("\n📌 len() — Total server count:")
print(len(servers))

# type() — Kya type hai?
print("\n📌 type() — Data type check:")
print(type(servers))

# sorted() — Alphabetically sort karo
print("\n📌 sorted() — Alphabetically sorted server list:")
print(sorted(servers))

# max() — Peak CPU usage kya hai?
cpu_readings = [85, 72, 91, 60, 78]
print("\n📌 max() — Peak CPU usage (%):")
print(max(cpu_readings))

# min() — Sabse low CPU usage
print("\n📌 min() — Lowest CPU usage (%):")
print(min(cpu_readings))

# sum() — Total memory usage
memory_usage_gb = [4.2, 8.0, 2.5, 6.1]
print("\n📌 sum() — Total memory used (GB):")
print(sum(memory_usage_gb))

# enumerate() — Index ke saath iterate karna
print("\n📌 enumerate() — Servers with index:")
for idx, server in enumerate(servers, start=1):
    print(f"  [{idx}] {server}")

# zip() — Two lists ko pair karna
cpu_load = [85, 72, 91, 60]
print("\n📌 zip() — Server + CPU paired:")
for server, cpu in zip(servers, cpu_load):
    print(f"  {server} → {cpu}% CPU")

print("\n✅ Rule: Pehle check karo — kya Python mein iska built-in already exist karta hai?")
