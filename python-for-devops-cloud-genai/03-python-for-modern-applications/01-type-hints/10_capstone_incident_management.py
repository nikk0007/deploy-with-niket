# ============================================================
# FILE 10 — CAPSTONE: Everything Together
# A realistic mini-project using all type hint concepts
# Domain: Cloud Incident Management System
# ============================================================
#
# This file shows how ALL concepts from this video
# work together in a real-world style codebase.
#
# Concepts used:
# ✅ Variable annotations
# ✅ Function parameters and return types
# ✅ list, dict, tuple
# ✅ Optional (str | None)
# ✅ Union types (int | str)
# ✅ Custom classes as type hints
# ✅ Callable
# ✅ Pydantic for data validation
# ============================================================

from pydantic import BaseModel, ValidationError
from typing import Callable, Any


# ============================================================
# MODELS (Pydantic — type hints + validation)
# ============================================================

class CloudService(BaseModel):
    service_id: str
    service_name: str
    region: str
    owner_team: str
    is_critical: bool


class Incident(BaseModel):
    incident_id: str
    title: str
    severity: str                          # "P1", "P2", "P3"
    affected_service: CloudService         # Nested model
    reported_by: str
    assigned_to: str | None = None         # Optional
    resolved: bool = False
    resolution_notes: str | None = None


# ============================================================
# INCIDENT REGISTRY — in-memory store
# ============================================================

incident_registry: dict[str, Incident] = {}


# ============================================================
# FUNCTIONS
# ============================================================

def create_incident(
    incident_id: str,
    title: str,
    severity: str,
    service: CloudService,
    reported_by: str
) -> Incident:
    """Create a new incident and register it."""
    incident = Incident(
        incident_id=incident_id,
        title=title,
        severity=severity,
        affected_service=service,
        reported_by=reported_by
    )
    incident_registry[incident_id] = incident
    print(f"[CREATED] Incident {incident_id}: {title} ({severity})")
    return incident


def assign_incident(incident_id: str, engineer: str) -> bool:
    """Assign an incident to an on-call engineer."""
    incident = incident_registry.get(incident_id)
    if incident is None:
        print(f"[ERROR] Incident {incident_id} not found")
        return False
    incident.assigned_to = engineer
    print(f"[ASSIGNED] {incident_id} → {engineer}")
    return True


def resolve_incident(incident_id: str, notes: str) -> bool:
    """Mark an incident as resolved with resolution notes."""
    incident = incident_registry.get(incident_id)
    if incident is None:
        print(f"[ERROR] Incident {incident_id} not found")
        return False
    incident.resolved = True
    incident.resolution_notes = notes
    print(f"[RESOLVED] {incident_id}: {notes}")
    return True


def get_open_incidents() -> list[Incident]:
    """Return all unresolved incidents."""
    return [i for i in incident_registry.values() if not i.resolved]


def get_incidents_by_severity(severity: str) -> list[Incident]:
    """Return all incidents of a given severity level."""
    return [
        i for i in incident_registry.values()
        if i.severity == severity
    ]


def get_incident(incident_id: str) -> Incident | None:
    """Fetch a single incident by ID. Returns None if not found."""
    return incident_registry.get(incident_id)


def summarize_incident(incident: Incident) -> dict[str, str | bool | None]:
    """Return a flat summary dict of an incident."""
    return {
        "id": incident.incident_id,
        "title": incident.title,
        "severity": incident.severity,
        "service": incident.affected_service.service_name,
        "region": incident.affected_service.region,
        "assigned_to": incident.assigned_to,
        "resolved": incident.resolved,
        "notes": incident.resolution_notes
    }


def notify_team(
    incident: Incident,
    send_fn: Callable[[str, str], None]
) -> None:
    """Dispatch a notification using any notification function."""
    message = (
        f"[{incident.severity}] {incident.title} "
        f"| Service: {incident.affected_service.service_name} "
        f"| Region: {incident.affected_service.region}"
    )
    send_fn("incidents-channel", message)


# ============================================================
# NOTIFICATION FUNCTIONS
# ============================================================

def slack_notify(channel: str, message: str) -> None:
    print(f"[Slack → #{channel}] {message}")

def pagerduty_notify(channel: str, message: str) -> None:
    print(f"[PagerDuty → {channel}] {message}")


# ============================================================
# MAIN FLOW — Simulating a real incident lifecycle
# ============================================================

if __name__ == "__main__":

    # Define some cloud services
    payment_service = CloudService(
        service_id="SVC-001",
        service_name="payment-api",
        region="ap-south-1",
        owner_team="payments-team",
        is_critical=True
    )

    auth_service = CloudService(
        service_id="SVC-002",
        service_name="auth-service",
        region="ap-south-1",
        owner_team="platform-team",
        is_critical=True
    )

    reporting_service = CloudService(
        service_id="SVC-003",
        service_name="reporting-api",
        region="us-east-1",
        owner_team="data-team",
        is_critical=False
    )

    print("=" * 55)
    print("INCIDENT MANAGEMENT SYSTEM — SIMULATION")
    print("=" * 55)

    # Create incidents
    inc1 = create_incident("INC-001", "Payment gateway timeout", "P1", payment_service, "Monitoring Bot")
    inc2 = create_incident("INC-002", "Auth token validation failures", "P2", auth_service, "Rohan Desai")
    inc3 = create_incident("INC-003", "Reports export taking >5 min", "P3", reporting_service, "Priya Iyer")

    print()

    # Assign engineers
    assign_incident("INC-001", "Arun Kumar")
    assign_incident("INC-002", "Neha Joshi")

    print()

    # Notify team
    notify_team(inc1, slack_notify)
    notify_team(inc1, pagerduty_notify)

    print()

    # Resolve one incident
    resolve_incident("INC-001", "Increased connection pool size from 50 to 200. Timeout resolved.")

    print()

    # Check open incidents
    open_incidents = get_open_incidents()
    print(f"Open incidents: {len(open_incidents)}")
    for inc in open_incidents:
        print(f"  - [{inc.severity}] {inc.title} → Assigned to: {inc.assigned_to or 'Unassigned'}")

    print()

    # Fetch and summarize
    fetched = get_incident("INC-001")
    if fetched is not None:
        summary = summarize_incident(fetched)
        print("Summary of INC-001:")
        for key, value in summary.items():
            print(f"  {key}: {value}")

    print()

    # Validation error demo
    print("--- Pydantic Validation Error Demo ---")
    try:
        bad_service = CloudService(
            service_id=404,                # Should be str
            service_name="broken-api",
            region="ap-south-1",
            owner_team="unknown",
            is_critical="yes"              # Should be bool
        )
    except ValidationError as e:
        print(f"Caught ValidationError:\n{e}")

    print()
    print("=" * 55)
    print("All type hints used in this file:")
    print("  ✅ str, int, float, bool — basic types")
    print("  ✅ list[Incident]         — list of objects")
    print("  ✅ dict[str, Incident]    — dict with typed values")
    print("  ✅ str | None             — Optional value")
    print("  ✅ Incident | None        — Optional custom class")
    print("  ✅ CloudService           — custom class as type hint")
    print("  ✅ Callable[[str,str],None] — function as parameter")
    print("  ✅ Pydantic BaseModel     — runtime validation")
    print("=" * 55)
