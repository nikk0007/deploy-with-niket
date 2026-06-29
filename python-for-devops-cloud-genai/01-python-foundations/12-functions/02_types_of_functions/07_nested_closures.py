# ============================================================
# SECTION 7 — NESTED FUNCTIONS & CLOSURES
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

print("=" * 55)
print("  NESTED FUNCTIONS & CLOSURES")
print("=" * 55)

# ---- Nested function: Microservice Logger ----

def create_service_logger(service_name):
    """
    Outer function — creates a logger for a specific service.
    Inner function 'log' is defined inside.
    """
    def log(message, level="INFO"):   # ← Inner (nested) function
        print(f"  [{level}] [{service_name}] {message}")
    return log   # ← Returns the inner function


print("\n📌 Nested function — create_service_logger():")
k8s_logger     = create_service_logger("k8s-controller")
payment_logger = create_service_logger("payment-service")
auth_logger    = create_service_logger("auth-service")

k8s_logger("Pod scheduled successfully")
k8s_logger("OOMKilled — pod restarting", "ERROR")
payment_logger("Transaction processed — ₹4,999")
payment_logger("Payment gateway timeout", "WARN")
auth_logger("JWT token issued")


# ---- What is a Closure? ----

print("\n📌 CLOSURE demo — outer function exits, but inner still remembers:")
print("  k8s_logger still 'remembers' service_name = 'k8s-controller'")
print("  even though create_service_logger() has already finished running!")
k8s_logger("This proves closure is working ✅")


# ---- AWS Client Factory — Closure in action ----

def aws_client_factory(region):
    """
    Closure: 'region' is captured by the inner function.
    Each factory call creates a region-specific client getter.
    """
    def get_client(service):
        print(f"  Creating {service} client for region: {region}")
        return f"{service}-client-{region}"
    return get_client


print("\n📌 aws_client_factory() — Closure for AWS region config:")
mumbai_clients   = aws_client_factory("ap-south-1")
virginia_clients = aws_client_factory("us-east-1")

print("\n  Mumbai region clients:")
mumbai_clients("ec2")
mumbai_clients("s3")
mumbai_clients("lambda")

print("\n  Virginia region clients:")
virginia_clients("ec2")
virginia_clients("rds")


# ---- Closure as a counter (stateful without a class) ----

def make_api_counter(service_name):
    """
    A closure that maintains call count — stateful, without a class.
    Useful for rate-limiting tracking per service.
    """
    count = 0   # This variable is "enclosed" by the inner function

    def call(endpoint):
        nonlocal count
        count += 1
        print(f"  [{service_name}] Call #{count} → {endpoint}")
        return count
    return call


print("\n📌 Stateful closure — make_api_counter():")
openai_call  = make_api_counter("OpenAI")
aws_call     = make_api_counter("AWS-SDK")

openai_call("/v1/chat/completions")
openai_call("/v1/embeddings")
openai_call("/v1/chat/completions")

aws_call("ec2:DescribeInstances")
aws_call("s3:ListBuckets")

print("\n✅ CLOSURE = Inner function + Outer function ke variables ki memory")
print("   Outer function khatam ho jaye — inner function phir bhi yaad rakhta hai!")
