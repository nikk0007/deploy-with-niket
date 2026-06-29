# ---- VARIABLES WITH TYPE HINTS ----

patient_name: str = "Rahul Sharma"
bed_number: int = 42
temperature: float = 98.6
is_discharged: bool = False

print(patient_name)       # Rahul Sharma
print(bed_number)         # 42
print(temperature)        # 98.6
print(is_discharged)      # False


# ---- FUNCTIONS WITHOUT TYPE HINTS ----
# No idea what to pass. No idea what comes back.

def calculate_bill(days, rate):
    return days * rate


# ---- FUNCTIONS WITH TYPE HINTS ----
# Crystal clear — just by reading the signature.

def calculate_bill_typed(days: int, rate: float) -> float:
    return days * rate

print(calculate_bill_typed(5, 1200.0))   # 6000.0


# ---- MORE EXAMPLES ----

def get_patient_status(patient_id: int) -> str:
    # Returns status like "Admitted", "Discharged", "ICU"
    return "Admitted"

def register_patient(name: str, age: int, is_emergency: bool) -> int:
    # Returns the new patient's bed number
    return 101

def compute_discount(original_price: float, discount_percent: float) -> float:
    return original_price - (original_price * discount_percent / 100)

print(compute_discount(5000.0, 10.0))   # 4500.0


# ============================================================
# READING A TYPE-HINTED FUNCTION:
# parameter_name: ExpectedType
# -> ReturnType
# ============================================================
