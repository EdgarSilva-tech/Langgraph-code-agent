from langchain_anthropic import ChatAnthropic
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from IPython.display import Image, display
from dotenv import load_dotenv
from code_ingestion import get_code

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

class State(TypedDict):
    messages: Annotated[list, add_messages]
    code_link: str

def model(state: State):
    code = get_code(state["code_link"])
    prompt = f"Given the following context: {state['messages']} and code: {code} answer any question about it and execute any tasks asked for example: create a function, write a Readme, etc."
    response = llm.invoke(prompt)
    return {"messages": state["messages"] + [response]}

graph_state = StateGraph(State)

graph_state.add_node('llm', model)
graph_state.add_edge(START, 'llm')
graph_state.add_edge('llm', END)

graph = graph_state.compile()

events = graph.stream(
    {"messages": "Write a readme for this code", "code_link": "https://github.com/EdgarSilva-tech/Youtube_Sentiment.git"},
    stream_mode="values"
)
for event in events:
    if "messages" in event:
        print(event["messages"][-1])