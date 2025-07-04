from typing import TypedDict, Annotated, Dict
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain.schema import BaseMessage
from langgraph.graph import StateGraph, START
from langgraph.graph.state import CompiledStateGraph


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    retries: int
    max_retries: int
    model: ChatOpenAI


class AgentGraph:
    def compile(self) -> CompiledStateGraph[AgentState, AgentState, AgentState]:
        """
        Compile the agent graph.
        """
        return StateGraph(AgentState).add_node(
            self.agent_node).add_edge(
            START, "agent_node").compile()

    def agent_node(self, state: AgentState) -> Dict:

        if state["retries"] >= state["max_retries"]:
            return {}
        last_message = state["messages"][-1]

        model = state["model"]
        response = model.invoke(input=last_message.content)

        return {
            "messages": [response],
            "retries": state["retries"] + 1,
        }
