<h1>Code Analysis and Documentation Generator</h1>
<p>This project is a Python-based tool that analyzes code, generates documentation, and provides interactive assistance for programming-related inquiries. It uses language models and graph-based processing to offer various functionalities.</p>
<h2>Key Components</h2>
<ol>
<li><strong>Agent (agent.py)</strong></li>
<li>Implements a state graph for processing user inquiries.</li>
<li>Uses the Anthropic ChatAnthropic model for natural language understanding.</li>
<li>Includes a router to classify user inquiries into different categories.</li>
<li>
<p>Integrates with various tools for code analysis and documentation generation.</p>
</li>
<li>
<p><strong>Code Ingestion (code_ingestion.py)</strong></p>
</li>
<li>Fetches code from a GitHub URL or local file path.</li>
<li>
<p>Supports various file extensions including Python, Dockerfile, Jupyter notebooks, and YAML.</p>
</li>
<li>
<p><strong>Main Script (main.py)</strong></p>
</li>
<li>Provides a command-line interface to interact with the tool.</li>
<li>
<p>Processes user questions and code sources.</p>
</li>
<li>
<p><strong>Function Parser (function_parser.py)</strong></p>
</li>
<li>Extracts function and class signatures from Python code.</li>
<li>
<p>Generates PyTest unit tests for the extracted functions.</p>
</li>
<li>
<p><strong>README Generator (readme_generator.py)</strong></p>
</li>
<li>Creates a README.md file from provided text.</li>
</ol>
<h2>Features</h2>
<ul>
<li>Code analysis and understanding</li>
<li>Automatic unit test generation</li>
<li>README file creation</li>
<li>Interactive Q&amp;A about code</li>
<li>Support for multiple programming file types</li>
</ul>
<h2>Usage</h2>
<p>To use this tool, run the main script with the following arguments:</p>
<p><code>python main.py --source &lt;github_url_or_local_path&gt; --question "&lt;your_question&gt;"</code></p>
<p>Replace <code>&lt;github_url_or_local_path&gt;</code> with the source of your code and <code>&lt;your_question&gt;</code> with any programming-related inquiry.</p>
<h2>Dependencies</h2>
<ul>
<li>langchain_anthropic</li>
<li>langgraph</li>
<li>pydantic</li>
<li>python-dotenv</li>
<li>IPython</li>
<li>markdown</li>
</ul>
<p>Make sure to set up your environment variables, especially for the Anthropic API key.</p>
<h2>Note</h2>
<p>This tool is designed to assist with various programming tasks, including code analysis, documentation generation, and answering programming-related questions. It leverages advanced language models and graph-based processing to provide comprehensive assistance.</p>