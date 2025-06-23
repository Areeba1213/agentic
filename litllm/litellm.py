# agent_example.py
from litellm import completion

response = completion(
    model="openai/gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Give me 3 healthy snacks."}],
)
print(response["choices"][0]["message"]["content"])
