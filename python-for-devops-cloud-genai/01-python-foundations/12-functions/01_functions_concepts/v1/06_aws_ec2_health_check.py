# SECTION 7 DEMO — Use Case 1: AWS EC2 Health Check
# NOTE: requires `pip install boto3` and valid AWS credentials configured to actually run.
# This demonstrates the PATTERN — code structure is real and production-accurate.

import boto3

def check_ec2_health(instance_id, region="ap-south-1"):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instance_status(InstanceIds=[instance_id])
    statuses = response["InstanceStatuses"]
    if not statuses:
        return f"Instance {instance_id}: No status — may be stopped"
    state = statuses[0]["InstanceState"]["Name"]
    system_status = statuses[0]["SystemStatus"]["Status"]
    return f"Instance {instance_id} | State: {state} | System: {system_status}"

# Ek function — kisi bhi instance ke liye
print(check_ec2_health("i-0abc123def456"))
print(check_ec2_health("i-0xyz789uvw012", region="us-east-1"))

# Ye function tumhare monitoring script mein call ho sakta hai.
# Lambda mein ho sakta hai. CI/CD pipeline mein ho sakta hai.
# Ek jagah likha — har jagah kaam aata hai.
