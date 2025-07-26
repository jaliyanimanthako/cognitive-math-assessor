from langgraph.graph import StateGraph, END
from evaluater import cognitive_level_agent
from answer import answer_generation_agent
from typing import TypedDict

class State(TypedDict):
    question: str
    level: str
    answer: str

def run_agentic_graph(user_question: str):
    def assess_cognitive_level_node(state: State) -> State:
        return {**state, **cognitive_level_agent(state["question"])}

    def generate_answer_node(state: State) -> State:
        return answer_generation_agent(state)

    graph = StateGraph(state_schema=State)  
    graph.add_node("AssessCognitiveLevel", assess_cognitive_level_node)
    graph.add_node("GenerateAnswer", generate_answer_node)

    graph.set_entry_point("AssessCognitiveLevel")
    graph.add_edge("AssessCognitiveLevel", "GenerateAnswer")
    graph.set_finish_point("GenerateAnswer")

    app = graph.compile()

    input_state: State = {"question": user_question, "level": "", "answer": ""}
    final_state = app.invoke(input_state)

    return final_state

