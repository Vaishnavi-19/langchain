# LangChain

LangChain is an open-source framework designed to simplify the development of applications powered by large language models (LLMs). It provides a suite of tools and abstractions to build, deploy, and manage LLM-based applications efficiently.

## Key Features

- **Prompt Management**: Create, version, and manage prompts for LLMs.
- **Chains**: Combine multiple LLM calls and other utilities into sequences.
- **Agents**: Enable LLMs to interact with external tools and APIs.
- **Memory**: Persist state across conversations and interactions.
- **Integrations**: Support for various LLMs, vector stores, and data sources.

## Installation

To install LangChain, use pip:

```bash
pip install langchain
```

For additional dependencies based on your use case (e.g., OpenAI, Hugging Face), install extras:

```bash
pip install langchain[openai]
```

## Using Ollama (Local LLM)

Ollama is a local LLM runtime that lets you run models on your own machine without requiring an API key.

### 1) Install Ollama

- **Windows/macOS/Linux (recommended):** Download the installer from https://ollama.com and follow the instructions.
- **Linux (alternative):** Use the provided package manager commands from the Ollama docs.

After installation, verify it works:

```bash
ollama --help
```

### 2) Pull a model

```bash
ollama pull llama2
```

### 3) Install the LangChain Ollama integration

```bash
pip install langchain-ollama
```

### 4) Use Ollama in LangChain

```python
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="llama2")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short summary about {topic}."
)

chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(topic="artificial intelligence")
print(result)
```

> **Tip:** If you encounter issues, ensure the Ollama daemon is running (e.g., `ollama server` or `ollama run`), and that the model is downloaded.

## Quick Start

Here's a simple example of using LangChain to create a basic chain:

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the LLM
llm = OpenAI(temperature=0.7)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short summary about {topic}."
)

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run(topic="artificial intelligence")
print(result)
```

## Documentation

For more detailed information, visit the [official LangChain documentation](https://python.langchain.com/).

## Contributing

Contributions are welcome! Please see the [contributing guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.