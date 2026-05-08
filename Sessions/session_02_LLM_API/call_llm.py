from groq import Groq  # pip install groq
from my_api_key import api_key  # Importing the API key from a separate file for security reasons

client = Groq(api_key=api_key)

prompt=input("Ask groq about Geography: ")
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",

    messages=[
        {"role": "system", "content": "You are a Geography assistant."},
        {"role": "user", "content": prompt}
    ],

    temperature=0.7,        # creativity (0 = deterministic, 1+ = creative)
    top_p=0.9,              # nucleus sampling
    max_tokens=200,         # output length limit
    frequency_penalty=0.0,  # reduces repetition
    presence_penalty=0.0,   # encourages new topics
    stop=None               # optional stop sequences
)

print(response.choices[0].message.content)