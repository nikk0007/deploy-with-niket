# DEMO 5 — Dictionary Comprehension
# Real-world scenario: building a service-name to port-number lookup map

services = ["auth-service", "payment-service", "notification-service"]

# ── Normal way ──
service_ports = {}
for index, service in enumerate(services):
    service_ports[service] = 8000 + index

print(service_ports)
# Output: {'auth-service': 8000, 'payment-service': 8001, 'notification-service': 8002}


# ── Dictionary comprehension ──
service_ports = {service: 8000 + index for index, service in enumerate(services)}

print(service_ports)
# Same output


# Another common GenAI use case — mapping prompt names to their token length
prompts = ["summarize_doc", "translate_text", "extract_entities"]

prompt_token_count = {prompt: len(prompt) for prompt in prompts}

print(prompt_token_count)
# Output: {'summarize_doc': 13, 'translate_text': 14, 'extract_entities': 16}
