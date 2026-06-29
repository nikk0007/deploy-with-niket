# Section 1: STRING (str)
# Scenario: a monitoring script storing server name, region, and a log entry.

server_name: str = "prod-api-server-01"
region: str = "ap-south-1"
log_entry: str = "ERROR: Connection timeout at 14:32:07"

print(server_name)
print(region)
print(log_entry)

# Strings are IMMUTABLE - once created, they cannot be changed in place.
# Any "change" actually creates a new string in memory.

# ---------------------------------------------------------------
# Indexing - every character has a position, starting from 0
# ---------------------------------------------------------------
print(log_entry[0])      # 'E'
print(log_entry[4])      # 'R'
print(log_entry[-1])     # '7'  -> negative indexing, last character

# ---------------------------------------------------------------
# Slicing - [start : end : step]
# Note: the 'end' index is NOT included.
# ---------------------------------------------------------------
print(log_entry[0:5])    # "ERROR"   -> index 0 to 4
print(log_entry[:5])     # "ERROR"   -> same result, start defaults to 0
print(log_entry[7:])     # "Connection timeout at 14:32:07"
print(log_entry[::2])    # every second character
print(log_entry[::-1])   # reverse the entire string - popular trick

# ---------------------------------------------------------------
# String methods used in production scripts
# ---------------------------------------------------------------
print(server_name.upper())                   # "PROD-API-SERVER-01"
print(log_entry.startswith("ERROR"))          # True
print(region.split("-"))                      # ['ap', 'south', '1']
print("  ap-south-1  ".strip())               # "ap-south-1"
print(log_entry.replace("ERROR", "ALERT"))    # replace log level

# f-strings - dynamic messages (URLs, logs, Slack alerts, etc.)
message = f"Deploying to {region}"
print(message)
