from dotenv import load_dotenv
import os
import openai
from prompt import evaluate_agent_prompt

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
def cognitive_level_agent(state: dict) -> dict:

    
    chat_history = state.get("chat_history", [])
    
    chat_history = chat_history + [
        {"role": "user", "content": state["question"]},
        {"role": "assistant", "content": state["answer"]}
    ]

    # If chat is empty (first turn), use current question
    if not chat_history:
        chat_history = [{"role": "user", "content": state["question"]}]
    conversation = "\n".join(f"{m['role'].capitalize()}: {m['content']}" for m in chat_history)

    full_prompt = evaluate_agent_prompt.format(conversation=conversation)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful cognitive assessment agent."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=100,
        temperature=0.0
    )

    level = response.choices[0].message["content"].strip()
    
    return {"level": level}