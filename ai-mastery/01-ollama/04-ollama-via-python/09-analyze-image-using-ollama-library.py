# pip install ollama pillow

import ollama
import base64
from pathlib import Path

# Step 1: Pull the vision model from Ollama
# llava is a multimodal model that can understand both text and images.
# This will download the model (~4GB) if not already present on your machine.
print("Pulling vision model...")
ollama.pull("llava")
print("Model ready!")

# Step 2: Load image from disk and convert to base64
# We read the image file as binary and encode it to base64 string.
# Base64 is a way to represent binary data (like an image) as a text string
# so it can be safely included in a JSON request body.
image_path = "sample_invoice.jpg"  # path to your local image file
image_data = Path(image_path).read_bytes()  # read image as raw bytes
image_base64 = base64.b64encode(image_data).decode("utf-8")  # encode to base64 string

print(f"\nImage loaded: {image_path}")
print(f"Image size: {len(image_data)} bytes")

# Step 3: Send image + question to the vision model
# The images parameter accepts a list of base64-encoded image strings.
# The content in the message is our text question about the image.
# We can ask anything about the image — describe it, extract text, identify objects etc.
print("\n--- Asking: What is in this image? ---")
response = ollama.chat(
    model="llava",
    messages=[
        {
            "role": "user",
            "content": "What is in this image? Describe it in detail.",
            "images": [image_base64]  # list of base64 encoded images
        }
    ]
)

# Step 4: Extract and print the response
# response is a dictionary. The model's reply is in response['message']['content']
print("\nModel Response:")
print(response["message"]["content"])


# -------------------------------------------------------------------
# APPROACH 1B: Sending image directly as file path bytes (simpler way)
# Instead of manually encoding to base64, ollama library also accepts
# raw bytes directly in the images list — even simpler for local files.
# -------------------------------------------------------------------
print("\n\n--- Sending image as raw bytes (simpler approach) ---")

raw_response = ollama.chat(
    model="llava",
    messages=[
        {
            "role": "user",
            "content": "Is there any text visible in this image? If yes, extract all the text you can read.",
            "images": [image_data]  # raw bytes directly — no base64 encoding needed
        }
    ]
)

print("\nText extracted from image:")
print(raw_response["message"]["content"])


# -------------------------------------------------------------------
# MULTI-TURN: Ask follow-up questions about the same image
# Key insight: include the image only in the FIRST message.
# Subsequent messages are text-only follow-ups — model already has context.
# -------------------------------------------------------------------
print("\n\n--- Multi-turn: Follow-up questions about the same image ---")

# Build conversation history with image in first message
conversation = [
    {
        "role": "user",
        "content": "Look at this image carefully and tell me what you see.",
        "images": [image_data]  # image sent only once in the first message
    }
]

# Get first response and add to history
first_response = ollama.chat(model="llava", messages=conversation)
first_reply = first_response["message"]["content"]
print(f"\nModel: {first_reply}")

# Add assistant reply to conversation history
conversation.append({
    "role": "assistant",
    "content": first_reply
})

# Follow-up question — no image needed, model already has context from turn 1
conversation.append({
    "role": "user",
    "content": "What is the total amount mentioned in the document?"
    # no 'images' key here — we are asking a follow-up, not sending a new image
})

follow_up_response = ollama.chat(model="llava", messages=conversation)
print(f"\nFollow-up Answer: {follow_up_response['message']['content']}")