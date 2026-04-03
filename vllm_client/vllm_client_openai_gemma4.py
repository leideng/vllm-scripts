from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="google/gemma-4-31B-it",
    messages=[
        {"role": "user", "content": "If 2x+3y=10, 3x-4y=-2; then what is x and y?"}
    ],
    max_tokens=512,
    temperature=0.7
)

print(response.choices[0].message.content)
