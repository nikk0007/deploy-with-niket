# Section 6: MULTIPLE RETURN PATTERNS

print("=== Pattern 1: status + data together ===")
# Don't just return data - return status alongside it, so the
# caller always knows whether the operation actually succeeded.


def fetch_ec2_instance_details(instance_id):
    if not instance_id:
        return None, "Invalid instance ID format"
    if instance_id == "i-terminated":
        return None, "Instance not found - may have been terminated"
    # simulated successful fetch
    details = {
        "instance_type": "t3.large",
        "state": "running",
        "region": "ap-south-1",
        "uptime_hours": 312
    }
    return details, "success"


details, status = fetch_ec2_instance_details("i-0abc123def456")
if status == "success":
    print(f"Instance type: {details['instance_type']} | State: {details['state']}")
else:
    print(f"Fetch failed: {status}")

details, status = fetch_ec2_instance_details("i-terminated")
if status == "success":
    print(f"Instance type: {details['instance_type']} | State: {details['state']}")
else:
    print(f"Fetch failed: {status}")


print()
print("=== Pattern 2: related computed values that belong together ===")


def analyze_pipeline_run_times(durations_seconds):
    average = sum(durations_seconds) / len(durations_seconds)
    longest = max(durations_seconds)
    shortest = min(durations_seconds)
    success_count = len([d for d in durations_seconds if d > 0])
    failure_count = len([d for d in durations_seconds if d <= 0])
    return average, longest, shortest, success_count, failure_count


avg, longest, shortest, passed, failed = analyze_pipeline_run_times(
    [120, 95, -1, 140, 88, 110, -1, 132, 99, 105]
)
print(f"Average: {avg:.1f}s | Longest: {longest}s | Shortest: {shortest}s")
print(f"Successful runs: {passed} | Failed runs: {failed}")


print()
print("=== When to use multiple return vs a dictionary ===")
print("2-4 fixed, predictable values  -> multiple return (tuple unpacking)")
print("5+ values, or structure may change -> return a dictionary")

# Example of the dictionary style for a larger structure:
example_response = {
    "status": "ok",
    "data": {"region": "ap-south-1"},
    "metadata": {"source": "audit-script"},
    "request_id": "req-12345",
    "timestamp": "2026-06-21T10:00:00Z",
    "processing_time_ms": 142
}
print(example_response)
