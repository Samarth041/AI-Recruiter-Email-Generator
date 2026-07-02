
import os
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()
from langsmith import Client

client=Client()
client.create_feedback(
    run_id="019f1d74-07f5-7fc1-93d1-1e7aa2d12aed",
    key="tone_quality",
    score=1,  # 1 = good, 0 = bad
    comment="Personalized well, mentioned the right team",
)