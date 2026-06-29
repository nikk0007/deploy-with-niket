# Section 3: TUPLE (tuple)
# Scenario: data that should NEVER change at runtime,
# like a database connection (host, port).

db_connection: tuple = ("prod-db.internal", 5432)
http_response: tuple = (200, "OK")
server_location: tuple = ("Mumbai", 19.0760, 72.8777)

print(db_connection)
print(http_response)
print(server_location)

# Tuples are IMMUTABLE - "list" that can never be modified after creation.
# Uncomment the next line to see the error this causes:
# db_connection[0] = "new-host"   # TypeError: 'tuple' object does not support item assignment

# ---------------------------------------------------------------
# Unpacking - tuple's superpower
# ---------------------------------------------------------------
host, port = db_connection
print(host)   # prod-db.internal
print(port)   # 5432

status_code, message = http_response
print(status_code)   # 200
print(message)       # OK

# This pattern is very common in DevOps scripts: a function returns
# multiple values as a tuple, and you unpack them directly.

# ---------------------------------------------------------------
# List vs Tuple - the rule
# ---------------------------------------------------------------
# Data that SHOULD change      -> list
# Data that should NEVER change -> tuple
#
# Bonus: tuples are slightly faster in memory, and (unlike lists)
# can be used as dictionary keys.

location_cache = {
    server_location: "Primary data center"
}
print(location_cache[server_location])
