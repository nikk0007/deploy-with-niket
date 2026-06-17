import asyncio
import time

async def health_check(service):
    print(f"Pinging {service}...")
    # never use time.sleep() in async functions, use asyncio.sleep() instead
    await asyncio.sleep(2)
    print(f"{service} is UP")

async def main():
    # await means "wait for this to finish before moving on"
    await asyncio.gather(
        health_check("auth-service"),
        health_check("payment-service"),
        health_check("notification-service"),
    )
    
    # the below print statement will only run after all the above tasks are done
    print("All services are UP")

start = time.time()

asyncio.run(main())

end = time.time()

print(f"\nTotal time taken: {end - start:.2f} seconds")
