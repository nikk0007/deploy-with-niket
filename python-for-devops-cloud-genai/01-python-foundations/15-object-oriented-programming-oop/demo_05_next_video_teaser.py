# demo_05_next_video_teaser.py
# ============================================================
# VIDEO DEMO — End of Video (Part 8 / Cliffhanger)
# Show this at the END of the video as a teaser for Video 2
# Say: "Next video, WE WILL BUILD THIS from scratch — line by line"
# ============================================================

# -------------------------------------------------------
# THIS is what we will build in Video 2
# Right now — just show them how it is USED
# Do NOT explain class, self, __init__ yet
# -------------------------------------------------------

class EC2Manager:
    def __init__(self, region="ap-south-1"):
        self.region = region
        print(f"EC2Manager initialized for region: {self.region}")

    def create(self, instance_type="t2.micro"):
        print(f"Creating {instance_type} EC2 instance in {self.region}...")

    def stop(self, instance_id):
        print(f"Stopping instance {instance_id} in {self.region}...")

    def delete(self, instance_id):
        print(f"Terminating instance {instance_id} in {self.region}...")

    def list_instances(self):
        print(f"Listing all instances in {self.region}...")

    def create_snapshot(self, instance_id):
        print(f"Creating snapshot of {instance_id}...")


# -------------------------------------------------------
# SHOW the USAGE — this is what students already understand
# -------------------------------------------------------

print("=== Mumbai Region ===")
mumbai_ec2 = EC2Manager(region="ap-south-1")
mumbai_ec2.create(instance_type="t3.medium")
mumbai_ec2.list_instances()
mumbai_ec2.stop(instance_id="i-0abc123")
mumbai_ec2.create_snapshot(instance_id="i-0abc123")
mumbai_ec2.delete(instance_id="i-0abc123")

print("\n=== US East Region ===")
us_ec2 = EC2Manager(region="us-east-1")
us_ec2.create(instance_type="t2.micro")
us_ec2.list_instances()

# -------------------------------------------------------
# KEY MOMENT — point at the screen and say:
#
# "Notice something interesting here."
# "We created TWO separate EC2Manager objects."
# "One for Mumbai. One for US East."
# "Each one remembers its OWN region."
# "mumbai_ec2.create() knows it is in Mumbai."
# "us_ec2.create() knows it is in US East."
# "Functions cannot do this without passing region every single time."
# "Classes REMEMBER things. That's another reason they exist."
#
# Then say:
# "How does a class 'remember' things?
#  What is __init__? What is self? What is self.region?"
# "That is EXACTLY what we will build from scratch in the next video."
# -------------------------------------------------------


# -------------------------------------------------------
# QUESTIONS TO LEAVE THE AUDIENCE WITH (show on screen):
# -------------------------------------------------------

print("\n" + "="*60)
print("Questions for the next video:")
print("="*60)
print()
print("  1. What is 'class EC2Manager' — what does this line do?")
print("  2. What is __init__? Why does every class seem to have it?")
print("  3. What is 'self'? Why does it appear in every method?")
print("  4. How does mumbai_ec2 'remember' its region?")
print("  5. What exactly is mumbai_ec2 — is it a class or something else?")
print()
print("  Next video: We build EC2Manager from a blank Python file.")
print("  Line 1 to last line. No shortcuts.")
print("="*60)
