import asyncio
import time

async def check_server_health():
    print("  [1] Checking server health...")
    await asyncio.sleep(2)      # non-blocking — baaki tasks chal sakte hain
    print("  [1] Server is healthy ✓")
    return "healthy"

async def fetch_from_database():
    print("  [2] Fetching records from database...")
    await asyncio.sleep(3)      # non-blocking
    print("  [2] Got 500 records ✓")
    return [{"id": i} for i in range(500)]

async def call_external_api():
    print("  [3] Calling payment gateway API...")
    await asyncio.sleep(2)      # non-blocking
    print("  [3] Payment API responded ✓")
    return {"status": "ok"}

async def main():
    start = time.time()

    result1, result2, result3 = await asyncio.gather(
        check_server_health(),
        fetch_from_database(),
        call_external_api(),
    )

    end = time.time()
    print(f"\nAll tasks done in {end - start:.2f} seconds")

asyncio.run(main())