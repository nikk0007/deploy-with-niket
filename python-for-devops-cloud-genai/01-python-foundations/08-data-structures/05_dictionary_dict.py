# Section 5: DICTIONARY (dict)
# Python's "JSON" - used for AWS API responses, Kubernetes configs,
# CI/CD environment variable maps, and more.

server_config: dict = {
    "hostname": "prod-api-01",
    "region": "ap-south-1",
    "port": 8080,
    "replicas": 3
}

print(server_config)

# Keys are unique. Values can be anything (str, int, list, dict, etc.)

# ---------------------------------------------------------------
# Accessing values
# ---------------------------------------------------------------
print(server_config["region"])   # "ap-south-1"
print(server_config["port"])     # 8080

# Direct bracket access on a missing key raises KeyError and crashes
# the program. Uncomment to see it:
# print(server_config["timeout"])   # KeyError: 'timeout'

# Safe way - use .get() with a default value
print(server_config.get("timeout", 30))     # 30 (key doesn't exist)
print(server_config.get("env", "staging"))  # "staging" (key doesn't exist)

# ---------------------------------------------------------------
# Common operations
# ---------------------------------------------------------------
server_config["replicas"] = 5              # update existing key
server_config["env"] = "production"        # add a new key
print(server_config)

del server_config["port"]                  # delete a key
print(server_config)

removed_value = server_config.pop("region")  # remove and return
print("Removed:", removed_value)
print(server_config)

print(server_config.keys())     # all keys
print(server_config.values())   # all values
print(server_config.items())    # all key-value pairs (as tuples)

server_config.update({"replicas": 10, "timeout": 60})   # bulk update
print(server_config)

# ---------------------------------------------------------------
# Nested dictionary - real-world API/config structure
# ---------------------------------------------------------------
k8s_deployment = {
    "name": "payment-api",
    "replicas": 3,
    "containers": [
        {"name": "api", "image": "payment-api:v2.1", "port": 8080}
    ],
    "labels": {"team": "payments", "env": "prod"}
}

print(k8s_deployment["containers"][0]["image"])   # payment-api:v2.1
print(k8s_deployment["labels"]["team"])           # payments
