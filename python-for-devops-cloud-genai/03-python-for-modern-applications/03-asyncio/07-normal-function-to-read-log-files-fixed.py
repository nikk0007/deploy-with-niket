import asyncio
import time

LOG_FILES = [
    "app.log",
    "error.log",
    "access.log",
    "audit.log",
    "debug.log"
]

async def read_log_file(filename):
    print(f"  Reading {filename}...")
    await asyncio.sleep(2)              # non-blocking I/O simulation
    print(f"  Done reading {filename}")
    return f"contents of {filename}"

async def process_all_logs():
    start = time.time()

    tasks = [read_log_file(log) for log in LOG_FILES]
    
    # *tasks unpacks the list of tasks into separate arguments for asyncio.gather()
    # i.e., asyncio.gather(task1, task2, task3, ...)
    results = await asyncio.gather(*tasks)

    end = time.time()
    print(f"\nRead {len(LOG_FILES)} files in {end - start:.2f} seconds")

asyncio.run(process_all_logs())

#=============================================================
# Just for the record: Below is the Expanded form without list comprehension
async def process_all_logs_expanded_form():
    start = time.time()

    # Expanded form — each coroutine created explicitly
    task1 = read_log_file("app.log")
    task2 = read_log_file("error.log")
    task3 = read_log_file("access.log")
    task4 = read_log_file("audit.log")
    task5 = read_log_file("debug.log")

    results = await asyncio.gather(task1, task2, task3, task4, task5)

    end = time.time()
    print(f"\nRead 5 files in {end - start:.2f} seconds")
    #=============================================================