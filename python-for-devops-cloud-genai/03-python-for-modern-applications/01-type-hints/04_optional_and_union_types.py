# ============================================================
# FILE 04 — Optional and Union Types
# Video Section: "Optional and Union Types"
# ============================================================

# ---- THE PROBLEM THIS SOLVES ----
# When fetching from a database — the record might not exist.
# When reading a config — the key might be missing.
# The function could return a value OR None.
# We need to express that clearly.


# ============================================================
# OPTIONAL — Value may or may not be present
# ============================================================

# Old style (Python 3.8 and below)
from typing import Optional

def fetch_employee(emp_id: int) -> Optional[str]:
    """
    Returns employee name if found.
    Returns None if employee does not exist.
    """
    employee_db = {101: "Sneha Kulkarni", 102: "Arjun Mehta"}
    return employee_db.get(emp_id)  # returns None if key missing

print(fetch_employee(101))   # Sneha Kulkarni
print(fetch_employee(999))   # None


# Modern style (Python 3.10+) — Preferred
def fetch_employee_v2(emp_id: int) -> str | None:
    employee_db = {101: "Sneha Kulkarni", 102: "Arjun Mehta"}
    return employee_db.get(emp_id)

print(fetch_employee_v2(102))   # Arjun Mehta
print(fetch_employee_v2(888))   # None


# More Optional examples
def get_config_value(key: str) -> str | None:
    config = {"env": "production", "region": "ap-south-1"}
    return config.get(key)

def get_last_login(user_id: int) -> str | None:
    # New user might not have logged in yet
    logins = {1: "2024-11-01", 2: "2024-10-15"}
    return logins.get(user_id)

print(get_config_value("env"))        # production
print(get_config_value("missing"))    # None
print(get_last_login(1))              # 2024-11-01
print(get_last_login(99))             # None


# ============================================================
# UNION — Multiple types are valid
# ============================================================

# When a parameter can legitimately be more than one type

def log_event(event_id: int | str) -> None:
    """
    event_id could be an integer (from internal system)
    or a string (from external API)
    Both are valid.
    """
    print(f"Logging event: {event_id}")

log_event(1042)          # Logging event: 1042
log_event("EVT-2024-XZ") # Logging event: EVT-2024-XZ


def process_pnr(pnr: int | str) -> str:
    """
    IRCTC PNR — some systems store as int, some as string.
    This function handles both.
    """
    return f"Processing PNR: {str(pnr)}"

print(process_pnr(4521067890))       # Processing PNR: 4521067890
print(process_pnr("4521067890"))     # Processing PNR: 4521067890


def set_timeout(value: int | float) -> None:
    print(f"Timeout set to {value} seconds")

set_timeout(30)      # int
set_timeout(0.5)     # float


# ============================================================
# OPTIONAL PARAMETERS IN FUNCTION SIGNATURE
# ============================================================

def create_ticket(
    title: str,
    priority: str,
    assigned_to: str | None = None    # Optional parameter with default None
) -> dict[str, str | None]:
    return {
        "title": title,
        "priority": priority,
        "assigned_to": assigned_to
    }

print(create_ticket("Server Down", "high"))
print(create_ticket("Update Docs", "low", "Ravi Kumar"))


# ============================================================
# SUMMARY:
# str | None      → value is a string OR nothing (Optional)
# int | str       → value can be integer OR string (Union)
# str | None = None  → optional parameter, defaults to None
#
# Modern syntax uses pipe | symbol (Python 3.10+)
# Older syntax uses Optional[str] or Union[int, str]
# ============================================================
