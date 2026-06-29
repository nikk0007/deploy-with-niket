"""
DEMO 02: Multiple except blocks
Topic: Exception & Error Handling in Python
Use Case: Cloud / DevOps — Calling a health-check or metrics API endpoint

Run this file to see different exceptions handled differently.
We simulate various failure modes using mock responses.
"""

import json


# ─────────────────────────────────────────────────────────────────────────────
# We'll mock requests to avoid a real network dependency.
# In your own project, remove the mock and use actual requests.
# ─────────────────────────────────────────────────────────────────────────────

class MockTimeout(Exception):
    pass

class MockConnectionError(Exception):
    pass

class MockHTTPError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"HTTP {status_code}")

class MockResponse:
    def __init__(self, data, status_code=200):
        self._data = data
        self.status_code = status_code

    def json(self):
        if self._data == "__invalid_json__":
            raise ValueError("No JSON object could be decoded")
        return self._data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise MockHTTPError(self.status_code)


def simulate_api_call(scenario):
    """Simulates different API failure scenarios."""
    if scenario == "timeout":
        raise MockTimeout("Request timed out after 10s")
    elif scenario == "connection_error":
        raise MockConnectionError("Failed to establish connection")
    elif scenario == "503":
        return MockResponse({}, status_code=503)
    elif scenario == "401":
        return MockResponse({}, status_code=401)
    elif scenario == "invalid_json":
        return MockResponse("__invalid_json__")
    else:
        return MockResponse({"cpu": 42.5, "memory": 68.2, "pods_running": 12})


# ─────────────────────────────────────────────────────────────────────────────
# MAIN FUNCTION: fetch_cluster_metrics with multiple except blocks
# ─────────────────────────────────────────────────────────────────────────────

def fetch_cluster_metrics(scenario="success"):
    """
    Fetches Kubernetes cluster metrics from a monitoring endpoint.
    Handles each failure type with a specific, appropriate response.
    """
    endpoint = "https://monitoring.internal/api/v1/metrics"
    print(f"\n[*] Fetching cluster metrics from: {endpoint}")
    print(f"    Simulating scenario: '{scenario}'")

    try:
        response = simulate_api_call(scenario)
        response.raise_for_status()
        data = response.json()
        print(f"[+] Metrics received: {json.dumps(data, indent=4)}")
        return data

    except MockTimeout:
        print("[-] Metrics endpoint timed out.")
        print("    Action: Scheduling retry in next monitoring cycle.")
        return None

    except MockConnectionError:
        print("[-] Cannot connect to metrics endpoint.")
        print("    Action: Triggering PagerDuty alert — service may be down.")
        # In real code: pagerduty_alert("Cluster metrics unreachable")
        raise  # Re-raise because this is a hard failure

    except MockHTTPError as e:
        if e.status_code == 503:
            print("[-] Metrics service temporarily unavailable (503).")
            print("    Action: Will retry after backoff. Not alerting yet.")
            return None
        elif e.status_code == 401:
            print("[-] Authentication failed (401).")
            print("    Action: Check service account token or API key rotation.")
            raise
        else:
            print(f"[-] Unexpected HTTP error: {e}")
            raise

    except ValueError:
        print("[-] Metrics endpoint returned invalid JSON.")
        print("    Action: Logging malformed response for investigation.")
        raise


# ─────────────────────────────────────────────────────────────────────────────
# MAIN: Run all scenarios
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("DEMO 02: Multiple except Blocks — Cloud Metrics API")
    print("=" * 60)

    scenarios = ["success", "timeout", "503", "invalid_json"]

    for scenario in scenarios:
        try:
            fetch_cluster_metrics(scenario)
        except Exception as e:
            print(f"    [Caller caught re-raised exception]: {type(e).__name__}: {e}")

    print("\n[Done] Demo 02 complete.")
