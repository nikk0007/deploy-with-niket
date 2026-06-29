# ============================================================
# 09_genai_usecase.py
# Topic: Real GenAI Use Case — AI Specialist Dispatcher
# ============================================================

# Every AI application — chatbot, code reviewer, document summarizer,
# DevOps assistant — is built on the same core pattern:
#
#   One function wraps the AI API call.
#   The system_context argument swaps the "specialist" persona.
#   Call the same function with different context → different expert.
#
# This is the foundation of what people call "AI agents."
#
# NOTE: This file simulates the AI responses so it runs without an API key.
#       The real API call is shown in comments — swap it in when you are ready.

# ---- Simulated AI responses ----

SIMULATED_RESPONSES = {
    "devops":   "[DevOps AI] Top 3 pre-deployment checks: (1) Run all unit and integration tests. "
                "(2) Verify resource quotas and limits are set on all pods. "
                "(3) Confirm a rollback plan and tested rollback procedure exists.",

    "cost":     "[Cost AI] Bill breakdown — EC2 Rs.28,000 is your largest line item; "
                "consider Reserved Instances for a 30-40% saving. "
                "RDS Rs.12,000: check if you can right-size to a smaller instance class. "
                "Data Transfer Rs.5,000: review if S3 Transfer Acceleration is enabled unnecessarily.",

    "security": "[Security AI] Critical findings: (1) IAM role has wildcard (*) permissions — "
                "scope these down immediately. (2) S3 bucket policy allows public read — "
                "remove unless intentional. (3) No MFA enforced on root account.",

    "incident": "[SRE AI] Root cause analysis: memory leak in the payment-service container "
                "caused OOM kill at 03:42 UTC. Recommended actions: (1) Add memory limits. "
                "(2) Deploy v2.1.5 hotfix. (3) Add OOM alert to Grafana dashboard.",
}


# ---- The core function — one function, many specialists ----

def ask_ai_specialist(user_query, specialist_type="devops"):
    """
    Send a query to an AI specialist and return the response.

    user_query      : The question or task for the AI.
    specialist_type : One of 'devops', 'cost', 'security', 'incident'.
    Returns         : The AI's response as a string.

    In production, replace the simulated response below with:

        import anthropic
        SYSTEM_CONTEXTS = {
            "devops":   "You are a senior DevOps engineer with 10 years of Kubernetes experience.",
            "cost":     "You are an AWS cost optimization specialist.",
            "security": "You are a cloud security engineer specialising in AWS IAM and compliance.",
            "incident": "You are a senior SRE leading a post-incident root cause analysis.",
        }
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_CONTEXTS[specialist_type],
            messages=[{"role": "user", "content": user_query}]
        )
        return response.content[0].text
    """
    return SIMULATED_RESPONSES.get(specialist_type, "[AI] No specialist found for that type.")


# ---- Same function call — different specialist each time ----

print("=" * 60)
print("  AI Specialist Dispatcher — Demo")
print("=" * 60 + "\n")

# Specialist 1: DevOps Engineer
query_1 = "What are the top 3 things to check before a production Kubernetes deployment?"
print(f"Query   : {query_1}")
print(f"Response: {ask_ai_specialist(query_1, specialist_type='devops')}")
print()

# Specialist 2: AWS Cost Analyst
query_2 = "Explain this AWS bill: EC2 Rs.28000, RDS Rs.12000, Data Transfer Rs.5000"
print(f"Query   : {query_2}")
print(f"Response: {ask_ai_specialist(query_2, specialist_type='cost')}")
print()

# Specialist 3: Security Engineer
query_3 = "Review these IAM policies and S3 bucket permissions for security issues."
print(f"Query   : {query_3}")
print(f"Response: {ask_ai_specialist(query_3, specialist_type='security')}")
print()

# Specialist 4: SRE Incident Analyst
query_4 = "Our payment service went down at 3am. Help me write the root cause analysis."
print(f"Query   : {query_4}")
print(f"Response: {ask_ai_specialist(query_4, specialist_type='incident')}")
print()

# ---- The bigger picture ----
print("=" * 60)
print("""
What just happened?
  One function. Four different AI specialists.
  Only the system_context changes — the function stays the same.

This is the foundation of AI agents:
  search_web()         → searches the internet
  read_document()      → parses a PDF or file
  summarize_text()     → condenses long content
  send_alert()         → fires a Slack or email notification
  ask_ai_specialist()  → routes to the right AI persona

An AI agent is a Python program that decides
WHICH functions to call and WHEN.
The functions themselves are what you are learning right now.
""")
