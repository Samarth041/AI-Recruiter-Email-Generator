import os
from dotenv import load_dotenv
load_dotenv()


from langsmith import Client
client=Client()


DATASET_NAME = "recruiter-email-generator-set"

#create or reuse dataset

try:
    dataset=client.read_dataset(dataset_name=DATASET_NAME)
    print(f"DataSet '{DATASET_NAME}' already exists.")
except Exception:
    dataset=client.create_dataset(
        dataset_name=DATASET_NAME,
        description="Real companies from JNU Placement Cell outreach with manually approved recruiter emails.",
    )

    print(f"Created dataset '{DATASET_NAME}'")

#examples-----------------------------------------------



examples=[

    #---Samsung-------
    {
        "inputs": {
            "company": "Samsung",
            "role": "Machine Learning Engineer Intern",
            "contact_name": "Priya Sharma",
        },
        "outputs": {
            "email": """Dear Priya Ma'am,

    Greetings from the Placement Cell, School of Engineering, Jawaharlal Nehru University (JNU)!

    We are reaching out to explore recruitment opportunities with Samsung for our pre-final and final year B.Tech students, particularly for Machine Learning Engineer internship roles.

    Samsung has consistently been at the forefront of innovation in AI, semiconductor technologies, consumer electronics, and intelligent devices. Our students have strong academic and practical experience in Python, Machine Learning, Deep Learning, Computer Vision, and Data Structures & Algorithms, enabling them to contribute effectively to engineering teams working on next-generation AI products.

    About JNU

    • NAAC A++ Accredited (3.91/4)
    • NIRF Rank 2 among Indian Universities
    • President's Award for Best University

    Our School of Engineering offers B.Tech, Dual Degree, M.Tech and PhD programs in Computer Science and Electronics & Communication.

    We would be delighted to discuss internship opportunities, campus recruitment drives, or any hiring initiatives that align with Samsung's requirements. We have attached our placement brochure for your reference.

    Thank you for your time, and we look forward to the possibility of collaborating with Samsung.

    Warm regards,

    Samarth Gupta
    Placement Cell
    School of Engineering
    Jawaharlal Nehru University"""
        }
    },

    #------Google-----------
    {
        "inputs": {
            "company": "Google",
            "role": "Software Engineering Intern",
            "contact_name": "Rahul Verma",
        },
        "outputs": {
            "email": """Dear Rahul Sir,

    Greetings from the Placement Cell, School of Engineering, Jawaharlal Nehru University (JNU)!

    We would like to explore internship and full-time recruitment opportunities with Google for our Computer Science and Electronics students.

    Google's work across Search, Cloud, AI, Android, and distributed systems inspires students worldwide. Our students possess strong foundations in Data Structures & Algorithms, System Design fundamentals, Backend Development, Cloud Computing, Machine Learning, and Open Source technologies that align well with Google's engineering culture.

    JNU has consistently been recognized among India's leading universities with NAAC A++ accreditation and top NIRF rankings.

    We would be grateful for the opportunity to connect with the appropriate hiring team and discuss how our students can contribute to Google's engineering organization.

    Please find our placement brochure attached.

    Warm regards,

    Samarth Gupta
    Placement Cell
    School of Engineering
    Jawaharlal Nehru University"""
        }
    },


    #------Nanonets-------------
    {
            "inputs": {
                "company": "Nanonets",
                "role": "AI Engineer Intern",
                "contact_name": "Ankit Gupta",
            },
            "outputs": {
                "email": """Dear Ankit Sir,

        Greetings from the Placement Cell, School of Engineering, Jawaharlal Nehru University (JNU)!

        We are writing to explore internship opportunities with Nanonets for our students interested in AI Engineering and Machine Learning.

        Nanonets has built an impressive platform around intelligent document processing and AI automation. Our students have hands-on experience in Python, Deep Learning, Computer Vision, LLM applications, OCR pipelines, FastAPI, and cloud deployment through academic and personal projects, making them strong candidates for your engineering teams.

        Our School of Engineering admits students through JEE and offers rigorous training in Computer Science and Electronics.

        We would appreciate the opportunity to connect with your recruitment team and explore internship collaborations. Our placement brochure has been attached for your reference.

        Warm regards,

        Samarth Gupta
        Placement Cell
        School of Engineering
        Jawaharlal Nehru University"""
        }
    },
    #--------------BEtterPlace-----------------
    {
        "inputs": {
            "company": "BetterPlace",
            "role": "Backend Engineering Intern",
            "contact_name": "Neha Singh",
        },
        "outputs": {
            "email": """Dear Neha Ma'am,

    Greetings from the Placement Cell, School of Engineering, Jawaharlal Nehru University (JNU)!

    We would like to explore recruitment opportunities for our students with BetterPlace for Backend Engineering internship roles.

    BetterPlace has established itself as a leader in workforce management and HR technology. Our students have developed strong technical expertise in Java, Python, REST APIs, Databases, Backend Systems, Cloud Technologies, and Software Engineering through coursework and practical projects, making them well aligned with technology-driven organizations like BetterPlace.

    JNU continues to be recognized as one of India's premier universities with excellent academic standards and research culture.

    We would be grateful for an opportunity to discuss internship hiring, campus recruitment, or other collaboration opportunities.

    Warm regards,

    Samarth Gupta
    Placement Cell
    School of Engineering
    Jawaharlal Nehru University"""
        }
    },
    #----------------Staqu technologies---------------------
    {
        "inputs": {
            "company": "Staqu Technologies",
            "role": "Computer Vision Intern",
            "contact_name": "Rohit Sharma",
        },
        "outputs": {
            "email": """Dear Rohit Sir,

    Greetings from the Placement Cell, School of Engineering, Jawaharlal Nehru University (JNU)!

    We are reaching out to explore internship opportunities with Staqu Technologies for our students interested in Computer Vision and Artificial Intelligence.

    Staqu's work in AI-powered video analytics, surveillance, and computer vision solutions closely aligns with the technical interests of many of our students. They have developed strong skills in Python, OpenCV, Deep Learning, Object Detection, Image Processing, and Machine Learning through academic coursework and industry-oriented projects.

    Our students are eager to contribute to real-world AI products while gaining valuable industry experience.

    We would appreciate the opportunity to discuss how JNU students can contribute to Staqu Technologies through internships or campus hiring. Our placement brochure is attached for your reference.

    Warm regards,

    Samarth Gupta
    Placement Cell
    School of Engineering
    Jawaharlal Nehru University"""
        }
    }
    
]

client.create_examples(dataset_id=dataset.id,examples=examples)

print(f"Dataset '{dataset.name}' created successfully!")
print(f"Added {len(examples)} examples.")