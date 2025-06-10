import requests
import webbrowser
import os

# Prompt input from user
prompt = input("Enter a prompt to generate an image: ")

# Your Stability AI API key
api_key = "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"  # Replace with your actual key

# Stability Core API endpoint (returns image directly)
url = "https://api.stability.ai/v2beta/stable-image/generate/core"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "image/*"  # ✅ CORRECTED: Accept image of any type
}

# Send as multipart/form-data
files = {
    "prompt": (None, prompt),
    "output_format": (None, "png"),
}

response = requests.post(url, headers=headers, files=files)

# Save and open image
if response.status_code == 200:
    image_path = "generated_image.png"
    with open(image_path, "wb") as f:
        f.write(response.content)
    print(f"✅ Image saved as: {image_path}")
    webbrowser.open('file://' + os.path.realpath(image_path))
else:
    print("❌ Request failed:", response.status_code)
    print(response.text)