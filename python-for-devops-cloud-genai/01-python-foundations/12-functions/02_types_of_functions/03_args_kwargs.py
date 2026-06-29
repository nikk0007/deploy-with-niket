# ============================================================
# SECTION 3 — *ARGS AND **KWARGS
# Python for DevOps, Cloud & GenAI | Types of Functions
# ============================================================

print("=" * 55)
print("  *ARGS & **KWARGS — DevOps Examples")
print("=" * 55)

# ----- *args — Variable positional arguments -----
def deploy_to_environments(*environments):
    """Deploy to any number of environments."""
    print(f"\n🚀 Deploying to {len(environments)} environment(s):")
    for env in environments:
        print(f"  ✅ Deploying to: {env}...")


print("\n📌 *args — deploy_to_environments():")
deploy_to_environments("dev")
deploy_to_environments("dev", "staging")
deploy_to_environments("dev", "staging", "prod")

# What *args actually is
def show_args_type(*args):
    print(f"\n  Type of *args: {type(args)}")
    print(f"  Value: {args}")

print("\n📌 *args is actually a TUPLE:")
show_args_type("dev", "staging", "prod")


# ----- **kwargs — Variable keyword arguments -----
def create_ec2_instance(**config):
    """Create EC2 instance with flexible config."""
    print("\n🖥️  Creating EC2 instance with config:")
    for key, value in config.items():
        print(f"  {key}: {value}")


print("\n📌 **kwargs — create_ec2_instance():")
create_ec2_instance(instance_type="t3.micro", region="ap-south-1", ami_id="ami-0abc123")
print()
create_ec2_instance(instance_type="c5.large", region="us-east-1")

# What **kwargs actually is
def show_kwargs_type(**kwargs):
    print(f"\n  Type of **kwargs: {type(kwargs)}")
    print(f"  Value: {kwargs}")

print("\n📌 **kwargs is actually a DICT:")
show_kwargs_type(region="ap-south-1", instance_type="t3.micro")


# ----- Combining all three -----
def full_deploy(project_name, *environments, **options):
    """Full deployment function combining regular arg, *args, and **kwargs."""
    print(f"\n📦 Project:      {project_name}")
    print(f"🌍 Environments: {environments}")
    print(f"⚙️  Options:      {options}")


print("\n📌 Combined — regular + *args + **kwargs:")
full_deploy(
    "payment-service",          # regular arg
    "dev", "staging", "prod",   # *args
    docker_tag="v2.1",          # **kwargs
    rollback=True
)

print("\n✅ ORDER RULE: regular args → *args → **kwargs")
print("   Ulta kiya toh Python error dega!")
