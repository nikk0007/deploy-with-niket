# ============================================================
# FILE 03 — Type Hints for Collections: list, dict, tuple
# Video Section: "Collections"
# ============================================================

# ---- LIST ----

flight_seats: list[int] = [12, 15, 22, 34]
passenger_names: list[str] = ["Ananya", "Rohan", "Meera"]
departure_times: list[float] = [6.30, 10.45, 14.15, 18.00]

print(flight_seats)       # [12, 15, 22, 34]
print(passenger_names)    # ['Ananya', 'Rohan', 'Meera']


# ---- DICTIONARY ----

department_headcount: dict[str, int] = {
    "engineering": 120,
    "operations": 45,
    "finance": 30
}

server_health: dict[str, bool] = {
    "api-server": True,
    "db-server": True,
    "cache-server": False
}

print(department_headcount)
print(server_health)


# ---- TUPLE — Fixed length, fixed types ----

gps_coordinates: tuple[float, float] = (28.6139, 77.2090)   # Delhi coordinates
deployment_window: tuple[str, str] = ("02:00", "04:00")      # Maintenance window

print(gps_coordinates)
print(deployment_window)


# ---- OLDER STYLE (Python 3.8 and below) ----
# Use this only if you are on an older Python version

from typing import List, Dict, Tuple

old_style_seats: List[int] = [12, 15, 22]
old_style_map: Dict[str, int] = {"servers": 10, "pods": 30}
old_style_coords: Tuple[float, float] = (19.0760, 72.8777)   # Mumbai


# ---- MODERN STYLE (Python 3.9+) — Preferred ----

modern_seats: list[int] = [12, 15, 22]
modern_map: dict[str, int] = {"servers": 10, "pods": 30}
modern_coords: tuple[float, float] = (19.0760, 72.8777)


# ---- FUNCTIONS WITH COLLECTION TYPE HINTS ----

def get_available_seats(flight_number: str) -> list[int]:
    # Returns list of available seat numbers
    return [3, 7, 12, 19, 24]

def get_region_stats() -> dict[str, int]:
    return {"ap-south-1": 8, "us-east-1": 12}

def get_server_location(server_id: str) -> tuple[float, float]:
    return (28.6139, 77.2090)

print(get_available_seats("AI-302"))
print(get_region_stats())
print(get_server_location("prod-server-01"))


# ============================================================
# SUMMARY:
# list[int]             → list of integers
# dict[str, int]        → string keys, integer values
# tuple[float, float]   → exactly two floats, in order
# ============================================================
