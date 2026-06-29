# DEMO 6 — Set Comprehension
# Real-world scenario: extracting unique cloud regions from deployment logs
# (logs often have duplicate region entries — one per deployment event)

deployment_logs = ["ap-south-1", "us-east-1", "ap-south-1", "eu-west-1", "us-east-1", "ap-south-1"]

unique_regions = {region for region in deployment_logs}

print(unique_regions)
# Output: {'ap-south-1', 'us-east-1', 'eu-west-1'}
# (set has no fixed order — that's expected)

# This is extremely common when parsing CloudTrail or access logs
# where you need to know "which regions were touched" without duplicates.
