# demo_03_real_libraries_oop.py
# ============================================================
# VIDEO DEMO — Part 6
# Show students: "You are ALREADY using OOP every day"
# These are REAL library usage patterns (not runnable without keys)
# Show these as READ-ONLY code — explain each line
# ============================================================

# -------------------------------------------------------
# NOTE FOR TEACHER:
# Do NOT run this file — it requires real AWS keys,
# Kubernetes config, OpenAI keys, etc.
# Just open it and SHOW the code while explaining.
# The point is: spot the OOP pattern in each library.
# -------------------------------------------------------


# ===========================================================
# BOTO3 — AWS SDK for Python
# ===========================================================
# pip install boto3

# import boto3

# ec2 = boto3.client("ec2")               # <-- Creating an OBJECT called ec2
#                                          # boto3.client() returns an EC2 object
#
# ec2.run_instances(                       # <-- Calling a METHOD on that object
#     ImageId="ami-0abcdef1234567890",
#     InstanceType="t2.micro",
#     MinCount=1,
#     MaxCount=1
# )
#
# ec2.describe_instances()                 # <-- Another METHOD on the same object
# ec2.stop_instances(InstanceIds=["i-1234567890abcdef0"])
# ec2.terminate_instances(InstanceIds=["i-1234567890abcdef0"])

# TEACH:
# ec2 is an OBJECT
# run_instances, describe_instances, stop_instances are METHODS
# They are all grouped under the ec2 object — exactly like our EC2Manager class
# boto3 just calls it client() instead of class


# ===========================================================
# KUBERNETES PYTHON CLIENT
# ===========================================================
# pip install kubernetes

# from kubernetes import client, config
#
# config.load_kube_config()
#
# v1 = client.CoreV1Api()                 # <-- Creating an OBJECT called v1
#
# pods = v1.list_namespaced_pod(          # <-- Calling a METHOD
#     namespace="default"
# )
#
# for pod in pods.items:
#     print(pod.metadata.name)
#
# v1.delete_namespaced_pod(              # <-- Another METHOD on the same object
#     name="my-pod",
#     namespace="default"
# )

# TEACH:
# v1 is an object of type CoreV1Api
# list_namespaced_pod, delete_namespaced_pod are its methods
# ALL pod operations live under the v1 object — just like our KubernetesManager


# ===========================================================
# OPENAI SDK
# ===========================================================
# pip install openai

# from openai import OpenAI
#
# client = OpenAI(api_key="your-api-key")     # <-- Creating an OBJECT called client
#
# response = client.responses.create(          # <-- METHOD call
#     model="gpt-4o",
#     input="What is Kubernetes?"
# )
# print(response.output_text)
#
# embedding = client.embeddings.create(        # <-- Another METHOD, same object
#     model="text-embedding-3-small",
#     input="DevOps automation"
# )

# TEACH:
# client is an OpenAI object
# responses.create and embeddings.create are methods
# Notice: client.responses.create and client.embeddings.create
# Two different "sub-objects" (responses, embeddings) — nested OOP


# ===========================================================
# ANTHROPIC SDK
# ===========================================================
# pip install anthropic

# import anthropic
#
# client = anthropic.Anthropic(api_key="your-api-key")   # <-- OBJECT
#
# message = client.messages.create(                        # <-- METHOD
#     model="claude-sonnet-4-6",
#     max_tokens=1024,
#     messages=[
#         {"role": "user", "content": "Explain Docker in 2 lines"}
#     ]
# )
# print(message.content[0].text)


# ===========================================================
# LANGCHAIN — Most popular GenAI framework
# ===========================================================
# pip install langchain langchain-openai

# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(                        # <-- Creating an OBJECT called llm
#     model="gpt-4o",
#     temperature=0.7
# )
#
# response = llm.invoke(                   # <-- METHOD call
#     "Explain the difference between Docker and Kubernetes"
# )
# print(response.content)

# TEACH:
# llm is a ChatOpenAI object
# invoke() is its method
# Want to switch to Claude? Just swap the class — same method name:
#
# from langchain_anthropic import ChatAnthropic
# llm = ChatAnthropic(model="claude-sonnet-4-6")  # different class
# response = llm.invoke("Same question")           # SAME method!
#
# This is the POWER of OOP — multiple classes, same interface
# (This concept is called polymorphism — but we will cover that later)


# ===========================================================
# LANGGRAPH — Agent framework
# ===========================================================
# pip install langgraph

# from langgraph.graph import StateGraph
#
# graph = StateGraph(...)           # <-- OBJECT
# graph.add_node(...)               # <-- METHOD
# graph.add_edge(...)               # <-- METHOD
# graph.compile()                   # <-- METHOD
# graph.invoke({"input": "..."})    # <-- METHOD


# ===========================================================
# PATTERN RECOGNITION — What did you notice?
# ===========================================================

# Every library follows the SAME pattern:
#
#   something = LibraryClass()     # Create an object
#   something.do_action()          # Call a method on it
#
# That is OOP.
# You have been reading it, using it, and building on it.
# Now you know what it is called — and next video,
# you will build it yourself from scratch.


# ===========================================================
# SUMMARY TABLE (point to this while teaching)
# ===========================================================

libraries = {
    "boto3":                 "ec2 = boto3.client('ec2') → ec2.run_instances()",
    "Kubernetes Client":     "v1 = client.CoreV1Api() → v1.list_namespaced_pod()",
    "OpenAI SDK":            "client = OpenAI() → client.responses.create()",
    "Anthropic SDK":         "client = anthropic.Anthropic() → client.messages.create()",
    "LangChain":             "llm = ChatOpenAI() → llm.invoke()",
    "LangGraph":             "graph = StateGraph() → graph.add_node()",
    "CrewAI":                "crew = Crew() → crew.kickoff()",
    "Azure SDK":             "compute = ComputeManagementClient() → compute.virtual_machines.list()",
    "Google Cloud SDK":      "storage = storage.Client() → storage.list_buckets()",
}

print("Libraries you already use that are built on OOP:\n")
for library, example in libraries.items():
    print(f"  {library}")
    print(f"    {example}")
    print()
