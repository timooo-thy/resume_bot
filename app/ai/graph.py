from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain.schema import BaseMessage
from langgraph.graph import StateGraph, START
from langgraph.graph.state import CompiledStateGraph


class AgentState(TypedDict):
    """
    Represents the state of the agent in the graph.
    """
    messages: Annotated[list[BaseMessage], add_messages]
    retries: int
    max_retries: int
    model: ChatOpenAI


class AgentGraph:
    def compile(self) -> CompiledStateGraph[AgentState, AgentState, AgentState]:
        """
        Compile the agent graph.

        Returns:
            CompiledStateGraph: The compiled state graph for the agent.
        """
        return StateGraph(AgentState).add_node(
            self.agent_node).add_edge(
            START, "agent_node").compile()

    def agent_node(self, state: AgentState) -> dict:
        """
        The agent node function that processes the last message and generates a response.

        Args:
            state (AgentState): The current state of the agent.

        Returns:
            Dict: A dictionary containing the next state of the agent.
        """

        if state["retries"] >= state["max_retries"]:
            return {}
        last_message = state["messages"][-1]

        model = state["model"]
        response = model.invoke(input=last_message.content)

        return {
            "messages": [response],
            "retries": state["retries"] + 1,
        }
