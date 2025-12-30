from langchain_core.prompts import PromptTemplate

question_prompt = PromptTemplate(
    input_variables=["role", "skills"],
    template="""
You are an experienced technical interviewer.

Generate interview questions for:

Job Role: {role}
Skills: {skills}

Rules:
- 2 Easy questions
- 2 Medium questions
- 1 Hard question
- Only questions, no answers
- Group by difficulty

Format:
Easy:
1.
2.

Medium:
1.
2.

Hard:
1.
"""
)
