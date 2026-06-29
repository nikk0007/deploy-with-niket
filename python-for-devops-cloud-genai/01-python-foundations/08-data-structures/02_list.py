# Section 2: LIST (list)
# Scenario: monitoring system tracking running servers across regions.

active_servers: list = ["server-01", "server-02", "server-03"]
open_ports: list = [22, 80, 443, 8080]

print(active_servers)
print(open_ports)

# Lists are ORDERED  -> position matters
# Lists are MUTABLE   -> can add, remove, change items

# ---------------------------------------------------------------
# Common operations
# ---------------------------------------------------------------
active_servers.append("server-04")        # add at the end
print(active_servers)

active_servers.insert(0, "server-00")     # add at a specific position
print(active_servers)

active_servers.remove("server-02")        # remove by value
print(active_servers)

last_removed = active_servers.pop()       # remove (and return) last item
print("Removed:", last_removed)
print(active_servers)

print(len(active_servers))                # count items
print("server-01" in active_servers)      # membership check -> True/False

active_servers.sort()                     # sort the list
print(active_servers)

# ---------------------------------------------------------------
# Indexing & slicing work just like strings
# ---------------------------------------------------------------
print(active_servers[0])    # first server
print(active_servers[-1])   # last server

# ---------------------------------------------------------------
# Real use cases (just for reference, not run):
# - EC2 instance IDs that need patching
# - All pod names in a Kubernetes namespace
# - AI responses collected in a LangChain pipeline
# - A queue of pending deployment jobs
# ---------------------------------------------------------------
