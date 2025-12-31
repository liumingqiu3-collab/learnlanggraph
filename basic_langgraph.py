"""LangGraph beginner example: a tiny state machine.

Install dependencies:
  pip install langgraph langchain-core

Run:
  python basic_langgraph.py
"""

from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, StateGraph


class State(TypedDict):
    """Graph state shared between nodes."""

    text: str


def greet(state: State) -> State:
    """First node: create a greeting."""

    return {"text": "Hello from LangGraph!"}


def shout(state: State) -> State:
    """Second node: transform the text."""

    return {"text": state["text"].upper()}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("greet", greet)
    graph.add_node("shout", shout)
    graph.set_entry_point("greet")
    graph.add_edge("greet", "shout")
    graph.add_edge("shout", END)
    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    result = app.invoke({"text": ""})
    print(result["text"])
