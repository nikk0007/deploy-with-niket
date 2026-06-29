"""
DEMO 04: raise + Custom Exceptions
Topic: Exception & Error Handling in Python
Use Case: DevOps/Cloud — Infrastructure Provisioning Tool

Demonstrates:
  - raise: manually triggering exceptions to enforce rules
  - raise...from: exception chaining to preserve root cause
  - Custom exception hierarchy for a cloud provisioning tool
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# PART 1: Custom Exception Hierarchy
# ─────────────────────────────────────────────────────────────────────────────

class InfraProvisioningError(Exception):
    """Base class for all infrastructure provisioning errors.
    Catch this to handle any error from this module."""
    pass


class VMQuotaExceededError(InfraProvisioningError):
    """Raised when VM quota for a region would be exceeded."""
    def __init__(self, region, requested, current, limit):
        self.region = region
        self.requested = requested
        self.current = current
        self.limit = limit
        super().__init__(
            f"VM quota exceeded in region '{region}'. "
            f"Requested: {requested}, Current: {current}, Limit: {limit}. "
            f"Please request a quota increase or use a different region."
        )


class RegionUnavailableError(InfraProvisioningError):
    """Raised when the target region is not in the supported list."""
    pass


class NetworkConfigError(InfraProvisioningError):
    """Raised when a required network component (VPC, subnet) is missing."""
    pass


class StorageLimitError(InfraProvisioningError):
    """Raised when requested storage exceeds allowed maximum."""
    def __init__(self, requested_gb, max_gb):
        super().__init__(
            f"Storage request of {requested_gb} GB exceeds maximum allowed: {max_gb} GB."
        )


# ─────────────────────────────────────────────────────────────────────────────
# PART 2: Simulated Infrastructure State
# ─────────────────────────────────────────────────────────────────────────────

SUPPORTED_REGIONS = ["us-east-1", "eu-west-1", "ap-south-1"]

REGION_VM_STATE = {
    "us-east-1": {"current": 18, "limit": 20},
    "eu-west-1": {"current": 5,  "limit": 20},
    "ap-south-1": {"current": 19, "limit": 20},
}

AVAILABLE_VPCS = {
    "us-east-1": "vpc-abc123",
    "eu-west-1": "vpc-def456",
    # ap-south-1 intentionally missing to demo NetworkConfigError
}

MAX_STORAGE_GB = 1000


# ─────────────────────────────────────────────────────────────────────────────
# PART 3: Provisioning Functions with raise
# ─────────────────────────────────────────────────────────────────────────────

def validate_region(region):
    """Raises RegionUnavailableError for unsupported regions."""
    if region not in SUPPORTED_REGIONS:
        raise RegionUnavailableError(
            f"Region '{region}' is not supported by this tool. "
            f"Supported regions: {SUPPORTED_REGIONS}"
        )


def validate_vm_quota(region, count):
    """Raises VMQuotaExceededError if the requested VM count would breach the limit."""
    state = REGION_VM_STATE.get(region, {})
    current = state.get("current", 0)
    limit = state.get("limit", 20)
    if current + count > limit:
        raise VMQuotaExceededError(
            region=region,
            requested=count,
            current=current,
            limit=limit
        )


def validate_network(region):
    """Raises NetworkConfigError if no VPC is configured for the region."""
    if region not in AVAILABLE_VPCS:
        raise NetworkConfigError(
            f"No VPC configured for region '{region}'. "
            f"Please create a VPC before provisioning instances."
        )


def validate_storage(storage_gb):
    """Raises StorageLimitError for oversized storage requests."""
    if storage_gb > MAX_STORAGE_GB:
        raise StorageLimitError(storage_gb, MAX_STORAGE_GB)


# ─────────────────────────────────────────────────────────────────────────────
# PART 4: Exception Chaining Demo — raise...from
# ─────────────────────────────────────────────────────────────────────────────

class InternalAPIError(Exception):
    """Simulates a low-level cloud API SDK error."""
    pass


def call_cloud_api(region):
    """Simulates a low-level API call that might throw a generic SDK error."""
    if region == "eu-west-1":
        raise InternalAPIError("Cloud SDK: Connection refused on endpoint https://eu-west-1.internal:8443")


def provision_vm(region, count=1, storage_gb=100):
    """
    Main provisioning function.
    Validates all constraints before attempting the actual API call.
    Uses raise...from for exception chaining on low-level API errors.
    """
    logger.info(f"Provisioning {count} VM(s) in {region} with {storage_gb} GB storage...")

    # Step 1: Validate inputs early (fail fast)
    validate_region(region)
    validate_vm_quota(region, count)
    validate_network(region)
    validate_storage(storage_gb)

    # Step 2: Call the actual cloud API (with chaining)
    try:
        call_cloud_api(region)
    except InternalAPIError as e:
        raise InfraProvisioningError(
            f"VM provisioning failed in '{region}' due to a cloud API error."
        ) from e  # ← preserves the original InternalAPIError traceback

    logger.info(f"[✓] Successfully provisioned {count} VM(s) in {region}.")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN: Test all error scenarios
# ─────────────────────────────────────────────────────────────────────────────

def run_scenario(description, region, count=1, storage_gb=100):
    print(f"\n--- {description} ---")
    try:
        provision_vm(region=region, count=count, storage_gb=storage_gb)
    except VMQuotaExceededError as e:
        logger.error(f"[QUOTA] {e}")
        logger.info("Action: Requesting quota increase from cloud provider.")
    except RegionUnavailableError as e:
        logger.error(f"[REGION] {e}")
    except NetworkConfigError as e:
        logger.error(f"[NETWORK] {e}")
        logger.info("Action: Triggering VPC setup workflow.")
    except StorageLimitError as e:
        logger.error(f"[STORAGE] {e}")
    except InfraProvisioningError as e:
        logger.error(f"[INFRA] {e}")
        if e.__cause__:
            logger.error(f"  Root cause: {e.__cause__}")  # shows chained exception


if __name__ == "__main__":
    print("=" * 60)
    print("DEMO 04: raise + Custom Exceptions — Infra Provisioning")
    print("=" * 60)

    run_scenario("SUCCESS: us-east-1, 1 VM, 100 GB",       region="us-east-1", count=1,  storage_gb=100)
    run_scenario("FAIL: Unsupported region",                region="sa-east-1", count=1,  storage_gb=100)
    run_scenario("FAIL: VM quota exceeded (ap-south-1)",    region="ap-south-1", count=5, storage_gb=100)
    run_scenario("FAIL: No VPC configured (ap-south-1)",    region="ap-south-1", count=1, storage_gb=100)
    run_scenario("FAIL: Storage limit exceeded",            region="us-east-1", count=1,  storage_gb=1500)
    run_scenario("FAIL: API error with exception chaining", region="eu-west-1", count=1,  storage_gb=100)

    print("\n[Done] Demo 04 complete.")
