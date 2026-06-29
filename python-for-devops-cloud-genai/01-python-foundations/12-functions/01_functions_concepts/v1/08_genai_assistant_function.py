# SECTION 8 DEMO — Generative AI Use Case
# NOTE: requires `pip install anthropic` and a valid ANTHROPIC_API_KEY environment
# variable to actually run. This demonstrates the PATTERN used in real AI apps.

import anthropic

def ask_ai_assistant(user_query, system_context="You are a helpful assistant."):
    ai_client = anthropic.Anthropic()
    response = ai_client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=system_context,
        messages=[
            {"role": "user", "content": user_query}
        ]
    )
    return response.content[0].text

# Same function — alag context — alag specialist
devops_answer = ask_ai_assistant(
    "What are the top 3 things to check before a production Kubernetes deployment?",
    system_context="You are a senior DevOps engineer with 10 years of Kubernetes experience."
)

finance_answer = ask_ai_assistant(
    "Explain this AWS bill: EC2 Rs.28000, RDS Rs.12000, Data Transfer Rs.5000",
    system_context="You are an AWS cost optimization specialist."
)

print(devops_answer)
print("---")
print(finance_answer)

# Ye hai agentic AI ka seedha seedha foundation.
# Real AI agents mein kya hota hai? Multiple functions hoti hain —
# search_web(), read_document(), summarize_text(), send_email() —
# aur ek orchestrator function decide karta hai kab kaunsi function call karni hai.
# Pura AI agent — Python functions ka ek well-organized collection hota hai.
