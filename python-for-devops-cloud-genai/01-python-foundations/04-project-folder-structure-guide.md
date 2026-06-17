# 🗂️ Python project Folder Structure Complete Guide — Modules, Packages, Scope & Namespace

> *"Writing code is easy. Organizing code so that others — and future you —
> can understand it — that is the real skill."*

This guide covers how to structure Python projects professionally — from folder
layout to modules, packages, scope rules, namespace, and naming conventions.
The concepts here apply whether you are building a small script or a
production-grade application.

📺 **Video Tutorial:** [How to Write Clean Python Projects — Modules, Packages, Scope & Namespace | Hindi](#)
📂 **Part of:** Python for Beginners Series — Video #4

---

## 📋 Table of Contents

- [Why Organization Matters](#why-organization-matters)
- [Top-Level Project Structure](#top-level-project-structure)
- [Modules — The Basic Building Block](#modules--the-basic-building-block)
- [Packages — Grouping Related Modules](#packages--grouping-related-modules)
- [A Real Project Structure Walkthrough](#a-real-project-structure-walkthrough)
- [Scope — What Can Access What](#scope--what-can-access-what)
  - [The LEGB Rule](#the-legb-rule)
  - [Scope in Practice](#scope-in-practice)
  - [The City Mental Model](#the-city-mental-model)
- [Namespace — Every Name Has an Address](#namespace--every-name-has-an-address)
- [Naming Conventions — PEP 8](#naming-conventions--pep-8)
- [Quick Reference](#quick-reference)

---

## Why Organization Matters

A Python project does not stay small. What starts as 80 lines becomes 800,
then 8000. Without structure, even your own code becomes unreadable within weeks.

### What happens in unorganized projects

```
main.py  ← 2000 lines
         ← database logic here
         ← UI logic here
         ← calculation logic here
         ← report generation here
         ← config here
         ← everything here
```

- Finding a bug means searching thousands of lines in a single file
- Two developers cannot work simultaneously without constantly conflicting
- Changing one thing breaks three other things you did not expect
- Sharing or reusing any part of the code becomes nearly impossible

### What organized code gives you

```
calculator.py    ← open this for calculation bugs
db_connect.py    ← open this for database issues
report_gen.py    ← open this to change report format
```

- Every file has one clear responsibility
- New team members understand the project structure in under 60 seconds
- Bugs have a known address — you know exactly which file to open
- Individual parts can be tested, updated, or replaced independently

> 💡 **The core principle:** Separation of concerns. Each piece of code should
> have one job, live in one place, and be findable in under 10 seconds.
>
> Organization does not increase productivity — it prevents productivity from
> crashing as the project grows.

---

## Top-Level Project Structure

Every Python project starts with one top-level folder. Everything lives inside it.

### Minimal professional structure

```
my_project/
│
├── main.py              ← Entry point — run this to start the application
├── requirements.txt     ← All dependencies listed here
├── .gitignore           ← Files Git should not track
├── README.md            ← What this project is and how to run it
│
├── models/              ← Data definitions and classes
│   └── __init__.py
│
├── services/            ← Business logic and operations
│   └── __init__.py
│
├── utils/               ← Shared helper functions
│   └── __init__.py
│
└── tests/               ← All test files
```

### The entry point file — main.py

`main.py` (or `run.py`) is the **one file you run** to start the application.

- It does **not** contain business logic
- It only calls and connects other parts of the project
- Think of it as the **ignition key** — it starts the engine, it is not the engine

```python
# main.py — entry point example
from services.score_calc import calculate_final_score
from services.report_gen import generate_report

if __name__ == "__main__":
    score = calculate_final_score()
    generate_report(score)
```

When someone receives your project for the first time, they look for `main.py`
and know immediately — *this is where everything begins.* No guessing required.

---

## Modules — The Basic Building Block

In Python, **every single `.py` file is officially called a Module.**

This is Python's own vocabulary — used in documentation, on Stack Overflow,
and in job interviews. Knowing this term makes you sound and think like a
professional.

```
main.py              ← a module
calculator.py        ← a module
db_connect.py        ← a module
send_notification.py ← a module
```

### What a module contains

A module can contain functions, classes, variables — or all three.

```python
# score_calculator.py — a module with one clear responsibility

PASS_MARK = 40   # module-level variable

def calculate_percentage(marks_obtained, total_marks):
    return (marks_obtained / total_marks) * 100

def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"
```

### Importing a module

```python
# import the whole module
import score_calculator

# import specific functions from a module
from score_calculator import calculate_percentage, assign_grade

# use them
percentage = calculate_percentage(385, 500)
grade = assign_grade(percentage)
```

### One module — one responsibility

| Module | Its only job |
|--------|-------------|
| `db_connect.py` | Database connections only |
| `send_notification.py` | Sending notifications only |
| `score_calculator.py` | Score and grade calculations only |
| `report_gen.py` | Report generation only |

> 🏥 **Analogy:** A hospital has separate departments — Radiology, Cardiology,
> Emergency, Pharmacy. Each handles one type of work. If the pharmacy has a
> problem, you go to the pharmacy — not to Radiology. Modules work exactly
> the same way.

---

## Packages — Grouping Related Modules

When multiple related modules need to live together, they go inside a folder.
But **not every folder is a Python Package** — there is one specific requirement.

### The rule

> A folder becomes a Python Package **only** when it contains a file named
> exactly: `__init__.py`

### What goes inside `__init__.py`?

Most of the time — **nothing.** The file is completely empty.
Its mere presence is all that matters. It is Python's signal:
*"This folder is not just a folder — it is a package."*

```python
# __init__.py
# (this file is intentionally left empty)
```

### Module vs Package — in one line

```
Module  =  any .py file
Package =  a folder that contains __init__.py
```

### Package structure example

```
notifications/              ← Python PACKAGE (has __init__.py)
├── __init__.py             ← makes this folder a package
├── email_sender.py         ← module inside the package
├── sms_sender.py           ← module inside the package
└── push_sender.py          ← module inside the package

reports/                    ← just a plain folder (no __init__.py)
├── monthly_report.py       ← Python does NOT treat this as a package
└── weekly_report.py
```

### Importing from a package

```python
from notifications.email_sender import send_welcome_email
from notifications.sms_sender import send_otp
from notifications.push_sender import send_alert
```

The dot notation — `notifications.email_sender` — is Python reading:
*"Inside the notifications package, find the email_sender module."*

> 📌 **Note:** Even if you do not plan to create packages yourself right away,
> you will read other people's code on GitHub, use open-source libraries, and
> work in teams — all of which use packages constantly. Knowing this makes
> everything else click.

---

## A Real Project Structure Walkthrough

Here is how a complete, real project is organized — an **online exam system.**

```
exam_system/
│
├── main.py                  ← entry point — run this
├── requirements.txt
├── .gitignore
│
├── models/                  ← what kind of data exists in this system
│   ├── __init__.py
│   ├── student.py           ← Student class, student data structure
│   └── question.py          ← Question class, question data structure
│
├── services/                ← what operations the system performs
│   ├── __init__.py
│   ├── evaluator.py         ← answer checking logic
│   └── score_calc.py        ← score and grade calculation logic
│
├── utils/                   ← helper functions used across the project
│   ├── __init__.py
│   ├── timer.py             ← exam timer logic
│   └── validator.py         ← input validation functions
│
└── tests/                   ← automated tests for each part
    ├── test_evaluator.py
    └── test_score_calc.py
```

### What anyone can read from this structure alone — without opening a single file

- This is an exam system
- Students and questions are the core data — defined in `models/`
- Evaluation and scoring are the main operations — in `services/`
- Timer and validation are shared helpers — in `utils/`
- Each part has its own tests — in `tests/`

**Time taken to understand the full system: under 60 seconds. Lines of code read: zero.**

That is the power of organized code.

---

## Scope — What Can Access What

Scope defines **which parts of your code can see and use which variables
and functions.**

This is one of the most important concepts in Python — and in any programming
language. Once you understand it clearly, a huge category of bugs becomes
instantly obvious.

---

### The LEGB Rule

Python looks up any name in this exact order:

```
L  →  Local      — inside the current function
E  →  Enclosing  — outer function (for nested functions)
G  →  Global     — top of the current file
B  →  Built-in   — Python's own names: print, len, range, type...
```

Python checks L first, then E, then G, then B — and stops at the first match.

---

### Scope in Practice

```python
TAX_RATE = 0.18           # Global scope — visible throughout this file

def calculate_bill(amount):
    tax = amount * TAX_RATE    # Local — only visible inside this function
    total = amount + tax       # Local — only visible inside this function
    return total

def display_summary(amount):
    print(TAX_RATE)            # ✅ Works — TAX_RATE is global
    print(tax)                 # ❌ ERROR — tax is local to calculate_bill
```

**Why does this error happen?**

`tax` was created inside `calculate_bill`. It belongs to that function.
`display_summary` is a completely separate function — it has no access to
what was created inside `calculate_bill`.

**The rule in plain words:**

> Inner can see outer. Outer cannot see inner.

---

### The City Mental Model

This analogy makes scope permanently clear.

```
Your entire program  =  a city

Global variables     =  public roads and parks
                        anyone can use them, no permission needed

Each function        =  a house in the city
                        has its own private space inside

Variables inside     =  furniture and belongings inside that house
a function           =  only the people inside can use them
```

Applied to code:

```python
# PUBLIC ROAD — both functions can access this
interest_rate = 8.5

def calculate_emi(loan_amount, years):
    # INSIDE THIS HOUSE
    monthly_rate = interest_rate / 12 / 100   # ✅ can use the public road
    months = years * 12
    emi = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    return emi

def show_loan_summary(amount):
    # INSIDE A DIFFERENT HOUSE
    print(f"Interest rate: {interest_rate}")  # ✅ public road — accessible
    print(monthly_rate)                        # ❌ ERROR — that's inside
                                               #    calculate_emi's house
```

```
interest_rate   →  public road  →  both functions can use it     ✅
monthly_rate    →  inside calculate_emi's house  →  show_loan_summary cannot reach it  ❌
```

**Why is this a feature, not a limitation?**

Functions not sharing their internal variables means one function cannot
accidentally interfere with another function's internal working. In large
projects with hundreds of functions — this protection is invaluable.

---

## Namespace — Every Name Has an Address

Namespace is the **address system** Python uses to track every name —
every variable, function, and class — and where it belongs.

### Why namespace exists

```python
# file: payments.py
def process():
    print("Processing payment...")

# file: inventory.py
def process():
    print("Processing inventory...")
```

Both files have a function named `process`. No conflict. Why?

Because they live in **different namespaces**:
- `payments.process` — one address
- `inventory.process` — completely different address

Python keeps them separate automatically.

### Using namespace when importing

```python
import payments
import inventory

payments.process()    # ✅ runs payment processing
inventory.process()   # ✅ runs inventory processing — no confusion
```

### The analogy — India's Pincode system

Across India, thousands of people share the same name — "Amit Sharma",
"Priya Singh", "Rahul Verma." Yet a letter addressed with the full address
including pincode reaches exactly the right person every time.

**Namespace is that pincode system for Python.**

Every name has a complete, unique address. Same name in different files —
no conflict, no confusion, because the full address is different.

---

## Naming Conventions — PEP 8

These conventions are officially defined in **PEP 8** — Python's agreed-upon
style standard. Any Python developer reading your code will immediately know
what kind of thing each name is — just from how it is written.

### Files and folders — `snake_case`

```
score_calculator.py
db_connection.py
send_notification.py
exam_system/
```

All lowercase. Words separated by underscores. No spaces. No capitals.

### Classes — `PascalCase`

```python
class StudentReport:
    pass

class DatabaseConnection:
    pass

class NotificationService:
    pass
```

Each word starts with a capital letter. No underscores.

### Functions and variables — `snake_case`

```python
def calculate_grade(marks_obtained, total_marks):
    student_name = "Rahul Sharma"
    pass_percentage = 40
    return pass_percentage
```

Same style as files — lowercase with underscores.

### Constants — `ALL_CAPS`

Values that never change throughout the program:

```python
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
BASE_API_URL = "https://api.example.com"
GST_RATE = 0.18
```

All capitals. Words separated by underscores.

### Summary table

| Type | Convention | Example |
|------|-----------|---------|
| Files & folders | `snake_case` | `score_calculator.py` |
| Classes | `PascalCase` | `StudentReport` |
| Functions | `snake_case` | `calculate_grade()` |
| Variables | `snake_case` | `total_marks` |
| Constants | `ALL_CAPS` | `MAX_RETRY_ATTEMPTS` |

> 📌 **The one-line naming rule:**
> A name should be so clear that a comment explaining it is unnecessary.
>
> ```python
> x = 450          # what is this?
> total_marks = 450  # instantly clear
> ```

---

## Quick Reference

### Vocabulary

| Term | Definition |
|------|-----------|
| **Module** | Any `.py` file |
| **Package** | A folder that contains `__init__.py` |
| **Entry point** | `main.py` or `run.py` — where the application starts |
| **Scope** | Which code can see which variables |
| **LEGB** | Local → Enclosing → Global → Built-in (Python's scope lookup order) |
| **Namespace** | Python's address system for every name in your program |

### Professional folder structure

```
my_project/
├── main.py              ← entry point
├── requirements.txt     ← dependencies
├── .gitignore
├── README.md
│
├── models/
│   └── __init__.py      ← makes this a package
│
├── services/
│   └── __init__.py
│
├── utils/
│   └── __init__.py
│
└── tests/
```

### Scope rule — one line

```
Inner scope can see outer scope.
Outer scope cannot see inner scope.
```

### The professional starting sequence

```
1. Create project folder
2. Create virtual environment inside it
3. Activate the virtual environment
4. Create main.py and folder structure
5. THEN start writing code
```

> Structure first. Code second. Always.

---

### Files that always go in `.gitignore`

```
.venv/
__pycache__/
*.pyc
```
---
*Happy Coding! 🚀*