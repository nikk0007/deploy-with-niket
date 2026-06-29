"""
DEMO 02: open/close vs try/finally vs with Statement
Topic: File Handling in Python
Use Case: DevOps — Terraform backend config processing

Demonstrates:
  - The risky pattern: open() without close()
  - The safer pattern: try/finally
  - The modern pattern: with statement
  - Behind the scene: __enter__ and __exit__ dunders
"""

import os
import tempfile

DEMO_DIR = tempfile.mkdtemp(prefix="python_fh_demo02_")


def demo_path(name):
    return os.path.join(DEMO_DIR, name)


# Create sample config files for the demo
BACKEND_CONF_CONTENT = """\
bucket         = "terraform-state-prod"
key            = "infra/prod/terraform.tfstate"
region         = "ap-south-1"
dynamodb_table = "terraform-lock"
encrypt        = true
"""

BACKEND_CONF = demo_path("backend.conf")
with open(BACKEND_CONF, "w") as f:
    f.write(BACKEND_CONF_CONTENT)


# ─────────────────────────────────────────────────────────────────────────────
# PATTERN 1: Risky — open() without guaranteed close()
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("PATTERN 1: Risky — open() without guaranteed close()")
print("=" * 60)

def parse_backend_config_risky(path):
    """
    Reads a Terraform backend config.
    PROBLEM: If parse_config() raises an exception,
    file.close() is never called → file handle leak.
    """
    file = open(path, "r")
    content = file.read()
    # Imagine parse_config() raises an unexpected ValueError here.
    # file.close() below will NEVER run.
    config = {}
    for line in content.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip().strip('"')
    file.close()  # ← NOT guaranteed to run if anything above raises
    return config

try:
    config = parse_backend_config_risky(BACKEND_CONF)
    print("[OK] Config loaded (risky pattern):", config)
except Exception as e:
    print(f"[ERROR] {e}")

print("⚠️  If an exception had occurred before file.close(), the file handle would leak.")


# ─────────────────────────────────────────────────────────────────────────────
# PATTERN 2: Safer — try/finally guarantees close()
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("PATTERN 2: Safer — try/finally guarantees close()")
print("=" * 60)

def parse_backend_config_try_finally(path):
    """
    try/finally guarantees file.close() even if an exception occurs.
    Correct but verbose.
    """
    file = None
    try:
        file = open(path, "r")
        content = file.read()
        config = {}
        for line in content.splitlines():
            if "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip().strip('"')
        return config
    except FileNotFoundError:
        print(f"  [FileNotFoundError] Config not found: {path}")
        return {}
    except PermissionError:
        print(f"  [PermissionError] Cannot read: {path} — check file permissions")
        return {}
    finally:
        if file:
            file.close()
            print("  [finally] file.close() called — file handle released.")

config = parse_backend_config_try_finally(BACKEND_CONF)
print(f"[OK] Config loaded (try/finally): {config}")

# Also test with a missing file
config = parse_backend_config_try_finally(demo_path("nonexistent.conf"))
print(f"[Missing file result]: {config}")


# ─────────────────────────────────────────────────────────────────────────────
# PATTERN 3: Modern — with statement (recommended)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("PATTERN 3: Modern — with statement (recommended for all production code)")
print("=" * 60)

def parse_backend_config_with(path):
    """
    The with statement automatically calls __exit__() when the block ends.
    File is always closed — crash or not. Clean, short, production-safe.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # File is already closed here — even if f.read() raised an exception
        config = {}
        for line in content.splitlines():
            if "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip().strip('"')
        return config
    except FileNotFoundError:
        print(f"  [FileNotFoundError] Config not found: {path}")
        return {}
    except PermissionError:
        print(f"  [PermissionError] Cannot read: {path}")
        return {}

config = parse_backend_config_with(BACKEND_CONF)
print(f"[OK] Config loaded (with statement): {config}")


# ─────────────────────────────────────────────────────────────────────────────
# Opening multiple files at once with a single with statement
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("BONUS: Multiple files in a single with statement")
print("=" * 60)

pipeline_log = demo_path("pipeline.log")

with open(BACKEND_CONF, "r") as cfg, open(pipeline_log, "a") as log:
    config_content = cfg.read()
    log.write(f"[Pipeline] Loaded backend config ({len(config_content)} bytes)\n")
    log.write(f"[Pipeline] Target bucket: terraform-state-prod\n")

print("[OK] Config read and log entry written — both files closed automatically.")

with open(pipeline_log, "r") as f:
    print("[Log file content]:")
    print(f.read())


# ─────────────────────────────────────────────────────────────────────────────
# Behind the scene: __enter__ and __exit__
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("BEHIND THE SCENE: __enter__ and __exit__ dunders")
print("=" * 60)

f = open(BACKEND_CONF, "r")
print(f"Does file object have __enter__? {hasattr(f, '__enter__')}")
print(f"Does file object have __exit__?  {hasattr(f, '__exit__')}")
print()

# Calling dunders manually to show what `with` does automatically
file_ref = f.__enter__()
print(f"After __enter__(): file is open → f.closed = {f.closed}")

f.__exit__(None, None, None)
print(f"After __exit__():  file is closed → f.closed = {f.closed}")

print()
print("The `with` statement calls these two dunders for you — automatically.")
print("Any object that implements __enter__ and __exit__ can be used with `with`.")
print("This is the Context Manager Protocol.")

import shutil
shutil.rmtree(DEMO_DIR)
print(f"\n[Cleanup] Removed demo directory.")
print("[Done] Demo 02 complete.")
