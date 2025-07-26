from dotenv import load_dotenv
import os
import openai
from prompt import evaluate_agent_prompt

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
def cognitive_level_agent(user_question: str) -> dict:
    """
    This function uses OpenAI's API to analyze a user's question and determine its cognitive level.

    Args:
    user_question (str): The question posed by the user.

    Returns:
    str: The formatted string showing the question and cognitive level.
    """
    # Append the user question to the prompt
    full_prompt = evaluate_agent_prompt.format(user_question = user_question)

    # Use OpenAI's API to get the model's response via the chat-completions endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the model
        messages=[
            {"role": "system", "content": "You are a helpful cognitive assessment agent."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=100,  # Limit the response length
        temperature=0.0  # Set temperature to 0 for deterministic results
    )

    # Extract and return the response from the model
    level = response.choices[0].message["content"].strip()
    return {"level": level}

