# SECTION 2 DEMO — Define vs Call
# Real-world scenario: sending a deployment notification to multiple engineers

# Define — function ka blueprint ban raha hai. Abhi kuch execute nahi hota.
def notify_deployment(engineer_name):
    print(f"Hi {engineer_name}, your deployment to production has been triggered.")

# Call — ab actually chalta hai
notify_deployment("Ankit")
notify_deployment("Riya")
notify_deployment("Suresh")

# Output:
# Hi Ankit, your deployment to production has been triggered.
# Hi Riya, your deployment to production has been triggered.
# Hi Suresh, your deployment to production has been triggered.

# Ek function. Teen calls. Logic ek jagah.
# Agar message change karna ho — sirf function mein karo. Teen jagah automatically update.
