import time

def check_server_health():
    print("  [1] Checking server health...")
    time.sleep(2)
    print("  [1] Server is healthy ✓")
    return "healthy"

def fetch_from_database():
    print("  [2] Fetching records from database...")
    time.sleep(3)
    print("  [2] Got 500 records ✓")
    # returning a list of 500 records (dictionaries with an 'id' key)
    return [{"id": i} for i in range(500)]

def call_external_api():
    print("  [3] Calling payment gateway API...")
    time.sleep(2)
    print("  [3] Payment API responded ✓")
    return {"status": "ok"}

def main():
    start = time.time()

    result1 = check_server_health()
    result2 = fetch_from_database()
    result3 = call_external_api()

    end = time.time()
    
    # .2f means 2 decimal places (to avoid long float numbers like 7.0076165199279785)
    print(f"\nAll tasks done in {end - start:.2f} seconds")

main()