import ast
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

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
            prompt = (
                f"Write only valid unit test code for the following functions from the file {file}.\n"
                "Do not include any markdown formatting, explanations, or comments. Only return pure Python code:\n\n"
                f"{batched_prompt}"
            )
            test_cases[file] = llm.invoke(prompt).content

            if not os.path.exists('./tests'):
                os.makedirs('./tests')

            with open(f'./tests/test_{file}', 'w') as f:
                f.write(test_cases[file])

    return test_cases