from langgraph.graph import StateGraph, END
from evaluater import cognitive_level_agent
from answer import answer_generation_agent
from typing import TypedDict

class State(TypedDict):
    question: str
    level: str
    prev_level: str 
    answer: str
    chat_history: list

def run_agentic_graph(input_state: State) -> State:
    def level_number(level_str: str) -> int:
        try:
            return int(level_str.strip().replace('"Level": Level ', ''))
        except:
            return 1  # default if malformed

    def assess_cognitive_level_node(state: State) -> State:
        result = cognitive_level_agent(state)
        new_level = result["level"]
        prev_level = state.get("level", "")

        # Downgrade logic
        if prev_level:
            if level_number(new_level) > level_number(prev_level):
                new_level = prev_level  # prevent upgrade
        else:
            prev_level = new_level  # initial turn

        return {
            **state,
            "level": new_level,
            "prev_level": prev_level
        }

    def generate_answer_node(state: State) -> State:
        return answer_generation_agent(state)

    graph = StateGraph(state_schema=State)
    graph.add_node("AssessCognitiveLevel", assess_cognitive_level_node)
    graph.add_node("GenerateAnswer", generate_answer_node)
    graph.set_entry_point("AssessCognitiveLevel")
    graph.add_edge("AssessCognitiveLevel", "GenerateAnswer")
    graph.set_finish_point("GenerateAnswer")

    app = graph.compile()
    return app.invoke(input_state)

