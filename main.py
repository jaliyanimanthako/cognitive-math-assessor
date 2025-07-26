from nodes import run_agentic_graph

# CLI
# if __name__ == "__main__":
#     import os
#     from dotenv import load_dotenv
#     load_dotenv()

#     user_input = input("Enter your question: ")
#     result = run_agentic_graph(user_input)
#     print("\nCognitive Level:", result["level"])
#     print("\nAnswer:\n", result["answer"])

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    # initialize state
    state = {
        "question": "",
        "level": "",
        "prev_level": "",
        "answer": "",
        "chat_history": []
    }

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        state["question"] = user_input
        state = run_agentic_graph(state)  # 👈 update: pass whole state

        print(f"\nAI [{state['level']}]: {state['answer']}")
