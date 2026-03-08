# Ollama + LangChain Example

This repository demonstrates how to use **Ollama** (a local LLM runtime) together with the **LangChain** ecosystem.

## Using Ollama (Local LLM)

Ollama lets you run models locally without requiring a remote API key.

### 1) Install Ollama

- **Windows/macOS/Linux (recommended):** Download the installer from https://ollama.com and follow the instructions.
- **Linux (alternative):** Use the package manager commands from the Ollama docs.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.