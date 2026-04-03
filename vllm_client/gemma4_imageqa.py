import base64
from openai import OpenAI

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY"
)

# Path to your local images
image_path_1 = "figs/1200px-Cat03.jpg"
image_path_2 = "figs/1200px-Cat_November_2010-1a.jpg"

# Getting the base64 strings
base64_image_1 = encode_image(image_path_1)
base64_image_2 = encode_image(image_path_2)

response = client.chat.completions.create(
    model="google/gemma-4-E4B-it",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_1}"
                    }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_2}"
                    }
                },
                {
                    "type": "text",
                    "text": "What are the key similarities and differences between these two images?"
                }
            ]
        }
    ],
    max_tokens=2048
)

print("="*50+"whole message"+"="*50)
print(response)

print("="*50+"response"+"="*50)
print(response.choices[0].message.content)
