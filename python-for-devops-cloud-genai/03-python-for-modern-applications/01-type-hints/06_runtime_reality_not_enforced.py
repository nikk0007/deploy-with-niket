# ============================================================
# FILE 06 — The Runtime Reality
# Video Section: "Interview Question"
# ============================================================
# KEY QUESTION: Do type hints enforce types at runtime?
# ANSWER: NO. Python completely ignores them during execution.
# ============================================================


# ---- PROOF 1 — Wrong types passed, no error raised ----

def calculate_emi(principal: int, rate: float, months: int) -> float:
    return (principal * rate * months) / 100

# Correct usage
result_correct = calculate_emi(500000, 8.5, 12)
print(f"Correct: {result_correct}")   # 510000.0

# Wrong types — Python does NOT raise any error
result_wrong = calculate_emi("fifty thousand", "8.5%", "twelve")
# This will raise a TypeError at runtime due to string arithmetic,
# but that's a math error — NOT a type hint enforcement.
# The type hint itself does nothing to stop this call.


# ---- PROOF 2 — Completely wrong type, no complaint from Python ----

def greet_user(name: str) -> str:
    return f"Hello, {name}!"

print(greet_user("Rahul"))       # Hello, Rahul!
print(greet_user(12345))         # Hello, 12345! — No error. Python accepts it.
print(greet_user(True))          # Hello, True!  — Still no error.
print(greet_user(["a", "b"]))    # Hello, ['a', 'b']! — Python doesn't care.


# ---- PROOF 3 — Wrong return type, no enforcement ----

def get_server_count() -> int:
    return "ten"      # This is a string, not int. Python allows it.

result = get_server_count()
print(result)         # ten — no error, no warning at runtime
print(type(result))   # <class 'str'>


# ============================================================
# SO WHAT ARE TYPE HINTS ACTUALLY FOR?
# ============================================================
#
# 1. DEVELOPERS — Type hints make code self-documenting.
#    Whoever reads the function knows exactly what to pass.
#
# 2. IDEs — VS Code, PyCharm use type hints to:
#    - Show red underlines when wrong types are used
#    - Provide accurate auto-complete suggestions
#    - Display type info on hover
#
# 3. TYPE CHECKERS — Run separately before execution:
#    - mypy      → pip install mypy  → mypy this_file.py
#    - Pyright   → built into VS Code via Pylance extension
#    - Pylance   → real-time warnings in editor
#
# ============================================================
# HOW TO USE mypy (run this in terminal, not in Python):
#
# pip install mypy
# mypy 06_runtime_reality.py
#
# mypy WILL flag the wrong calls above as errors.
# Python at runtime will NOT.
# ============================================================


# ---- EXCEPTION: Pydantic and FastAPI DO enforce at runtime ----
# But they do it themselves — Python interpreter does not.

# from pydantic import BaseModel
#
# class Order(BaseModel):
#     product_id: int
#     quantity: int
#
# order = Order(product_id="not-an-int", quantity=2)
# ^ This WILL raise a ValidationError — because Pydantic checks it.
# That is Pydantic's job, not Python's.


# ============================================================
# SUMMARY TABLE:
#
# Who uses type hints?     What they do with it
# ─────────────────────────────────────────────────────────
# Python interpreter       Ignores them completely at runtime
# Developer (you)          Reads them for clarity
# VS Code / PyCharm        Shows warnings, powers auto-complete
# mypy / Pyright           Flags errors before you run code
# Pydantic / FastAPI       Enforces them at runtime (their own logic)
# ─────────────────────────────────────────────────────────
# ============================================================
