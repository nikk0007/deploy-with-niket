# SECTION 4 DEMO — Default Parameters and Keyword Arguments

def send_alert(message, recipient="ops-team@company.com", priority="normal"):
    print(f"[{priority.upper()}] To: {recipient} | Message: {message}")

# Sab teen diye
send_alert("Database CPU at 95%", "dba-team@company.com", "critical")

# Sirf message diya — baaki default
send_alert("Nightly backup completed successfully")

# Output:
# [CRITICAL] To: dba-team@company.com | Message: Database CPU at 95%
# [NORMAL] To: ops-team@company.com | Message: Nightly backup completed successfully


# ── Keyword Arguments — naam lekar bulao ──
# Order nahi pata? Naam se do — safe hai

send_alert(
    priority="critical",
    message="Payment gateway timeout",
    recipient="payments-team@company.com"
)


# ── IMPORTANT RULE ──
# Default parameters hamesha non-default ke baad aane chahiye.

def deploy_service(service_name, replicas, region="ap-south-1"):   # correct
    print(f"Deploying {service_name} with {replicas} replicas in {region}")

deploy_service("payment-service", 3)
deploy_service("auth-service", 5, region="us-east-1")

# def deploy_service(region="ap-south-1", service_name, replicas):   # SyntaxError!
# Python position se match karta hai.
# Agar default pehle ho — Python confuse ho jaayega ki kaunsa argument kiske liye hai.
