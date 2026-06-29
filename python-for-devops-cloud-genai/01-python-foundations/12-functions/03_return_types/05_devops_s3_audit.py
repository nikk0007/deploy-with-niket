# Section 7 - Use Case 1: AWS S3 Bucket Compliance Audit
#
# This file has two parts:
#   1) The REAL production version using boto3 (requires AWS credentials
#      and an actual bucket - shown for teaching, not meant to run live
#      without AWS access).
#   2) A SIMULATED version with the exact same return signature, so you
#      can run it live during the demo without needing AWS credentials.

# ---------------------------------------------------------------
# 1) REAL VERSION (uncomment to use with real AWS credentials)
# ---------------------------------------------------------------
#
# import boto3
#
# def audit_s3_bucket(bucket_name):
#     s3 = boto3.client("s3")
#     try:
#         location = s3.get_bucket_location(Bucket=bucket_name)
#         region = location["LocationConstraint"] or "us-east-1"
#
#         versioning = s3.get_bucket_versioning(Bucket=bucket_name)
#         versioning_status = versioning.get("Status", "Disabled")
#
#         encryption = s3.get_bucket_encryption(Bucket=bucket_name)
#         is_encrypted = bool(encryption.get("ServerSideEncryptionConfiguration"))
#
#         return region, versioning_status, is_encrypted, "audit_success"
#
#     except Exception as e:
#         return None, None, None, f"audit_failed: {str(e)}"


# ---------------------------------------------------------------
# 2) SIMULATED VERSION - same return signature, runs anywhere
# ---------------------------------------------------------------
def audit_s3_bucket(bucket_name):
    """Simulated S3 bucket audit for live demo purposes."""
    fake_bucket_data = {
        "prod-data-bucket-2024": {
            "region": "ap-south-1",
            "versioning": "Enabled",
            "encrypted": True
        },
        "legacy-backup-bucket": {
            "region": "us-east-1",
            "versioning": "Disabled",
            "encrypted": False
        }
    }

    if bucket_name not in fake_bucket_data:
        return None, None, None, "audit_failed: bucket not found"

    info = fake_bucket_data[bucket_name]
    return info["region"], info["versioning"], info["encrypted"], "audit_success"


region, versioning, encrypted, audit_status = audit_s3_bucket("prod-data-bucket-2024")

if audit_status == "audit_success":
    print(f"Region        : {region}")
    print(f"Versioning    : {versioning}")
    print(f"Encrypted     : {encrypted}")
    print(f"Compliance    : {'PASS' if encrypted and versioning == 'Enabled' else 'FAIL'}")
else:
    print(f"Audit error   : {audit_status}")

print()
print("--- Auditing a non-compliant bucket ---")
region, versioning, encrypted, audit_status = audit_s3_bucket("legacy-backup-bucket")
if audit_status == "audit_success":
    print(f"Region        : {region}")
    print(f"Versioning    : {versioning}")
    print(f"Encrypted     : {encrypted}")
    print(f"Compliance    : {'PASS' if encrypted and versioning == 'Enabled' else 'FAIL'}")
else:
    print(f"Audit error   : {audit_status}")
