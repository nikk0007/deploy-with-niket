# DEMO 2 — Filtering with if
# Real-world scenario: filtering Kubernetes pods that are using too much memory

pod_memory_mb = [120, 512, 980, 256, 1500, 64]
MEMORY_THRESHOLD = 500

# ── Normal loop ──
high_memory_pods = []
for mem in pod_memory_mb:
    if mem >= MEMORY_THRESHOLD:
        high_memory_pods.append(mem)

print(high_memory_pods)
# Output: [512, 980, 1500]


# ── Comprehension ──
high_memory_pods = [mem for mem in pod_memory_mb if mem >= MEMORY_THRESHOLD]

print(high_memory_pods)
# Same output: [512, 980, 1500]

# Read as:
# "Give me mem for every mem in pod_memory_mb if mem is >= threshold"
