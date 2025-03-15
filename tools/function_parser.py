import ast
from src.code_ingestion import get_code
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

def extract_functions(code_files: dict):
    """
    Parses Python code and extracts function/class signatures.
    """
    functions = {file: [] for file in code_files.keys() if file.endswith(".py")}

    for file, code in code_files.items():
        if file.endswith('.py'):
            parsed_code = ast.parse(code[0])
            functions[file] = [node.name for node in parsed_code.body if isinstance(node, ast.FunctionDef)]

    test_cases = {}
    batched_prompt = ""

    for file, func_list in functions.items():
        if func_list:
            batched_prompt += f"File: {file}\nFunctions: {', '.join(func_list)}\n\n"

    if batched_prompt:
        prompt = f"Write PyTest unit tests for the following functions. Include only the code:\n\n{batched_prompt}"
        response = llm.invoke(prompt).content

        # Distribute test cases back into their respective files
        for file in functions.keys():
            test_cases[file] = response.split("\n\n")  # Splitting tests by double newlines (adjust if needed)

    return test_cases

code = get_code("https://github.com/EdgarSilva-tech/Dog_LLM.git")

functions = extract_functions(code)

print(functions)