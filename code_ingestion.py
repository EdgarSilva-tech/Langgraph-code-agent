import os

def get_code(link: str) -> None:
    while True:
        os.system("mkdir project_code")
        os.chdir("project_code")
        os.system(f"git clone {link}")
        os.chdir("..")
        break

    code_files = {}
    files_extensions = ["py", "Dockerfile", "ipynb", "yaml", "yml"]
    for root, dirs, files in os.walk("project_code"):
        for file in files:
            if file.split(".")[-1] in files_extensions:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as file_content:
                    code_files[file] = [file_content.read()]

    return code_files


# files = get_code("https://github.com/EdgarSilva-tech/Dog_LLM.git")
# print(files)