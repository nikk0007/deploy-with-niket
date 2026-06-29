"""
DEMO 06: Complete Real-World Pattern — LLM API Call with Retry Logic
Topic: Exception & Error Handling in Python
Use Case: GenAI — Calling an LLM API (Anthropic Claude) in a data pipeline

Demonstrates ALL concepts combined:
  - Custom exceptions
  - Multiple except blocks
  - raise...from (exception chaining)
  - Exponential backoff retry
  - logger.exception() for full traceback
  - else and finally in a pipeline context
  - re-raise vs handle decision

NOTE: This demo runs in two modes:
  1. MOCK mode (default) — simulates API responses, no API key needed
  2. REAL mode — set ANTHROPIC_API_KEY env variable and USE_REAL_API=true
"""

import os
import time
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("llm_pipeline")


# ─────────────────────────────────────────────────────────────────────────────
# PART 1: Custom Exception Hierarchy for LLM pipeline
# ─────────────────────────────────────────────────────────────────────────────

class LLMPipelineError(Exception):
    """Base class for all LLM pipeline errors."""
    pass

class LLMServiceUnavailableError(LLMPipelineError):
    """Raised when the LLM API cannot be reached (network/endpoint issues)."""
    pass

class LLMRateLimitExhaustedError(LLMPipelineError):
    """Raised when all retry attempts are exhausted due to rate limiting."""
    pass

class LLMResponseParseError(LLMPipelineError):
    """Raised when the LLM returns a response that cannot be parsed as expected."""
    pass

class LLMContextLengthError(LLMPipelineError):
    """Raised when the input prompt exceeds the model's context window."""
    pass


# ─────────────────────────────────────────────────────────────────────────────
# PART 2: Mock LLM Client (simulates anthropic SDK behaviour)
# ─────────────────────────────────────────────────────────────────────────────

class MockRateLimitError(Exception):
    pass

class MockAPIConnectionError(Exception):
    pass

class MockContextLengthError(Exception):
    pass


class MockContent:
    def __init__(self, text):
        self.text = text

class MockResponse:
    def __init__(self, text):
        self.content = [MockContent(text)]


MOCK_CALL_COUNT = {"n": 0}

def mock_create_message(prompt, fail_scenario=None):
    """
    Simulates the anthropic client.messages.create() call.
    Configurable to simulate different failure scenarios.
    """
    MOCK_CALL_COUNT["n"] += 1
    call_num = MOCK_CALL_COUNT["n"]

    if fail_scenario == "rate_limit_then_success":
        if call_num <= 2:
            raise MockRateLimitError("Rate limit exceeded. Please slow down your requests.")
        return MockResponse('{"summary": "Disk usage at 87%. Alert warranted.", "severity": "high"}')

    elif fail_scenario == "connection_error":
        raise MockAPIConnectionError("Connection refused: https://api.anthropic.com")

    elif fail_scenario == "context_too_long":
        raise MockContextLengthError("Input tokens (200000) exceed model maximum (100000).")

    elif fail_scenario == "bad_json_response":
        return MockResponse("Sorry, I cannot parse this log format.")  # not JSON

    elif fail_scenario == "all_retries_fail":
        raise MockRateLimitError("Rate limit exceeded.")

    else:
        return MockResponse('{"summary": "System is healthy. No anomalies detected.", "severity": "low"}')


# ─────────────────────────────────────────────────────────────────────────────
# PART 3: Core LLM Caller with Full Exception Handling + Retry
# ─────────────────────────────────────────────────────────────────────────────

def call_llm_for_log_analysis(prompt: str, max_retries: int = 3, fail_scenario=None) -> dict:
    """
    Sends a prompt to the LLM and returns a parsed JSON response.

    Expected LLM output format:
      {"summary": "<string>", "severity": "<low|medium|high>"}

    Retry logic:
      - Rate limit errors → exponential backoff, then retry
      - Connection errors → fail immediately (retrying won't help)
      - Context length errors → fail immediately (retrying won't help)
      - Parse errors → fail immediately (retrying won't help)
    """
    for attempt in range(1, max_retries + 1):
        logger.info(f"LLM call attempt {attempt}/{max_retries}")

        try:
            # In real code: client = anthropic.Anthropic()
            # response = client.messages.create(
            #     model="claude-sonnet-4-6",
            #     max_tokens=256,
            #     messages=[{"role": "user", "content": prompt}]
            # )
            response = mock_create_message(prompt, fail_scenario=fail_scenario)
            raw_text = response.content[0].text.strip()

        except MockRateLimitError as e:
            # Retryable: wait with exponential backoff
            wait = 2 ** attempt
            logger.warning(
                f"Rate limit hit on attempt {attempt}/{max_retries}. "
                f"Waiting {wait}s before retry..."
            )
            time.sleep(0.1)  # Using 0.1s instead of real wait for demo speed
            if attempt == max_retries:
                raise LLMRateLimitExhaustedError(
                    f"Rate limit persisted after {max_retries} attempts."
                ) from e
            continue  # go to next retry

        except MockAPIConnectionError as e:
            # Not retryable: network issue won't resolve on its own
            raise LLMServiceUnavailableError(
                "LLM API is unreachable. Check network connectivity or API endpoint."
            ) from e

        except MockContextLengthError as e:
            # Not retryable: the prompt itself is too long
            raise LLMContextLengthError(
                "The log chunk is too large for the model. Split it before sending."
            ) from e

        except Exception as e:
            logger.exception("Unexpected error during LLM API call.")
            raise  # re-raise with full traceback preserved

        # If we get here, the API call succeeded — now parse the response
        try:
            parsed = json.loads(raw_text)
            if "summary" not in parsed or "severity" not in parsed:
                raise ValueError("Missing required fields: 'summary' and/or 'severity'.")
            return parsed

        except (json.JSONDecodeError, ValueError) as e:
            raise LLMResponseParseError(
                f"LLM returned an unparseable response: {repr(raw_text)}"
            ) from e

    # Should not reach here, but just in case
    raise LLMRateLimitExhaustedError("Exhausted all retry attempts.")


# ─────────────────────────────────────────────────────────────────────────────
# PART 4: Pipeline Function using else + finally
# ─────────────────────────────────────────────────────────────────────────────

import tempfile

def analyze_server_logs(log_chunk: str, output_path: str, fail_scenario=None):
    """
    Full pipeline step:
      1. Calls LLM to analyze a server log chunk
      2. Writes result to output file (else block)
      3. Always logs completion (finally block)
    """
    prompt = (
        "You are a DevOps assistant. Analyze this server log and return ONLY a JSON object "
        "with two fields: 'summary' (string) and 'severity' (low/medium/high).\n\n"
        f"Log:\n{log_chunk}"
    )

    try:
        result = call_llm_for_log_analysis(prompt, fail_scenario=fail_scenario)

    except LLMRateLimitExhaustedError:
        logger.error("Skipping log chunk: rate limit exhausted after all retries.")
        return None

    except LLMServiceUnavailableError as e:
        logger.error(f"LLM service down. Halting pipeline. Root cause: {e.__cause__}")
        raise  # Critical — stop the pipeline

    except LLMContextLengthError:
        logger.warning("Log chunk too large. Pipeline will re-chunk and retry.")
        return None

    except LLMResponseParseError as e:
        logger.error(f"Cannot parse LLM response: {e}")
        return None

    else:
        # Runs ONLY if call_llm_for_log_analysis returned successfully
        logger.info(f"Analysis complete. Severity: {result['severity'].upper()}")
        logger.info(f"Summary: {result['summary']}")

        with open(output_path, "w") as f:
            json.dump(result, f, indent=2)
        logger.info(f"Result written to: {output_path}")

        if result["severity"] == "high":
            logger.warning("HIGH severity detected! Triggering PagerDuty alert...")
            # In real code: pagerduty.trigger_alert(result["summary"])

        return result

    finally:
        # Runs ALWAYS
        logger.info("Pipeline step complete. Resources released.")
        MOCK_CALL_COUNT["n"] = 0  # reset mock counter for next scenario


# ─────────────────────────────────────────────────────────────────────────────
# MAIN: Run all scenarios
# ─────────────────────────────────────────────────────────────────────────────

SAMPLE_LOG = """
2024-01-15 03:42:11 ERROR kernel: [Hardware Error]: Machine check: Processor context corrupt
2024-01-15 03:42:11 WARN  disk: /dev/sda1 usage at 87%, threshold 85%
2024-01-15 03:42:12 ERROR nginx: upstream timed out (110: Connection timed out) while reading
2024-01-15 03:42:15 CRIT  OOM killer invoked, killing process 'java' pid 4821
"""

if __name__ == "__main__":
    print("=" * 60)
    print("DEMO 06: Complete LLM Pipeline — Exception Handling")
    print("=" * 60)

    scenarios = [
        ("success",               "✅ Success: clean LLM response"),
        ("rate_limit_then_success", "🔄 Rate limit → retries → success"),
        ("bad_json_response",     "❌ Bad JSON: parse error"),
        ("context_too_long",      "❌ Context too long: immediate fail"),
    ]

    with tempfile.TemporaryDirectory() as tmpdir:
        for scenario_key, label in scenarios:
            print(f"\n{'─'*60}")
            print(f"Scenario: {label}")
            print(f"{'─'*60}")
            output_file = os.path.join(tmpdir, f"result_{scenario_key}.json")

            try:
                result = analyze_server_logs(SAMPLE_LOG, output_file, fail_scenario=scenario_key)
                if result:
                    print(f"[Pipeline Result] {json.dumps(result)}")
                else:
                    print("[Pipeline Result] None (error was handled gracefully)")
            except LLMPipelineError as e:
                print(f"[Pipeline HALTED] {type(e).__name__}: {e}")

    print("\n" + "=" * 60)
    print("[Done] Demo 06 complete.")
    print("=" * 60)
