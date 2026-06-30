import os
from dotenv import load_dotenv
load_dotenv()

import langsmith as ls

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableConfig
from typing import TypedDict
from langgraph.graph import StateGraph, END
#-----------------------Hf model-------------------------
hf_token=os.getenv("HF_TOKEN")
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational",
    huggingfacehub_api_token=hf_token,
    temperature=0.7
)
llm = ChatHuggingFace(llm=llm)

#---------------------------------------------------------

#---------------------Google Gemini Model-------------------------------
#llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)
#-----------------------------------------------------------------------

#state
class EmailState(TypedDict):
    company:str
    role:str
    contact_name:str
    research:str
    email:str

    outreach_wave:str
    company_type:str
    
# node 1
@ls.traceable(name="Research Company", run_type="chain")
def research_company(state:EmailState)->dict:

    prompt=f"In 2 sentences , what does {state['company']} do,and why would they hire from a university placement cell?"
    result=llm.invoke(prompt)
    return {"research":result.content}


#Node 2
@ls.traceable(name="Write Email", run_type="chain")
def write_email(state:EmailState)->dict:

    prompt = f"""
You are writing on behalf of a university placement cell.

Write a professional outreach email to {state['contact_name']} at {state['company']}.

Purpose: Request recruitment opportunities for our students for the role of {state['role']}.

Company context:
{state['research']}

Rules:
- We are the placement cell, NOT the company.
- Do not pretend we are hiring.
- Mention how our students could be a good fit based on the company context.
- Keep it under 120 words.
- Professional and personalized.
"""

    result=llm.invoke(prompt)
    return {"email":result.content}

graph=StateGraph(EmailState)

graph.add_node("research",research_company)
graph.add_node("write",write_email)

graph.set_entry_point("research")

graph.add_edge("research","write")
graph.add_edge("write",END)

app=graph.compile()

#batch run

companies = [
    {
        "company": "Samsung",
        "contact_name": "Priya Sharma",
        "role": "ML Engineer Intern",
        "outreach_wave": "first-contact",
        "company_type": "MNC",
    },
    {
        "company": "Google",
        "contact_name": "Rahul Verma",
        "role": "Software Engineer Intern",
        "outreach_wave": "follow-up",
        "company_type": "MNC",
    },
    {
        "company": "Nanonets",
        "contact_name": "Ankit Gupta",
        "role": "AI Engineer Intern",
        "outreach_wave": "first-contact",
        "company_type": "Startup",
    },
    {
        "company": "BetterPlace",
        "contact_name": "Neha Singh",
        "role": "Backend Intern",
        "outreach_wave": "follow-up",
        "company_type": "Startup",
    },
    {
        "company": "Staqu Technologies",
        "contact_name": "Rohit Sharma",
        "role": "Computer Vision Intern",
        "outreach_wave": "follow-up",
        "company_type": "Startup",
    },
]



if __name__=="__main__":
    for company in companies:

        config = RunnableConfig(
            tags=[company["outreach_wave"]],
            metadata={
                "company": company["company"],
                "company_type": company["company_type"],
            },
        )

        result=app.invoke(company,config=config)

        print("="*70)
        print(company["company"])
        print(result["email"])