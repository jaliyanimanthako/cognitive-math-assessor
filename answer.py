# agents/answer_generation_agent.py
import openai
from prompt import cognitive_prompt

def answer_generation_agent(state: dict) -> dict:

    user_question = state["question"]
    cognitive_level = state["level"]
    history = state.get("chat_history", [])

    MAX_TURNS = 3
    if len(history) > MAX_TURNS * 2:
        history = history[-MAX_TURNS * 2:]

    print(history)

    #prompt = cognitive_prompt.format(question=user_question, level=cognitive_level)
    full_prompt = history + [
        {"role": "user", "content": f"[{cognitive_level}] {user_question}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a pedagogically-aware assistant."},
            *full_prompt
            #{"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    answer = response.choices[0].message["content"].strip()
    updated_history = full_prompt + [{"role": "assistant", "content": answer}]
    return {
        "question": user_question,
        "level": cognitive_level,
        "answer": answer,
        "chat_history": updated_history  
    }

