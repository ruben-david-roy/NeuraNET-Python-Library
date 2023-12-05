# 🌐 NeuraNET Python API library

The Official NeuraNET Python Library

---

## 🛠 Installation

To get started with the library, simply run the following command:

```bash
pip install neuranet
```

## 💬 Chat Usage
Using the Chat AIs library is straightforward. Below is an example of a conversation:
```python
import neuranet

api_key = "YOUR_API_KEY_HERE"
mode = 'chat'
client = neuranet.client(api_key, mode)

# Set up the conversation history and model
conversation_history = [
    {"sender": "instruct", "content": "You are a helpful assistant."},
    {"sender": "user", "content": "Hello."},
    {"sender": "assistant", "content": "Hello, how can I assist you?"},
    {"sender": "user", "content": "How are you?"}
]

model = "nlite"  # options: nlite, npro, npro-vision

# Get the response
try:
    response = client.generate(conversation_history, model)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")
```

## 🎨 Image Usage
Using the Image generation AIs library is straightforward. Below is an example of a conversation:
```python
import neuranet

api_key = "YOUR_API_KEY_HERE"
mode = 'image'
client = neuranet.client(api_key, mode)
model = "vinci-mini" # options: vinci-mini, vinci-max

prompt = "A large oak tree"

response = client.generate(prompt, model)
print(response)
```
