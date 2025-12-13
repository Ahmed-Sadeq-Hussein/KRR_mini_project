from ollama import chat
from ollama import ChatResponse

with open("query.txt", "r", encoding="utf-8") as f:
    prompt_text = f.read()

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': prompt_text,
  },
])
print(response['message']['content'])