from nodes import run_agentic_graph

# CLI
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    user_input = input("Enter your question: ")
    result = run_agentic_graph(user_input)
    print("\nCognitive Level:", result["level"])
    print("\nAnswer:\n", result["answer"])
