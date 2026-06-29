# demo_01_procedural_chaos.py
# ============================================================
# VIDEO DEMO — Part 1 & 2
# Show this first: "Functions work great for small scripts"
# Then show how it becomes chaotic as project grows
# ============================================================

# -------------------------------------------------------
# STEP 1: Small script — functions are perfect here
# -------------------------------------------------------

def create_ec2():
    print("Creating EC2 instance...")

def stop_ec2():
    print("Stopping EC2 instance...")

def terminate_ec2():
    print("Terminating EC2 instance...")

# Call them — clean, simple, works great
create_ec2()
stop_ec2()
terminate_ec2()


# -------------------------------------------------------
# STEP 2: Now the project grows — add Kubernetes
# -------------------------------------------------------

def create_cluster():
    print("Creating Kubernetes cluster...")

def delete_cluster():
    print("Deleting Kubernetes cluster...")

def get_pods():
    print("Getting pods...")

def restart_deployment():
    print("Restarting deployment...")

def create_namespace():
    print("Creating namespace...")


# -------------------------------------------------------
# STEP 3: Add Docker
# -------------------------------------------------------

def build_image():
    print("Building Docker image...")

def run_container():
    print("Running Docker container...")

def push_image():
    print("Pushing image to registry...")


# -------------------------------------------------------
# STEP 4: Add GenAI / OpenAI
# -------------------------------------------------------

def generate_openai():
    print("Generating response from OpenAI...")

def generate_claude():
    print("Generating response from Claude...")

def generate_ollama():
    print("Generating response from Ollama...")

def generate_gemini():
    print("Generating response from Gemini...")

def embed_openai():
    print("Creating embeddings via OpenAI...")

def embed_claude():
    print("Creating embeddings via Claude...")


# -------------------------------------------------------
# PAUSE HERE while teaching and ask the students:
# "Which functions actually belong together?"
# "How do you find all Kubernetes functions in this file?"
# "What happens when we have 100 functions like this?"
# -------------------------------------------------------

# -------------------------------------------------------
# STEP 5: Now call them — notice how messy this looks
# -------------------------------------------------------

print("\n--- Running EC2 Operations ---")
create_ec2()
stop_ec2()
terminate_ec2()

print("\n--- Running Kubernetes Operations ---")
create_cluster()
get_pods()
restart_deployment()

print("\n--- Running Docker Operations ---")
build_image()
run_container()
push_image()

print("\n--- Running AI Operations ---")
generate_openai()
generate_claude()
embed_openai()

# -------------------------------------------------------
# POINT TO MAKE:
# 30 functions, 4 categories, one flat file.
# No structure. No grouping. No clarity.
# Imagine 6 months from now — 100 functions.
# Imagine a new team member opening this file.
# This is the PROBLEM that OOP solves.
# -------------------------------------------------------
