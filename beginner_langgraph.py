"""Beginner-friendly LangGraph example.

Run:
    python beginner_langgraph.py
"""

from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, StateGraph


class WorkflowState(TypedDict):
    user_input: str
    processed: str


def add_greeting(state: WorkflowState) -> WorkflowState:
    """First node: add a greeting to the input."""
    return {
        "user_input": state["user_input"],
        "processed": f"Hello! You said: {state['user_input']}",
    }


def add_summary(state: WorkflowState) -> WorkflowState:
    """Second node: summarize the processed text."""
    summary = f"Summary length: {len(state['processed'])} characters."
    return {
        "user_input": state["user_input"],
        "processed": f"{state['processed']}\n{summary}",
    }


def build_graph() -> StateGraph:
    graph = StateGraph(WorkflowState)

    graph.add_node("greeting", add_greeting)
    graph.add_node("summary", add_summary)

    graph.set_entry_point("greeting")
    graph.add_edge("greeting", "summary")
    graph.add_edge("summary", END)

    return graph


def main() -> None:
    graph = build_graph().compile()
    result = graph.invoke({"user_input": "I want to learn LangGraph."})
    print("Final state:")
    print(result["processed"])


if __name__ == "__main__":
    main()
