# Section 9: COMMON MISTAKES with return values

print("=== Mistake 1: writing code after return (dead code) ===")


def get_instance_id():
    return "i-0abc123def456"
    print("Done")   # this will NEVER run - dead code


print(get_instance_id())
print("Always make sure 'return' is the last statement in its block.\n")


print("=== Mistake 2: not capturing the return value ===")


def validate_api_key(key):
    return key.startswith("sk-") and len(key) > 10


validate_api_key("sk-prod-xxxxxxxx")             # result is thrown away
is_valid = validate_api_key("sk-prod-xxxxxxxx")  # correct way
print("Captured result:", is_valid)
print("If you need the result, always store it in a variable.\n")


print("=== Mistake 3: unpacking mismatch ===")


def get_region_zone():
    return "ap-south-1", "ap-south-1a"   # 2 values


try:
    region, zone, extra = get_region_zone()   # ValueError: too many values to unpack
except ValueError as e:
    print("ValueError caught:", e)

region, zone = get_region_zone()   # correct - matches the number of values
print(f"Correct unpacking -> region: {region}, zone: {zone}\n")


print("=== Mistake 4: assuming a function returns something ===")


def display_deployment_summary(deployment_id):
    print(f"Deployment summary for: {deployment_id}")
    # no return statement here


summary = display_deployment_summary("deploy-2024-001")
try:
    status = summary["status"]   # TypeError: 'NoneType' object is not subscriptable
except TypeError as e:
    print("TypeError caught:", e)
    print("Lesson: check whether a function actually returns something before using the result.")


print()
print("=== Final rules (recap) ===")
print("- Action only, no result needed      -> no return (None is expected)")
print("- One clear result needed            -> single return")
print("- Different results based on logic   -> conditional return, prefer early return")
print("- Caller needs several related values -> multiple return (tuple unpacking, 2-4 values)")
print("- 5+ values or flexible structure     -> return a dictionary")
