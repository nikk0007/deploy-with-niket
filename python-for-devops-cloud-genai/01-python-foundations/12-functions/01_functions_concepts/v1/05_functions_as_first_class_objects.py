# SECTION 6 DEMO — Functions as First-Class Objects
# Real-world scenario: validating config keys before a deployment proceeds

def validate_api_key(key):
    return len(key) == 20 and key.startswith("sk-")

# Function ko variable mein store kiya — parentheses nahi, calling nahi, storing hai
checker = validate_api_key

print(checker("sk-1234567890abcdefgh"))   # True (20 chars, starts with sk-)
print(checker("invalid-key"))             # False


# ── Function ko argument ki tarah pass karna ──

def process_config_entry(entry_name, validation_fn):
    if validation_fn(entry_name):
        print(f"Config '{entry_name}' — Valid. Deployment can proceed.")
    else:
        print(f"Config '{entry_name}' — Invalid. Deployment blocked.")

def is_valid_region_code(region):
    return region in ["ap-south-1", "us-east-1", "eu-west-1"]

def is_valid_port(port_str):
    return port_str.isdigit() and 1024 <= int(port_str) <= 65535

# Same process function — alag alag validation functions ke saath
process_config_entry("ap-south-1", is_valid_region_code)
process_config_entry("8080", is_valid_port)
process_config_entry("invalid-region", is_valid_region_code)

# Ye pattern production mein kaafi use hota hai:
# Web frameworks mein middleware, data pipelines mein transformations,
# testing frameworks mein — har jagah functions ko objects ki tarah treat kiya jaata hai.
