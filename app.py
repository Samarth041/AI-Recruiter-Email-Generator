import streamlit as st

from recruiter_agent import app
from langchain_core.runnables import RunnableConfig

st.set_page_config(
    page_title="JNU Recruitrt Email Generator",
    page_icon="📧",
    layout="wide"
)

st.title("📧 AI Recruiter Email Generator")

st.write(
    "Generate personalised recruiter outreach emails"
)

st.divider()

company=st.text_input("Company Name ")

contact_name=st.text_input("Recruiter / HR name  ")

role=st.text_input("Role  ")

if st.button("Generate Email "):
    if not company or not contact_name or not role:
        st.warning("Please fill all fields..")

    else:
        state={
            "company":company,
            "contact_name":contact_name,
            "role":role,

            #optional metadata

            "company_type":"Unknown",
            "outreach_wave":"streamlit"
        }

        config=RunnableConfig(
            tags=["streamlit-ui"],
            metadata={
                "company":company,
                "company_type": "Unknown",
                "source": "streamlit",
            }
        )

        with st.spinner("Researching Company ...."):
            result=app.invoke(state,config=config)

        st.success("Email Generated")

        st.subheader("Generated Email ")

        st.text_area(
            "",
            value=result["email"],
            height=350
        )