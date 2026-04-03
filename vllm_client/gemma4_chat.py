from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="google/gemma-4-E4B-it",
    messages=[
        {"role": "user", "content": "If 2x+3y=10, 3x-4y=-2; then what is x and y?"}
    ],
    max_tokens=2048,
    temperature=0.7
)

print("="*50+"whole message"+"="*50)
print(response)

print("="*50+"response"+"="*50)
print(response.choices[0].message.content)
