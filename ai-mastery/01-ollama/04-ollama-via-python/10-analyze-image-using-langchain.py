# pip install langchain-ollama langchain-core pillow

import base64
from pathlib import Path
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser

# Step 1: Initialize the vision model using ChatOllama
# Same model as before — llava supports both text and image input.
# temperature=0 for consistent, deterministic responses.
my_llm = ChatOllama(
    model="llava",
    temperature=0
)

# Step 2: Load and encode the image as base64
# LangChain requires images to be sent as base64 encoded strings
# inside the message content with a specific format.
image_path = "sample_invoice.jpg"
image_bytes = Path(image_path).read_bytes()
image_base64 = base64.b64encode(image_bytes).decode("utf-8")

# Step 3: Detect the image type for the media_type field
# LangChain needs to know the image format (jpeg, png, gif, webp)
# so it can correctly format the request to the model.
# Here we hardcode jpeg — in production, detect dynamically using imghdr or Pillow.
image_media_type = "image/jpeg"  # change to image/png for PNG files

print("\n--- LangChain Approach: Analysing image ---")

# Step 4: Create a HumanMessage with both text and image content
# LangChain uses a specific structure for multimodal messages:
# content is a LIST of dictionaries — one for text, one for image.
# This is different from plain text messages where content is just a string.
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "You are a document analysis assistant. Analyse this image and extract: 1) Document type 2) Key fields and values 3) Any amounts or dates mentioned."
            # text part — our instruction/question to the model
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:{image_media_type};base64,{image_base64}"
                # image is sent as a data URL — base64 encoded with media type prefix
                # format: data:<media_type>;base64,<base64_string>
            }
        }
    ]
)

# Step 5: Invoke the model with the multimodal message
# model receives both the text instruction and the image together
ai_response = my_llm.invoke([message])

print("\nDocument Analysis Result:")
print(ai_response.content)


# -------------------------------------------------------------------
# LANGCHAIN CHAIN: Using prompt + model + output parser together
# This is more structured and easier to reuse across different images.
# -------------------------------------------------------------------
print("\n\n--- LangChain Chain approach ---")

def analyse_image_with_question(image_path: str, question: str) -> str:
    """
    Reusable function to analyse any local image with any question.
    Takes image path and question as input, returns model's text response.
    """
    # Load and encode image
    img_bytes = Path(image_path).read_bytes()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    # Build the multimodal message
    msg = HumanMessage(
        content=[
            {"type": "text", "text": question},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}
            }
        ]
    )

    # Chain: model | output parser
    # StrOutputParser extracts plain text from the model's response object
    chain = my_llm | StrOutputParser()

    # invoke the chain with the multimodal message wrapped in a list
    return chain.invoke([msg])


# Use the reusable function with different questions on the same image
result1 = analyse_image_with_question(
    "sample_invoice.jpg",
    "What is the vendor name and invoice number in this document?"
)
print(f"\nQ: Vendor name and invoice number?\nA: {result1}")

result2 = analyse_image_with_question(
    "sample_invoice.jpg",
    "List all line items and their amounts from this invoice."
)
print(f"\nQ: Line items and amounts?\nA: {result2}")


# -------------------------------------------------------------------
# STREAMING RESPONSE with LangChain vision
# For longer analysis tasks, streaming shows output as it is generated
# instead of waiting for the complete response.
# -------------------------------------------------------------------
print("\n\n--- Streaming vision response ---")

stream_message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Give me a detailed description of everything you see in this image."
        },
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}
        }
    ]
)

print("\nStreaming model response:")
# stream() returns chunks as they are generated — better user experience for long outputs
for chunk in my_llm.stream([stream_message]):
    print(chunk.content, end="", flush=True)
print()  # newline after streaming completes