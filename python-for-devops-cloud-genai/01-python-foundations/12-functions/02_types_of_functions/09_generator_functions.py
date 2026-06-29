# ============================================================
# SECTION 9 — GENERATOR FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

import time

print("=" * 55)
print("  GENERATOR FUNCTIONS — DevOps & GenAI Examples")
print("=" * 55)


# ---- Problem: Loading all logs at once (Memory hog) ----

print("\n📌 Regular function — loads EVERYTHING into memory at once:")

def read_all_error_logs_bad(log_entries):
    """BAD: Loads all matching logs into a list — memory intensive!"""
    result = []
    for entry in log_entries:
        if "ERROR" in entry:
            result.append(entry)
    return result   # Returns entire list at once

# Simulate 1 million log lines
all_logs = [
    f"Log line {i}: {'ERROR - Connection refused' if i % 100 == 0 else 'INFO - Request processed'}"
    for i in range(1_000_000)
]
print(f"  Total log lines: {len(all_logs):,}")
error_list = read_all_error_logs_bad(all_logs)
print(f"  Errors found:    {len(error_list):,}")
print("  ⚠️  Entire error list loaded into RAM — risky at scale!")


# ---- Solution: Generator function ----

print("\n📌 Generator function — yields ONE at a time, memory safe:")

def read_large_log(log_entries):
    """GOOD: Yields one log at a time — constant memory usage!"""
    for entry in log_entries:
        if "ERROR" in entry:
            yield entry   # ← yield, not return!


error_logs = read_large_log(all_logs)   # Nothing loaded yet!
print(f"  Type: {type(error_logs)}")    # <generator object>

print("  First 5 errors:")
for i, error in enumerate(error_logs):
    print(f"    {error}")
    if i == 4:
        break

print("  ✅ Memory constant — 1M lines processed without loading all!")


# ---- Generator: Paginated AWS API results ----

def paginate_ec2_instances(total_instances, page_size=5):
    """
    Simulates paginated AWS API response.
    Yields one page at a time — like boto3 paginators.
    """
    instance_ids = [f"i-{str(n).zfill(4)}" for n in range(total_instances)]
    for i in range(0, total_instances, page_size):
        page = instance_ids[i:i + page_size]
        print(f"  📦 Fetching page {i // page_size + 1} from AWS API...")
        yield page   # Yield one page at a time


print("\n📌 paginate_ec2_instances() — Simulates AWS paginator:")
for page in paginate_ec2_instances(total_instances=18, page_size=5):
    print(f"    Processing: {page}")


# ---- Generator: LLM Streaming Response (GenAI) ----

def stream_llm_response(tokens):
    """
    Simulates LLM token streaming — like ChatGPT typing response word by word.
    yield makes this memory-efficient and enables real-time display.
    """
    for token in tokens:
        yield token


response_tokens = [
    "Kubernetes", " is", " an", " open-source",
    " container", " orchestration", " platform",
    " that", " automates", " deployment,",
    " scaling,", " and", " management", "."
]

print("\n📌 stream_llm_response() — GenAI streaming simulation:")
print("  Streaming response: ", end="")
for token in stream_llm_response(response_tokens):
    print(token, end="", flush=True)
    time.sleep(0.08)   # Simulate token generation delay
print()


# ---- yield vs return ----

print("\n📌 KEY DIFFERENCE: return vs yield")
print("  Regular function → computes ALL results, returns at once")
print("  Generator function → computes ONE result at a time with yield")
print("  Generator is LAZY — only runs when you ask for the next item")


# Quick demo of laziness
def lazy_demo():
    print("  [Generator] About to yield 1")
    yield 1
    print("  [Generator] About to yield 2")
    yield 2
    print("  [Generator] About to yield 3")
    yield 3

print("\n📌 Generator is LAZY — runs only when iterated:")
gen = lazy_demo()
print("  Generator created. Nothing ran yet.")
print(f"  next(gen) → {next(gen)}")
print(f"  next(gen) → {next(gen)}")
print(f"  next(gen) → {next(gen)}")

print("\n✅ Use generators when:")
print("   - Large files / logs process karne ho (CloudWatch, S3)")
print("   - Paginated API responses handle karne ho (AWS, GitHub)")
print("   - LLM token streaming implement karna ho")
print("   - Memory constraints hain production systems mein")
