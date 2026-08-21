import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY", "gsk_your_actual_key_here"))
models = client.models.list()

for m in models.data:
    print(m.id)