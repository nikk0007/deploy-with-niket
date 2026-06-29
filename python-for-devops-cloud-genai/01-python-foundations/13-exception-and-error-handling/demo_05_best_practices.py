"""
DEMO 05: Production Best Practices — Logging Exceptions the Right Way
Topic: Exception & Error Handling in Python
Use Case: DevOps/Cloud — Terraform workspace automation script

Demonstrates:
  - logger.exception() vs logger.error() — key difference
  - Why `except: pass` is dangerous (silent failure demo)
  - Why bare `except Exception` everywhere is also bad
  - Correct re-raise pattern: `raise` vs `raise e`
  - Context managers and exception safety
"""

import logging
import traceback

# Set up structured logging (as you would in a real DevOps tool)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
)
logger = logging.getLogger("terraform_runner")


# ─────────────────────────────────────────────────────────────────────────────
# ANTI-PATTERN 1: Silent failure — the most dangerous pattern
# ─────────────────────────────────────────────────────────────────────────────

def bad_apply_silently(workspace):
    """
    WRONG: This swallows the error silently.
    Your pipeline continues as if nothing happened.
    Data integrity: destroyed. Debugging: impossible.
    """
    try:
        raise ConnectionError("Terraform backend unreachable: s3://state-bucket")
    except Exception:
        pass  # ← NEVER do this. This hides the error completely.

print("=" * 60)
print("ANTI-PATTERN 1: Silent failure (except: pass)")
print("=" * 60)
bad_apply_silently("prod")
print("[!] bad_apply_silently() returned with no output — error was completely hidden.\n")


# ─────────────────────────────────────────────────────────────────────────────
# ANTI-PATTERN 2: logger.error() — logs message but LOSES traceback
# ─────────────────────────────────────────────────────────────────────────────

def bad_apply_with_error_log(workspace):
    """
    WRONG: logger.error() only logs the message, not the stack trace.
    You see something went wrong but not WHERE or WHY.
    """
    try:
        raise RuntimeError("Terraform plan failed: resource conflict detected")
    except Exception as e:
        logger.error(f"Terraform apply failed: {e}")  # ← loses traceback

print("=" * 60)
print("ANTI-PATTERN 2: logger.error() — traceback is lost")
print("=" * 60)
bad_apply_with_error_log("staging")
print()


# ─────────────────────────────────────────────────────────────────────────────
# BEST PRACTICE: logger.exception() — logs message + full traceback
# ─────────────────────────────────────────────────────────────────────────────

def good_apply_with_exception_log(workspace):
    """
    CORRECT: logger.exception() logs the full traceback automatically.
    Works exactly like logger.error() but adds exc_info=True automatically.
    """
    try:
        raise RuntimeError("Terraform plan failed: resource conflict detected")
    except Exception as e:
        logger.exception(f"Terraform apply failed in workspace '{workspace}'")
        # ↑ Full traceback is included in the log output automatically
        raise  # re-raise so the caller knows the operation failed

print("=" * 60)
print("BEST PRACTICE: logger.exception() — full traceback included")
print("=" * 60)
try:
    good_apply_with_exception_log("prod")
except Exception:
    pass  # just to prevent script from stopping
print()


# ─────────────────────────────────────────────────────────────────────────────
# ANTI-PATTERN 3: Wrong re-raise — `raise e` vs `raise`
# ─────────────────────────────────────────────────────────────────────────────

def wrong_reraise():
    """
    WRONG: `raise e` resets the traceback to THIS line.
    The original line where the error occurred is lost.
    """
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.error("Something went wrong")
        raise e  # ← traceback now points HERE, not to `10 / 0`


def correct_reraise():
    """
    CORRECT: bare `raise` preserves the original traceback.
    The traceback points to `10 / 0` — the actual source of the error.
    """
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.error("Something went wrong")
        raise  # ← traceback preserved perfectly


print("=" * 60)
print("Re-raise comparison: raise e (wrong) vs raise (correct)")
print("=" * 60)

print("\n--- Wrong re-raise (`raise e`): ---")
try:
    wrong_reraise()
except ZeroDivisionError:
    traceback.print_exc()

print("\n--- Correct re-raise (bare `raise`): ---")
try:
    correct_reraise()
except ZeroDivisionError:
    traceback.print_exc()


# ─────────────────────────────────────────────────────────────────────────────
# BEST PRACTICE: Context manager for resource safety
# ─────────────────────────────────────────────────────────────────────────────

class TerraformLock:
    """
    Simulates a Terraform state lock.
    The `with` statement guarantees the lock is released even if an error occurs.
    """
    def __init__(self, workspace):
        self.workspace = workspace

    def __enter__(self):
        logger.info(f"[Lock] Acquiring state lock for workspace: {self.workspace}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info(f"[Lock] Releasing state lock for workspace: {self.workspace}")
        if exc_type:
            logger.warning(f"[Lock] Lock released after exception: {exc_type.__name__}")
        return False  # Don't suppress the exception — let it propagate

    def apply(self):
        logger.info(f"[Terraform] Running apply in workspace: {self.workspace}")
        raise RuntimeError("Simulated apply failure: state conflict")


print("\n" + "=" * 60)
print("BEST PRACTICE: Context Manager — guaranteed resource cleanup")
print("=" * 60)

try:
    with TerraformLock("production") as tf:
        tf.apply()  # This will raise — but the lock is still released!
except RuntimeError as e:
    logger.exception(f"Terraform run failed: {e}")

print("\n[Done] Demo 05 complete.")
