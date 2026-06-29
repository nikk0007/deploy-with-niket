# Section 8: Generative AI Use Case - returning the AI answer
# PLUS production-relevant metadata (tokens, latency, stop reason).
#
# Two versions again: the REAL one calling the Anthropic API (needs
# an API key and the anthropic package), and a SIMULATED one with the
# identical return signature for a live demo without API access.

# ---------------------------------------------------------------
# 1) REAL VERSION (uncomment to use with a real Anthropic API key)
# ---------------------------------------------------------------
#
# import anthropic
# import time
#
# def call_ai_with_metadata(prompt, system_prompt="You are a helpful assistant."):
#     ai_client = anthropic.Anthropic()
#     start_time = time.time()
#
#     response = ai_client.messages.create(
#         model="claude-sonnet-4-20250514",
#         max_tokens=1024,
#         system=system_prompt,
#         messages=[{"role": "user", "content": prompt}]
#     )
#
#     latency_ms = round((time.time() - start_time) * 1000, 2)
#     answer = response.content[0].text
#     input_tokens = response.usage.input_tokens
#     output_tokens = response.usage.output_tokens
#     stop_reason = response.stop_reason
#
#     return answer, input_tokens, output_tokens, latency_ms, stop_reason


# ---------------------------------------------------------------
# 2) SIMULATED VERSION - same return signature, runs anywhere
# ---------------------------------------------------------------
import time


def call_ai_with_metadata(prompt, system_prompt="You are a helpful assistant."):
    """Simulated AI call for live demo purposes."""
    start_time = time.time()

    # Pretend processing time
    time.sleep(0.05)

    answer = (
        "1. CrashLoopBackOff or repeated pod restarts.\n"
        "2. Readiness/liveness probe failures.\n"
        "3. Resource limits being hit (CPU/memory throttling or OOMKilled)."
    )
    input_tokens = 18
    output_tokens = 42
    latency_ms = round((time.time() - start_time) * 1000, 2)
    stop_reason = "end_turn"

    return answer, input_tokens, output_tokens, latency_ms, stop_reason


answer, in_tok, out_tok, latency, stop = call_ai_with_metadata(
    prompt="What are 3 signs a Kubernetes deployment is unhealthy?",
    system_prompt="You are a senior SRE with deep Kubernetes expertise."
)

print(f"AI Answer:\n{answer}\n")
print(f"Input tokens  : {in_tok}")
print(f"Output tokens : {out_tok}")
print(f"Latency       : {latency}ms")
print(f"Stop reason   : {stop}")

# Cost estimate (example rates)
cost = (in_tok * 0.000003) + (out_tok * 0.000015)
print(f"Estimated cost: ${cost:.6f}")
