# HOOK DEMO: The bug that crashed a production deployment at 2 AM
#
# A config file gave the replica count as "3" - a STRING, not an
# integer. One data type mistake, one production outage.

replica_count_from_config = "3"   # comes in as a string (e.g. from JSON/YAML)

print(type(replica_count_from_config))   # <class 'str'>

# WRONG: trying to do math with a string crashes the script
# desired_replicas = replica_count_from_config + 2
# TypeError: can only concatenate str (not "int") to str

# RIGHT: convert to the correct data type first
replica_count = int(replica_count_from_config)
print(type(replica_count))               # <class 'int'>

desired_replicas = replica_count + 2
print(f"Scaling from {replica_count} to {desired_replicas} replicas")

# Lesson: always know (and check) what data type you're actually
# working with - especially data coming from config files, APIs,
# or user input.
