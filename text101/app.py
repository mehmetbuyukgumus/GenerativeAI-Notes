from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

my_keys = os.getenv("openai_api_key")

client = OpenAI(api_key=my_keys)

AI_response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    temperature=0,
    max_tokens=256,
    messages=[
        {"role": "systme","content": "Sen yardımsever bir asistansın"},
        {"role": "user", "content": "Mevsimler neden oluşur? Dünya kendi etrafında döndüğü için mi?"}
    ]

)

print(AI_response.choices[0].message.content)