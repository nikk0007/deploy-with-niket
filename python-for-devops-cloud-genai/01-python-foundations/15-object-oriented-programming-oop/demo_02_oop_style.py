# demo_02_oop_style.py
# ============================================================
# VIDEO DEMO — Part 4 & 5
# Show this AFTER demo_01 — same operations, OOP style
# Students should immediately feel the difference
# DO NOT explain class/self/__init__ here — just show the usage
# ============================================================

# -------------------------------------------------------
# NOTE FOR TEACHER:
# These are placeholder classes — we are NOT teaching
# how to write a class yet. That is Video 2.
# Just show HOW they are USED. The "feel" of OOP.
# -------------------------------------------------------

class EC2Manager:
    def create(self):
        print("Creating EC2 instance...")

    def stop(self):
        print("Stopping EC2 instance...")

    def delete(self):
        print("Terminating EC2 instance...")

    def describe(self):
        print("Describing EC2 instance...")

    def list_instances(self):
        print("Listing all EC2 instances...")

    def attach_volume(self):
        print("Attaching EBS volume...")

    def create_snapshot(self):
        print("Creating EC2 snapshot...")


class KubernetesManager:
    def create(self):
        print("Creating Kubernetes cluster...")

    def delete(self):
        print("Deleting Kubernetes cluster...")

    def get_pods(self):
        print("Getting all pods...")

    def scale(self):
        print("Scaling deployment...")

    def restart(self):
        print("Restarting deployment...")

    def create_namespace(self):
        print("Creating namespace...")


class DockerManager:
    def build(self):
        print("Building Docker image...")

    def run(self):
        print("Running Docker container...")

    def push(self):
        print("Pushing image to registry...")


class OpenAI:
    def generate(self):
        print("Generating response from OpenAI...")

    def embed(self):
        print("Creating embeddings via OpenAI...")

    def speech(self):
        print("Generating speech via OpenAI...")


class Claude:
    def generate(self):
        print("Generating response from Claude...")

    def embed(self):
        print("Creating embeddings via Claude...")


class Ollama:
    def generate(self):
        print("Generating response from Ollama (local)...")


# -------------------------------------------------------
# NOW USE THEM — this is the part students should see
# -------------------------------------------------------

print("--- EC2 Operations ---")
ec2 = EC2Manager()
ec2.create()
ec2.stop()
ec2.delete()
ec2.attach_volume()

print("\n--- Kubernetes Operations ---")
cluster = KubernetesManager()
cluster.create()
cluster.get_pods()
cluster.scale()
cluster.restart()

print("\n--- Docker Operations ---")
docker = DockerManager()
docker.build()
docker.run()
docker.push()

print("\n--- AI Operations ---")
openai = OpenAI()
openai.generate()
openai.embed()
openai.speech()

claude = Claude()
claude.generate()
claude.embed()

ollama = Ollama()
ollama.generate()

# -------------------------------------------------------
# PAUSE AND ASK STUDENTS:
# "Which one was easier to read — demo_01 or this?"
# "Can you immediately tell what ec2.stop() does?"
# "If you want to find all Kubernetes operations — where do you look?"
# "If a new engineer joins — which file would you hand them?"
# -------------------------------------------------------

# -------------------------------------------------------
# KEY TEACHING MOMENT:
# OOP does not reduce the number of lines.
# It ORGANIZES related behavior under one name.
# ec2.stop() reads like a sentence.
# cluster.scale() reads like plain English.
# This is WHY every serious library uses OOP.
# -------------------------------------------------------
