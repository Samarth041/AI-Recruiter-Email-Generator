import os
from dotenv import load_dotenv

load_dotenv(override=True)

print("API KEY :", os.getenv("LANGSMITH_API_KEY"))
print("ENDPOINT:", os.getenv("LANGSMITH_ENDPOINT"))
print("PROJECT :", os.getenv("LANGSMITH_PROJECT"))
print("TRACING :", os.getenv("LANGSMITH_TRACING"))