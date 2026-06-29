"""
DEMO 03: else and finally blocks
Topic: Exception & Error Handling in Python
Use Case: Cloud — Uploading pipeline output to object storage (e.g., AWS S3)

Demonstrates:
  - else   → runs only on success (trigger downstream pipeline)
  - finally → runs always (cleanup temp files, close resources)
"""

import os
import tempfile
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# Mock S3 uploader (no AWS credentials needed for demo)
# ─────────────────────────────────────────────────────────────────────────────

class MockS3:
    class exceptions:
        class NoCredentialsError(Exception):
            pass
        class ClientError(Exception):
            def __init__(self, code):
                self.response = {"Error": {"Code": code}}
                super().__init__(f"ClientError: {code}")

    def upload_file(self, local_path, bucket, key, fail_with=None):
        """Simulates an S3 upload. Pass fail_with to simulate errors."""
        if fail_with == "no_credentials":
            raise MockS3.exceptions.NoCredentialsError("No AWS credentials found.")
        elif fail_with == "access_denied":
            raise MockS3.exceptions.ClientError("AccessDenied")
        elif fail_with == "no_such_bucket":
            raise MockS3.exceptions.ClientError("NoSuchBucket")
        # Success: do nothing (simulates successful upload)
        logger.info(f"[S3 Mock] Uploaded '{local_path}' → s3://{bucket}/{key}")


s3 = MockS3()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN FUNCTION: upload_pipeline_output
# ─────────────────────────────────────────────────────────────────────────────

def trigger_downstream_pipeline(bucket, key):
    """Simulates notifying the next stage of the data pipeline."""
    logger.info(f"[Pipeline] Downstream pipeline triggered for: s3://{bucket}/{key}")


def upload_pipeline_output(local_path, bucket, key, fail_with=None):
    """
    Uploads a processed data file to cloud object storage.

    else block  → notifies downstream pipeline ONLY on successful upload
    finally block → cleans up local temp file ALWAYS, no matter what
    """
    logger.info(f"Starting upload: {local_path} → s3://{bucket}/{key}")

    try:
        s3.upload_file(local_path, bucket, key, fail_with=fail_with)

    except MockS3.exceptions.NoCredentialsError:
        logger.error("AWS credentials not configured. Check IAM role or env variables.")
        raise

    except MockS3.exceptions.ClientError as e:
        error_code = e.response["Error"]["Code"]
        logger.error(f"S3 upload failed. AWS error code: {error_code}")
        raise

    else:
        # This block runs ONLY if no exception occurred in try
        logger.info("Upload confirmed successful.")
        trigger_downstream_pipeline(bucket, key)

    finally:
        # This block ALWAYS runs — whether upload succeeded or failed
        if os.path.exists(local_path):
            os.remove(local_path)
            logger.info(f"Temp file cleaned up: {local_path}")
        else:
            logger.warning(f"Temp file already gone: {local_path}")


# ─────────────────────────────────────────────────────────────────────────────
# Helper: create a dummy temp file to simulate pipeline output
# ─────────────────────────────────────────────────────────────────────────────

def create_temp_output_file():
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False,
        prefix="pipeline_output_"
    )
    tmp.write("instance_id,region,status\ni-0abc123,ap-south-1,running\n")
    tmp.close()
    return tmp.name


# ─────────────────────────────────────────────────────────────────────────────
# MAIN: Run all scenarios
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("DEMO 03: else and finally — S3 Upload Pattern")
    print("=" * 60)

    scenarios = [
        ("success",        "Successful upload → else runs, finally runs"),
        ("no_credentials", "No credentials → except runs, finally runs, else SKIPPED"),
        ("access_denied",  "Access denied  → except runs, finally runs, else SKIPPED"),
    ]

    for fail_with, description in scenarios:
        print(f"\n--- Scenario: {description} ---")
        tmp_path = create_temp_output_file()
        print(f"    Temp file created: {tmp_path}")
        print(f"    File exists before upload: {os.path.exists(tmp_path)}")

        try:
            upload_pipeline_output(
                local_path=tmp_path,
                bucket="prod-data-lake",
                key=f"outputs/{os.path.basename(tmp_path)}",
                fail_with=None if fail_with == "success" else fail_with
            )
        except Exception as e:
            print(f"    [Caller] Exception propagated: {type(e).__name__}: {e}")

        print(f"    File exists AFTER upload attempt: {os.path.exists(tmp_path)}")
        # Should always be False — finally block always cleans up

    print("\n[Done] Demo 03 complete.")
