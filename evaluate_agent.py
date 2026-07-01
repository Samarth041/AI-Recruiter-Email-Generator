from langsmith import evaluate
from recruiter_agent_metadata import app

def target_function(inputs:dict)->dict:
    """Langsmith passes one examples from the dataset . We invoke our Langgraph app and return the generated email."""

    result=app.invoke(inputs)

    return {
        "email":result["email"]
    }

#-----------------------------------------------------------
#Evaluator 1

def under_word_limit(run,example):
    email=run.outputs["email"]

    words=len(email.split())

    return {
        "key":"under_120_words",
        "score":words<=120
    }

#---------------------------------------------------------------------
#Evaluator 2
def mentions_company(run,example):
    email=run.outputs["email"]

    company=example.inputs["company"]

    return {
        "key":"mentions_company",
        "score":company.lower() in email.lower()
    }


#----------------------------------------------------------------------
#Evaluator 3
def has_contact_name(run,example):
    email=run.outputs["email"]

    contact=example.inputs["contact_name"]

    return{
        "key":"has_contact_name",
        "score":contact.lower() in email.lower()
    }


#------------------------------------------------------------------

#Run evaluation


if __name__=="__main__":

    results=evaluate(
        target_function,
        #dataset name in LangSmith

        data="recruiter-email-generator-set",

        evaluators=[
            under_word_limit,
            mentions_company,
            has_contact_name
        ]
        
    )

    print(results)