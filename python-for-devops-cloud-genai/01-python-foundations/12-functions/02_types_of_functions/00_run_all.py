#!/usr/bin/env python3
# ============================================================
# MASTER RUNNER — Types of Functions in Python
# Python for DevOps, Cloud & GenAI Series
#
# Run individual files:  python 01_builtin_functions.py
# Run all in sequence:   python 00_run_all.py
# ============================================================

import subprocess
import sys
import os

DEMOS = [
    ("01_builtin_functions.py",     "SECTION 1  — Built-in Functions"),
    ("02_user_defined_functions.py","SECTION 2  — User-Defined Functions"),
    ("03_args_kwargs.py",           "SECTION 3  — *args and **kwargs"),
    ("04_lambda_higher_order.py",   "SECTION 4  — Lambda + Higher-Order Functions"),
    ("05_pure_vs_impure.py",        "SECTION 5  — Pure vs Impure Functions"),
    ("06_recursive_functions.py",   "SECTION 6  — Recursive Functions"),
    ("07_nested_closures.py",       "SECTION 7  — Nested Functions & Closures"),
    ("08_decorator_functions.py",   "SECTION 8  — Decorator Functions"),
    ("09_generator_functions.py",   "SECTION 9  — Generator Functions"),
    ("10_async_functions.py",       "SECTION 10 — Async Functions"),
    ("11_type_hinted_functions.py", "SECTION 11 — Type-Hinted Functions"),
]

def run_demo(filename, title):
    print("\n" + "█" * 60)
    print(f"  ▶  {title}")
    print("█" * 60)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath   = os.path.join(script_dir, filename)
    result = subprocess.run([sys.executable, filepath], capture_output=False)
    if result.returncode != 0:
        print(f"\n  ⚠️  {filename} exited with code {result.returncode}")
    input("\n  [ Press ENTER to continue to next section... ]")


if __name__ == "__main__":
    print("█" * 60)
    print("  TYPES OF FUNCTIONS IN PYTHON")
    print("  Python for DevOps, Cloud & GenAI")
    print("█" * 60)
    print("\n  Files in this demo pack:")
    for i, (f, t) in enumerate(DEMOS, 1):
        print(f"  {i:2}. {f}")

    print("\n  Run a specific section: python 03_args_kwargs.py")
    print("  Run all sections:       python 00_run_all.py")
    input("\n  [ Press ENTER to start running all demos... ]")

    for filename, title in DEMOS:
        run_demo(filename, title)

    print("\n" + "█" * 60)
    print("  ✅ ALL DEMOS COMPLETE!")
    print("  Subscribe for the next video:")
    print("  Multiple Return Types in Functions")
    print("█" * 60)
