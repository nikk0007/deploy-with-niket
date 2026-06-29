# ============================================================
# SECTION 8 — DECORATOR FUNCTIONS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

import time
import functools

print("=" * 55)
print("  DECORATOR FUNCTIONS — DevOps & GenAI Examples")
print("=" * 55)


# ---- Decorator anatomy ----

print("\n📌 Decorator anatomy — bare bones:")

def decorator_name(func):
    @functools.wraps(func)           # Preserves original function metadata
    def wrapper(*args, **kwargs):
        print("  [Before] Extra behavior added here")
        result = func(*args, **kwargs)
        print("  [After]  Extra behavior added here")
        return result
    return wrapper

@decorator_name
def my_function():
    print("  [Inside] Original function running")

my_function()


# ---- Timer Decorator ----

def timer(func):
    """Decorator: Measures and prints execution time of any function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start   = time.time()
        result  = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  ⏱️  [TIMER] {func.__name__}() completed in {elapsed:.3f}s")
        return result
    return wrapper


@timer
def fetch_kubernetes_pods(namespace):
    """Simulates fetching pods from Kubernetes API."""
    time.sleep(0.5)   # Simulating real API latency
    return ["api-pod-1", "db-pod-1", "cache-pod-1"]


@timer
def fetch_ec2_instances(region):
    """Simulates fetching EC2 instance list from AWS."""
    time.sleep(0.3)
    return ["i-001", "i-002", "i-003"]


print("\n📌 @timer decorator — auto execution time tracking:")
pods      = fetch_kubernetes_pods("production")
instances = fetch_ec2_instances("ap-south-1")
print(f"  Pods:      {pods}")
print(f"  Instances: {instances}")


# ---- Retry Decorator (parameterized) ----

def retry(max_attempts=3, delay=1):
    """
    Parameterized decorator: Retries a function on failure.
    Production-grade pattern for flaky cloud APIs.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  ⚠️  Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        print(f"  ⏳ Waiting {delay}s before retry...")
                        time.sleep(delay)
            raise Exception(f"❌ {func.__name__}() failed after {max_attempts} attempts")
        return wrapper
    return decorator


@retry(max_attempts=3, delay=1)
def call_openai_api(prompt):
    """Simulates a flaky OpenAI API call (rate limited)."""
    raise ConnectionError("Rate limited — 429 Too Many Requests")


print("\n📌 @retry decorator — automatic retry on failure:")
try:
    call_openai_api("Summarize this CloudWatch log")
except Exception as e:
    print(f"  {e}")


# ---- Logger Decorator ----

def log_calls(func):
    """Decorator: Logs every function call with its arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  📝 CALL: {func.__name__}() | args={args} | kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  📝 RETURN: {func.__name__}() → {result}")
        return result
    return wrapper


@log_calls
def scale_deployment(deployment_name, replicas):
    return f"Scaled {deployment_name} to {replicas} replicas"


print("\n📌 @log_calls decorator — automatic call logging:")
scale_deployment("payment-service", 5)
scale_deployment("auth-service", 3)


# ---- Stacking Decorators ----

print("\n📌 Stacking decorators — @timer + @log_calls together:")

@timer
@log_calls
def create_s3_bucket(bucket_name, region="ap-south-1"):
    time.sleep(0.1)   # Simulating API call
    return f"s3://{bucket_name}"

create_s3_bucket("my-devops-artifacts", region="us-east-1")

print("\n✅ Real-world decorators you already use:")
print("   @app.get('/users')     ← FastAPI")
print("   @app.post('/deploy')   ← FastAPI")
print("   @pytest.fixture        ← Testing")
print("   @staticmethod          ← Python classes")
