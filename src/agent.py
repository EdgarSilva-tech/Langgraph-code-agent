from langchain_anthropic import ChatAnthropic
from typing import Annotated, Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from IPython.display import Image, display
from dotenv import load_dotenv
from src.code_ingestion import get_code
from tools.function_parser import extract_functions
from tools.readme_generator import generate_readme
from langgraph.prebuilt import ToolNode, tools_condition
from pydantic import BaseModel

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
tools = [generate_readme, extract_functions]
llm_with_tools = llm.bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]
    code_content: str

def model(state: State):
    """Model function to interact with the LangChain agent."""
    prompt = f"Given the following context: {state['messages']} and code: {state['code_content']} answer any question about it and execute any tasks asked for example: create a function, write a Readme, etc."
    response = llm_with_tools.invoke(prompt)
    return {"messages": state["messages"] + [response]}

graph_state = StateGraph(State)

graph_state.add_node('ingest_code', get_code)
graph_state.add_node('llm', model)
graph_state.add_node('extract_functions', extract_functions)
graph_state.add_node('generate_readme', generate_readme)
tool_node = ToolNode(tools=tools)
graph_state.add_node("tools", tool_node)

graph_state.add_edge(START, 'ingest_code')
graph_state.add_edge('ingest_code', 'llm')
graph_state.add_conditional_edges('llm', tools_condition)
graph_state.add_edge("tools", "llm")
graph_state.add_edge('llm', END)

graph = graph_state.compile()

from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass