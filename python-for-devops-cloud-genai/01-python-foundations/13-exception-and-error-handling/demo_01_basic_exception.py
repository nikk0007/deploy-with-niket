"""
DEMO 01: Basic try / except
Topic: Exception & Error Handling in Python
Use Case: DevOps — Reading deployment config files

Run this file to see:
  1. What happens when a file exists (success path)
  2. What happens when a file is missing (exception path)
"""

import yaml
import json


# ─────────────────────────────────────────────────────────────────────────────
# EXAMPLE 1: Basic FileNotFoundError handling
# ─────────────────────────────────────────────────────────────────────────────

def load_yaml_config(filepath):
    """
    Loads a YAML deployment config file.
    Returns a dict on success, None on failure.
    """
    print(f"\n[*] Attempting to load config: {filepath}")
    try:
        with open(filepath, "r") as f:
            config = yaml.safe_load(f)
        print("[+] Config loaded successfully!")
        return config
    except FileNotFoundError:
        print(f"[-] Config file not found: {filepath}")
        print("    Falling back to default configuration.")
        return None
    except yaml.YAMLError as e:
        print(f"[-] Config file is malformed. YAML parse error: {e}")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# EXAMPLE 2: Handling JSON environment variable config
# ─────────────────────────────────────────────────────────────────────────────

import os

def get_service_config_from_env():
    """
    Reads a JSON config string from an environment variable.
    Common pattern in containerized/cloud environments.
    """
    print("\n[*] Reading SERVICE_CONFIG from environment variable...")
    raw_config = os.environ.get("SERVICE_CONFIG", None)

    if raw_config is None:
        print("[-] SERVICE_CONFIG env variable not set.")
        return {}

    try:
        config = json.loads(raw_config)
        print("[+] Parsed config from environment successfully.")
        return config
    except json.JSONDecodeError as e:
        print(f"[-] SERVICE_CONFIG contains invalid JSON: {e}")
        return {}


# ─────────────────────────────────────────────────────────────────────────────
# MAIN: Run both examples
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("DEMO 01: Basic try/except — Config File Loading")
    print("=" * 60)

    # Test 1a: File that doesn't exist
    result = load_yaml_config("/etc/deployment/nonexistent_config.yaml")
    print(f"    Result: {result}")

    # Test 1b: Create a temp yaml and read it successfully
    import tempfile
    sample_yaml = "environment: staging\nreplicas: 3\nimage: myapp:latest\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as tmp:
        tmp.write(sample_yaml)
        tmp_path = tmp.name

    result = load_yaml_config(tmp_path)
    print(f"    Result: {result}")
    os.remove(tmp_path)

    # Test 2: Environment variable config
    # With no env var set
    result = get_service_config_from_env()
    print(f"    Result: {result}")

    # With a valid env var
    os.environ["SERVICE_CONFIG"] = '{"region": "ap-south-1", "timeout": 30}'
    result = get_service_config_from_env()
    print(f"    Result: {result}")

    # With an invalid env var
    os.environ["SERVICE_CONFIG"] = "not-valid-json"
    result = get_service_config_from_env()
    print(f"    Result: {result}")

    print("\n[Done] Demo 01 complete.")
