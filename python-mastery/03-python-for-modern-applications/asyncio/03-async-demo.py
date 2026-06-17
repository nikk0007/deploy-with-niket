import asyncio

async def health_check(service_name):
    print(f"Checking {service_name}...")
    await asyncio.sleep(2)
    print(f"{service_name} is UP")

asyncio.run(health_check("auth-service"))