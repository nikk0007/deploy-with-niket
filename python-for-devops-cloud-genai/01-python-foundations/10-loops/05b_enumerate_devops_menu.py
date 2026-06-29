# ============================================================
# 21_enumerate_devops_menu.py
# Topic: Practical use of enumerate() — DevOps Control Panel
# ============================================================

# enumerate() is used here to:
#   1. Automatically number each menu option while displaying it
#   2. Match the user's number input back to the correct option
#   3. No manual index tracking needed anywhere in the code

# ---- Define the menu options ----
menu_options = [
    "Check health status of all microservices",
    "Deploy latest build to production",
    "Roll back to the previous stable release",
    "View real-time CPU and memory metrics",
    "Scale up the Kubernetes cluster",
    "Rotate API keys and secrets",
    "Download the latest deployment logs",
    "Exit the control panel",
]

# ---- Display the menu using enumerate ----
print("=" * 55)
print("       DEVOPS CONTROL PANEL — Main Menu")
print("=" * 55)

for number, option in enumerate(menu_options, start=1):
    print(f"  [{number}]  {option}")

print("=" * 55)

# ---- Get user input ----
choice = int(input("\nEnter the number of your choice: "))

# ---- Validate and respond ----
if 1 <= choice <= len(menu_options):
    selected = menu_options[choice - 1]   # list is 0-indexed, menu starts at 1
    print(f"\nYou selected option [{choice}]: {selected}")
    print("Executing... please wait.")
else:
    print(f"\nInvalid choice: {choice}. Please enter a number between 1 and {len(menu_options)}.")