import markdown as md
import os

def generate_readme(text: str):
    """
    Generate a README.md file from provided text.
    """
    # Convert text to Markdown format
    markdown_content = md.markdown(text)

    # Write directly to README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(markdown_content)

    return "README.md file generated successfully!"