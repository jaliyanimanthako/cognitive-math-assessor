# agents/answer_generation_agent.py
import openai
from prompt import cognitive_prompt

def answer_generation_agent(state: dict) -> dict:

    user_question = state["question"]
    cognitive_level = state["level"]

    prompt = cognitive_prompt.format(question=user_question, level=cognitive_level)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a pedagogically-aware assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    answer = response.choices[0].message["content"].strip()
    return {
        "answer": answer  # must return a dict with key "answer"
    }
