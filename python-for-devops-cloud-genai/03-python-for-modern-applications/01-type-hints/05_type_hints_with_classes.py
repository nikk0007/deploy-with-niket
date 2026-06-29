# ============================================================
# FILE 05 — Type Hints with Custom Classes
# Video Section: "Custom Classes"
# ============================================================

# Your own classes work perfectly as type annotations.
# IDE auto-complete + type checkers both benefit from this.


# ============================================================
# EXAMPLE 1 — Bank Account Transfer
# ============================================================

class BankAccount:
    def __init__(self, account_number: str, holder_name: str, balance: float):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def __repr__(self) -> str:
        return f"BankAccount({self.holder_name}, Balance: {self.balance})"


def transfer_funds(source: BankAccount, target: BankAccount, amount: float) -> bool:
    """
    Transfer amount from source to target account.
    Returns True if successful, False if insufficient balance.
    """
    if source.balance >= amount:
        source.balance -= amount
        target.balance += amount
        print(f"Transferred ₹{amount} from {source.holder_name} to {target.holder_name}")
        return True
    else:
        print(f"Insufficient balance in {source.holder_name}'s account")
        return False


account_a = BankAccount("SBI-001", "Neha Joshi", 15000.0)
account_b = BankAccount("SBI-002", "Karan Verma", 5000.0)

transfer_funds(account_a, account_b, 3000.0)
print(account_a)    # BankAccount(Neha Joshi, Balance: 12000.0)
print(account_b)    # BankAccount(Karan Verma, Balance: 8000.0)

transfer_funds(account_a, account_b, 50000.0)   # Insufficient balance


# ============================================================
# EXAMPLE 2 — Hospital Patient and Doctor
# ============================================================

class Patient:
    def __init__(self, patient_id: int, name: str, age: int):
        self.patient_id = patient_id
        self.name = name
        self.age = age

class Doctor:
    def __init__(self, doctor_id: int, name: str, specialization: str):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

def assign_doctor(patient: Patient, doctor: Doctor) -> str:
    return f"Dr. {doctor.name} ({doctor.specialization}) assigned to {patient.name}"

patient = Patient(1001, "Ramesh Gupta", 45)
doctor = Doctor(201, "Priya Sharma", "Cardiology")

result = assign_doctor(patient, doctor)
print(result)
# Dr. Priya Sharma (Cardiology) assigned to Ramesh Gupta


# ============================================================
# EXAMPLE 3 — Cloud Server and Deployment
# ============================================================

class CloudServer:
    def __init__(self, server_id: str, region: str, cpu_count: int, memory_gb: float):
        self.server_id = server_id
        self.region = region
        self.cpu_count = cpu_count
        self.memory_gb = memory_gb
        self.is_running: bool = False

    def __repr__(self) -> str:
        status = "Running" if self.is_running else "Stopped"
        return f"Server({self.server_id}, {self.region}, {status})"


def start_server(server: CloudServer) -> bool:
    server.is_running = True
    print(f"Server {server.server_id} started in {server.region}")
    return True

def stop_server(server: CloudServer) -> bool:
    server.is_running = False
    print(f"Server {server.server_id} stopped")
    return True

def get_server_info(server: CloudServer) -> dict[str, str | int | float | bool]:
    return {
        "id": server.server_id,
        "region": server.region,
        "cpu": server.cpu_count,
        "memory_gb": server.memory_gb,
        "running": server.is_running
    }


prod_server = CloudServer("prod-01", "ap-south-1", 8, 32.0)
start_server(prod_server)
print(get_server_info(prod_server))
stop_server(prod_server)
print(prod_server)


# ============================================================
# EXAMPLE 4 — List of Custom Objects
# ============================================================

class Employee:
    def __init__(self, emp_id: int, name: str, department: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

def get_high_earners(employees: list[Employee], threshold: float) -> list[Employee]:
    """Returns employees earning above the threshold."""
    return [emp for emp in employees if emp.salary > threshold]

def calculate_total_payroll(employees: list[Employee]) -> float:
    return sum(emp.salary for emp in employees)


team = [
    Employee(1, "Vikram Singh", "Engineering", 95000.0),
    Employee(2, "Pooja Rao", "Engineering", 120000.0),
    Employee(3, "Amit Tiwari", "Operations", 65000.0),
    Employee(4, "Sunita Das", "Finance", 78000.0),
]

high_earners = get_high_earners(team, 80000.0)
for emp in high_earners:
    print(f"{emp.name} — ₹{emp.salary}")

print(f"Total Payroll: ₹{calculate_total_payroll(team)}")


# ============================================================
# WHY THIS MATTERS:
#
# When you write:  source: BankAccount
# Your IDE knows:  source.balance, source.account_number, etc.
# Auto-complete works. Typos get flagged instantly.
# Type checkers catch wrong object types before runtime.
#
# This scales — the bigger your codebase, the more value it adds.
# ============================================================
