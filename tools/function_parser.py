import ast
from src.code_ingestion import get_code
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

class Tests:
    tests: str # Ensure both keys and values are strings

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620").with_structured_output(Tests)

def extract_functions(code_files: dict):
    """
    Parses Python code and extracts function/class signatures for which unit test are written.
    """
    functions = {file: [] for file in code_files.keys() if file.endswith(".py")}

    for file, code in code_files.items():
        if file.endswith('.py') and len(file) > 0:
            parsed_code = ast.parse(code[0])
            functions[file] = [node.name for node in parsed_code.body if isinstance(node, ast.FunctionDef)]

    test_cases = {}
    batched_prompt = ""

    for file, func_list in functions.items():
        if func_list:
            batched_prompt += f"File: {file}\nFunctions: {', '.join(func_list)}\n\n"

    if batched_prompt:
        for file, func_list in functions.items():
            prompt = f"Write PyTest unit tests for the following functions. Include only the Python code without any other comments:\n\n{batched_prompt}"
            test_cases[file] = llm.invoke(prompt)

        # Distribute test cases back into their respective files
        # for file in functions.keys():
        #     test_cases[file] = response  # Splitting tests by double newlines (adjust if needed)
            # with open('test_'+ file, "w") as f:
            #     f.write(test_cases[file][1])

    return test_cases


# os.makedirs('./tests', exist_ok=True)
# for file, cases in functions.items():
#     with open('./tests' + file, 'w') as f:
#         f.write(cases)