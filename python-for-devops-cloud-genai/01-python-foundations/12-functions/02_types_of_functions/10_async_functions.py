# ============================================================
# SECTION 10 — ASYNC FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

import asyncio
import time

print("=" * 55)
print("  ASYNC FUNCTIONS — DevOps & GenAI Examples")
print("=" * 55)


# ---- Problem: Sequential health checks (slow) ----

def check_service_sync(service_name, latency=0.5):
    """Synchronous check — blocks until done."""
    time.sleep(latency)   # Simulates HTTP request
    return {"service": service_name, "status": "healthy"}


print("\n📌 SYNC approach — services checked ONE BY ONE (slow):")
services = [
    "auth-service",
    "payment-service",
    "notification-service",
    "order-service",
    "inventory-service",
]

start = time.time()
sync_results = [check_service_sync(svc) for svc in services]
elapsed = time.time() - start
print(f"  ⏱️  Sync time: {elapsed:.2f}s for {len(services)} services")
print(f"  (Each service ~0.5s → Total ≈ {len(services) * 0.5}s expected)")


# ---- Solution: Async health checks (concurrent) ----

async def check_service_health(service_name, latency=0.5):
    """Async — non-blocking, runs concurrently with other coroutines."""
    await asyncio.sleep(latency)   # Simulates actual HTTP call
    print(f"  ✅ {service_name} — Healthy")
    return {"service": service_name, "status": "healthy"}


async def run_all_health_checks():
    """Run all health checks concurrently using asyncio.gather()."""
    print("\n📌 ASYNC approach — all services checked CONCURRENTLY:")
    start = time.time()

    results = await asyncio.gather(
        *[check_service_health(svc) for svc in services]
    )

    elapsed = time.time() - start
    print(f"\n  ⏱️  Async time: {elapsed:.2f}s for {len(results)} services")
    print(f"  (All ran simultaneously → Total ≈ 0.5s expected)")
    return results


asyncio.run(run_all_health_checks())


# ---- Async with real-world pattern: concurrent AWS calls ----

async def fetch_region_summary(region, latency=0.4):
    """Simulates fetching EC2 + RDS summary from a region."""
    await asyncio.sleep(latency)
    return {
        "region":    region,
        "ec2_count": 12,
        "rds_count": 3,
        "status":    "ok",
    }


async def multi_region_summary():
    regions = ["ap-south-1", "us-east-1", "eu-west-1", "ap-southeast-1"]

    print("\n📌 multi_region_summary() — Concurrent AWS region queries:")
    start   = time.time()
    results = await asyncio.gather(*[fetch_region_summary(r) for r in regions])
    elapsed = time.time() - start

    for r in results:
        print(f"  [{r['region']}] EC2: {r['ec2_count']} | RDS: {r['rds_count']}")
    print(f"  ⏱️  Total time: {elapsed:.2f}s (fetched {len(regions)} regions concurrently)")


asyncio.run(multi_region_summary())


# ---- Async generator: streaming LLM response ----

async def stream_llm_async(tokens):
    """Async generator — simulates real LLM streaming with async I/O."""
    for token in tokens:
        await asyncio.sleep(0.05)   # Simulate token generation latency
        yield token


async def display_streaming_response():
    tokens = [
        "Kubernetes", " pods", " are", " the",
        " smallest", " deployable", " unit",
        " in", " a", " cluster", "."
    ]
    print("\n📌 Async generator — LLM streaming response:")
    print("  Response: ", end="", flush=True)
    async for token in stream_llm_async(tokens):
        print(token, end="", flush=True)
    print()


asyncio.run(display_streaming_response())


print("\n✅ async/await is used in:")
print("   - FastAPI route handlers (@app.get, @app.post)")
print("   - LangChain / LiteLLM LLM calls")
print("   - AWS boto3 aioboto3 concurrent API calls")
print("   - Kubernetes health checkers")
print("\n✅ KEY RULE:")
print("   async def  → defines a coroutine")
print("   await      → waits for a coroutine without blocking others")
print("   asyncio.gather() → runs multiple coroutines concurrently")
