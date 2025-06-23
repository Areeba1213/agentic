# 🧠 Swarm Learning - UV, OpenRouter, and LiteLLM Agent Examples

This repository provides simple, beginner-friendly examples for the following tools:

- `01_uv`: A fast Python package manager.
- `02_openrouter`: Unified API access to various LLMs (like OpenAI, Anthropic, Mistral).
- `03_litellm_openai_agent`: Wrapper to run OpenAI-style agents using multiple providers.
- 
## 📁 Project Structure

00_swarm/
├── 01_uv/
│ └── uv_example.py
├── 02_openrouter/
│ └── openrouter_example.py
├── 03_litellm_openai_agent/
│ ├── agent_example.py
│ └── litellm_config.yaml
└── README.md
## 🔧 Setup Instructions
cd swarm_learning
🚀 Topic: 01_uv - Fast Python Package Manager
📌 What is uv?
uv is a superfast Python package manager made in Rust. It can create virtual environments, install packages, and manage dependencies much faster than pip.

🔍 How to Install & Run
# Install uv
# Create virtual environment
uv venv
source .venv/bin/activate

# Install a package (e.g., requests)
uv pip install requests

# Run the example
cd 01_uv
python uv_example.py
🤖 Topic: 02_openrouter - Unified LLM Access
📌 What is OpenRouter?
OpenRouter lets you access models like GPT-4, Claude, Mistral, etc. through one single API using your API key.

🔍 How to Use
Get your API key from https://openrouter.ai

Install OpenAI package:
pip install openai
Replace "your-openrouter-key" in openrouter_example.py with your actual key.

Run the script:
cd 02_openrouter
python openrouter_example.py
🧠 Topic: 03_litellm_openai_agent - Use Agents Easily
📌 What is LiteLLM?
LiteLLM lets you send OpenAI-style requests to any compatible provider like OpenRouter, Groq, Fireworks, etc. You can even use it to run agents with different backends.

🔍 Setup & Run
Install LiteLLM:
pip install litellm
Add your OpenAI key to litellm_config.yaml:
model_list:
  - model_name: openai/gpt-3.5-turbo
    litellm_provider: openai
    api_key: your-openai-api-key
Run the agent script:
cd 03_litellm_openai_agent
python agent_example.py
