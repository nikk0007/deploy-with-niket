# Real systems often need both in the same loop:
# continue → skip corrupted or invalid entries, keep going
# break    → stop everything if a critical limit is crossed

# ---- Example 1: GenAI Document Batch — Embedding Job ----
print("=== GenAI Document Batch Processing (Embeddings) ===\n")

documents = [
    ("invoice_2024.pdf", 1200),
    ("scan_corrupted.pdf", -1),
    ("contract_v2.pdf", 3400),
    ("broken_upload.pdf", -1),
    ("legal_brief_full.pdf", 128000),
    ("summary_notes.pdf", 800),
]

TOKEN_LIMIT = 100_000

for filename, token_count in documents:
    # Corrupted file — skip it and move on (continue)
    if token_count == -1:
        print(f"  [SKIP]  {filename} — corrupted, cannot read token count")
        continue

    # Token limit exceeded — halt the entire batch (break)
    if token_count >= TOKEN_LIMIT:
        print(f"  [HALT]  {filename} exceeds token limit ({token_count:,} tokens). Halting batch job.")
        break

    # Normal processing
    print(f"  [OK]    {filename} — embedding generated ({token_count:,} tokens)")

print("\n(summary_notes.pdf was NEVER reached — break fired on legal_brief_full.pdf)\n")


# ---- Example 2: Log Analysis — skip INFO, stop on CRITICAL ----
print("=== Log Analysis — Skip INFO, Stop on CRITICAL ===\n")

logs = [
    ("INFO", "Server started"),
    ("WARN", "High memory usage: 82%"),
    ("INFO", "Health check passed"),
    ("ERROR", "DB connection retry"),
    ("CRITICAL", "Out of memory — OOM killer triggered"),
    ("ERROR", "Pod restart loop detected"),
]

for level, message in logs:
    if level == "INFO":
        continue    # INFO logs are too noisy — skip them
    if level == "CRITICAL":
        print(f"  [!!!] CRITICAL: {message} — Paging on-call SRE immediately!")
        break       # stop all processing and escalate right now
    print(f"  [{level}] {message}")

print()
print("=== Summary ===")
print("continue → move on; the loop keeps going  (filter / skip)")
print("break    → full stop; exit the loop now   (halt / escalate)")
print("Together → selective processing with an emergency override.")
