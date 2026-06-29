# DEMO 1 — List Comprehension Basics
# Real-world scenario: squaring CPU utilization readings for a load-spike alert

cpu_readings = [10, 25, 40, 55, 70]

# ── Normal way: for loop + append() ──
squared_readings = []
for reading in cpu_readings:
    squared_readings.append(reading * reading)

print(squared_readings)
# Output: [100, 625, 1600, 3025, 4900]


# ── List comprehension way ──
squared_readings = [reading * reading for reading in cpu_readings]

print(squared_readings)
# Same output: [100, 625, 1600, 3025, 4900]

# Read it like English:
# [reading * reading for reading in cpu_readings]
# means: "Give me reading*reading for every reading in cpu_readings"

# Both versions do EXACTLY the same thing.
# List comprehension is just for loop + append() compressed into one line.
