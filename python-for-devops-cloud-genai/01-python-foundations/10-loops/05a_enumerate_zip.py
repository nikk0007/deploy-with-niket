# ---- enumerate() — get the index alongside each item ----
print("=== enumerate() — GenAI Prompt Batch Logging ===")
prompts = [
    "Summarize this PDF",
    "Translate to Hindi",
    "Generate test cases",
    "Extract key entities"
]

# start=1 makes the index begin at 1 instead of 0
for index, prompt in enumerate(prompts, start=1):
    print(f"Prompt #{index}: {prompt}")

# Default behaviour: index starts at 0
print("\n=== enumerate() — start=0 (default) ===")
for index, prompt in enumerate(prompts):
    print(f"[{index}] {prompt}")


# ---- zip() — loop over two lists at the same time ----
print("\n=== zip() — Region + Latency Monitoring Dashboard ===")
regions = ["Mumbai", "Singapore", "Frankfurt", "Virginia"]
latency_ms = [12, 45, 130, 180]

for region, latency in zip(regions, latency_ms):
    print(f"Region {region} — current latency: {latency}ms")


# ---- zip() with three lists ----
print("\n=== zip() — Three Lists Together ===")
instance_ids   = ["i-001", "i-002", "i-003"]
instance_types = ["t3.medium", "c5.large", "m5.xlarge"]
statuses       = ["running", "stopped", "running"]

for iid, itype, status in zip(instance_ids, instance_types, statuses):
    print(f"{iid} | {itype} | Status: {status}")


# ---- Combining enumerate and zip ----
print("\n=== enumerate + zip — Numbered Region Report ===")
for idx, (region, latency) in enumerate(zip(regions, latency_ms), start=1):
    print(f"#{idx} | {region} | {latency}ms")

