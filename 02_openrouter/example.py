# openrouter_example.py
import openai

openai.api_key = "your-openrouter-key"
openai.api_base = "https://openrouter.ai/api/v1"

response = openai.ChatCompletion.create(
    model="mistralai/mistral-7b-instruct",
    messages=[{"role": "user", "content": "Hello, who are you?"}]
)

print(response.choices[0].message["content"])
