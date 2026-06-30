import os
from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI

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

class EmailState(TypedDict):
    company:str
    role:str
    contact_name:str
    research:str
    email:str

def research_company(state:EmailState)->dict:
    prompt=f"In 2 sentences , what does {state['company']} do,and why would they hire from a university placement cell?"
    result=llm.invoke(prompt)
    return {"research":result.content}

def write_email(state:EmailState)->dict:
    prompt = f"""
You are an assistant for a UNIVERSITY PLACEMENT CELL.

Your job is to write recruiter outreach emails FROM THE PLACEMENT CELL to external company HRs/recruiters.

IMPORTANT ROLE CONTEXT:
- We are NOT a company.
- We are NOT applying for a job.
- We are a placement cell representing students.
- We are contacting companies to request recruitment opportunities for students.

TASK:
Write a short, professional recruiter outreach email to a company HR/contact person.

DETAILS:
- Contact Person: {state['contact_name']}
- Company: {state['company']}
- Role we are pitching students for: {state['role']}

Company Context (for understanding the company):
{state['research']}

RULES:
- Keep under 120 words
- Professional tone
- No fluff
- Do NOT pretend to be the company
- Do NOT mention fake job applications
- You are representing a placement cell seeking hiring opportunities for students

Write the email:
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

if __name__=="__main__":
    result=app.invoke({
        "company":"Staqu Technologies",
        "role":"ML Engineer Intern",
        "contact_name":"Priya Sharma",
    })

    print(result["email"])