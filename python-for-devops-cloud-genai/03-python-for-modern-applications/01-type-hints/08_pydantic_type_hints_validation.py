# ============================================================
# FILE 08 — Pydantic + Type Hints = Runtime Validation
# Video Section: "Real-World Example: Pydantic"
# ============================================================
#
# Install first: pip install pydantic
# ============================================================

from pydantic import BaseModel, ValidationError


# ============================================================
# EXAMPLE 1 — Flight Booking
# ============================================================

class FlightBooking(BaseModel):
    passenger_name: str
    flight_number: str
    seat_number: str
    fare: float
    is_confirmed: bool


# ---- Valid booking ----
booking = FlightBooking(
    passenger_name="Priya Nair",
    flight_number="AI-302",
    seat_number="14C",
    fare=4500.00,
    is_confirmed=True
)

print(booking)
print(f"Passenger: {booking.passenger_name}")
print(f"Fare: ₹{booking.fare}")


# ---- Pydantic auto-converts compatible types ----
# "4500" (string) is automatically converted to 4500.0 (float)
auto_converted = FlightBooking(
    passenger_name="Rahul Mehta",
    flight_number="6E-245",
    seat_number="3A",
    fare="4500",      # ← String, but Pydantic converts it to float
    is_confirmed=1    # ← Integer 1, Pydantic converts it to True
)
print(f"\nAuto-converted fare: {auto_converted.fare} (type: {type(auto_converted.fare).__name__})")
print(f"Auto-converted confirmed: {auto_converted.is_confirmed} (type: {type(auto_converted.is_confirmed).__name__})")


# ---- Invalid data → Pydantic raises ValidationError ----
print("\n--- Attempting invalid booking ---")
try:
    bad_booking = FlightBooking(
        passenger_name="Sonia Roy",
        flight_number="AI-100",
        seat_number="7B",
        fare="four thousand five hundred",   # ← Cannot convert to float
        is_confirmed=True
    )
except ValidationError as e:
    print(f"Validation Error caught:\n{e}")


# ============================================================
# EXAMPLE 2 — Cloud Deployment Config
# ============================================================

class DeploymentConfig(BaseModel):
    service_name: str
    replicas: int
    image_tag: str
    auto_scale: bool
    max_memory_mb: float
    environment: str = "staging"    # Default value


config = DeploymentConfig(
    service_name="payment-api",
    replicas=3,
    image_tag="v2.1.0",
    auto_scale=True,
    max_memory_mb=512.0
)

print(f"\nService: {config.service_name}")
print(f"Environment: {config.environment}")   # staging (default)
print(config.model_dump())                     # Full dict


# ---- Validation error example ----
print("\n--- Attempting invalid config ---")
try:
    bad_config = DeploymentConfig(
        service_name="order-api",
        replicas="three",          # ← Cannot convert to int
        image_tag="v1.0.0",
        auto_scale=True,
        max_memory_mb=256.0
    )
except ValidationError as e:
    print(f"Validation Error caught:\n{e}")


# ============================================================
# EXAMPLE 3 — Nested Models (Common in FastAPI and LangChain)
# ============================================================

class Address(BaseModel):
    street: str
    city: str
    pincode: str

class Employee(BaseModel):
    emp_id: int
    name: str
    department: str
    salary: float
    address: Address              # Nested Pydantic model
    skills: list[str]             # List with type hint


emp = Employee(
    emp_id=1001,
    name="Kavya Menon",
    department="Engineering",
    salary=95000.0,
    address=Address(
        street="12, MG Road",
        city="Bengaluru",
        pincode="560001"
    ),
    skills=["Python", "Docker", "Kubernetes"]
)

print(f"\nEmployee: {emp.name}")
print(f"City: {emp.address.city}")
print(f"Skills: {', '.join(emp.skills)}")
print(emp.model_dump())


# ============================================================
# TYPE HINTS + PYDANTIC SUMMARY:
#
# Type hints alone:
#   → Documentation for developers and IDEs
#   → No runtime validation
#
# Type hints + Pydantic:
#   → Automatic data validation at runtime
#   → Automatic type coercion where possible
#   → Clear ValidationError with field-level messages
#   → Used in FastAPI, LangChain, LlamaIndex, AWS Lambda handlers
#
# One rule:
#   If data comes from outside your code (API, user input, config file)
#   → Validate it with Pydantic
# ============================================================
