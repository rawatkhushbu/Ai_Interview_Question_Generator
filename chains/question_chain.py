from langchain_groq import ChatGroq
from prompts.question_prompt import question_prompt

def get_question_chain():
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.6
    )

    chain = question_prompt | llm
    return chain
