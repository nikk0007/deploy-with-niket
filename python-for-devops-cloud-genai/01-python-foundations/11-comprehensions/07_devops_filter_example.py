# DEMO 7 — Real DevOps Example
# Scenario: AWS returns a list of EC2 instance names. You only want the web servers.

instances = [
    "web-01",
    "web-02",
    "db-01",
    "web-03",
    "cache-01",
    "db-02"
]

web_servers = [
    instance
    for instance in instances
    if instance.startswith("web")
]

print(web_servers)
# Output: ['web-01', 'web-02', 'web-03']


# Bonus — combine filter + transform in one line (very common in real scripts)
# Get web server names in uppercase, only if they are web servers

web_servers_upper = [
    instance.upper()
    for instance in instances
    if instance.startswith("web")
]

print(web_servers_upper)
# Output: ['WEB-01', 'WEB-02', 'WEB-03']
