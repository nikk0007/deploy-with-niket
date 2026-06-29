import time

LOG_FILES = [
    "app.log",
    "error.log",
    "access.log",
    "audit.log",
    "debug.log"
]

def read_log_file(filename):
    print(f"  Reading {filename}...")
    time.sleep(2)
    print(f"  Done reading {filename}")
    return f"contents of {filename}"

def process_all_logs():
    start = time.time()

    results = []
    for log in LOG_FILES:
        content = read_log_file(log)
        results.append(content)

    end = time.time()
    print(f"\nRead {len(LOG_FILES)} files in {end - start:.2f} seconds")

process_all_logs()