from src.agent import graph
from src.code_ingestion import get_code
import argparse

def main(source, question):
    """Main function to process code and interact with the LangGraph agent."""
    code_content = get_code(source)

    if not code_content:
        print("Error fetching code!")
        return

    events = graph.stream(
        {"messages": [question], "code_content": code_content},
        stream_mode="values"
    )

    for event in events:
        if "messages" in event:
            print(event["messages"][-1])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze code using LangGraph")
    parser.add_argument("--source", required=True, help="GitHub URL or local file path")
    parser.add_argument("--question", required=True, help="Question to ask the agent")
    args = parser.parse_args()

    main(args.source, args.question)
