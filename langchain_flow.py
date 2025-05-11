import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

assert AZURE_OPENAI_ENDPOINT, "AZURE_OPENAI_ENDPOINT is not set."
assert AZURE_OPENAI_KEY, "AZURE_OPENAI_KEY is not set."
assert AZURE_OPENAI_MODEL, "AZURE_OPENAI_MODEL is not set."
assert AZURE_OPENAI_API_VERSION, "AZURE_OPENAI_API_VERSION is not set."

client = ChatCompletionsClient(
    endpoint=AZURE_OPENAI_ENDPOINT,
    credential=AzureKeyCredential(AZURE_OPENAI_KEY),
    api_version=AZURE_OPENAI_API_VERSION
)

def research_tool(query: str) -> str:
    messages = [
        SystemMessage(content="You are a researcher. Research the following topic in detail and provide a comprehensive summary."),
        UserMessage(content=query)
    ]
    response = client.complete(
        messages=messages,
        max_tokens=2048,
        model=AZURE_OPENAI_MODEL
    )
    return response.choices[0].message.content

def writer_tool(research: str) -> str:
    messages = [
        SystemMessage(content="You are a professional writer. Using the following research, write a clear, engaging article."),
        UserMessage(content=research)
    ]
    response = client.complete(
        messages=messages,
        max_tokens=2048,
        model=AZURE_OPENAI_MODEL
    )
    return response.choices[0].message.content

def run_flow(topic: str):
    research = research_tool(topic)
    print("=== Researcher Output ===")
    print(research)
    article = writer_tool(research)
    print("\n=== Writer Output ===")
    print(article)

if __name__ == "__main__":
    user_topic = input("Enter a topic for the researcher and writer agents: ")
    run_flow(user_topic)