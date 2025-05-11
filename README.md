# Semantic Kernel Python LangChain Agent Flow

This project demonstrates a two-step agent flow using Azure OpenAI's ChatCompletions API. It features a researcher agent that gathers information on a given topic and a writer agent that synthesizes the research into an article.

## Tools and Frameworks Used
- **Azure OpenAI Service**: Provides access to powerful language models via Azure's cloud platform.
- **azure-ai-inference**: Python SDK for interacting with Azure AI models, specifically used for chat completions in this project.
- **dotenv**: Loads environment variables from a `.env` file for secure and convenient configuration management.
- **Python Standard Library**: Used for environment variable access and basic scripting.

## Requirements
- Python 3.8+
- Azure OpenAI resource and deployment

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with the following variables:
   ```env
   AZURE_OPENAI_ENDPOINT=<your-azure-openai-endpoint>
   AZURE_OPENAI_KEY=<your-azure-openai-key>
   AZURE_OPENAI_MODEL=<your-deployment-name>
   AZURE_OPENAI_API_VERSION=<api-version>
   ```
   - `AZURE_OPENAI_ENDPOINT`: e.g. `https://<resource-name>.openai.azure.com/`
   - `AZURE_OPENAI_KEY`: your Azure OpenAI API key
   - `AZURE_OPENAI_MODEL`: your model deployment name
   - `AZURE_OPENAI_API_VERSION`: e.g. `2024-05-01-preview`

## Usage
Run the main script and enter a topic when prompted:
```bash
python langchain_flow.py
```