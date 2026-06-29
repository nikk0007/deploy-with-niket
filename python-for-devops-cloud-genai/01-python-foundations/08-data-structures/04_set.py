# Section 4: SET (set)
# Scenario: deduplicating IPs, and comparing deployed vs allowed regions.

deployed_regions: set = {"ap-south-1", "us-east-1", "eu-west-1"}
allowed_regions: set = {"ap-south-1", "us-east-1", "ap-southeast-1"}

print(deployed_regions)
print(allowed_regions)

# Sets only store UNIQUE values - duplicates are silently dropped.
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)   # {1, 2, 3}

# ---------------------------------------------------------------
# Set operations - real power
# ---------------------------------------------------------------
print(deployed_regions | allowed_regions)   # union        - all regions
print(deployed_regions & allowed_regions)   # intersection - in both
print(deployed_regions - allowed_regions)   # difference   - deployed but NOT allowed
print(deployed_regions ^ allowed_regions)   # symmetric    - in only one

# This single line of set math replaces what would otherwise be
# a 10-15 line loop with manual comparisons.

# ---------------------------------------------------------------
# Real use case: find unpatched servers
# ---------------------------------------------------------------
patched = {"server-01", "server-02", "server-03"}
all_servers = {"server-01", "server-02", "server-03", "server-04", "server-05"}

unpatched = all_servers - patched
print(unpatched)   # {'server-04', 'server-05'}

# ---------------------------------------------------------------
# Other real use cases (for reference):
# - Unique IP addresses from a log file
# - New alerts vs already-seen alerts in monitoring
# - Discarding duplicate LLM responses in a GenAI pipeline
# ---------------------------------------------------------------
