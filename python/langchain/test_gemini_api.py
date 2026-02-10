import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

# 1) Set your API key (pick ONE way)
# Recommended by LangChain: GOOGLE_API_KEY env var  [oai_citation:2‡reference.langchain.com](https://reference.langchain.com/python/integrations/langchain_google_genai/ChatGoogleGenerativeAI/?utm_source=chatgpt.com)
# os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_AI_STUDIO_KEY"

# Or, if you prefer Gemini's naming: GEMINI_API_KEY (common in Gemini docs)  [oai_citation:3‡Google AI for Developers](https://ai.google.dev/gemini-api/docs/quickstart?utm_source=chatgpt.com)
# os.environ["GEMINI_API_KEY"] = "YOUR_GOOGLE_AI_STUDIO_KEY"

# 2) Define a couple of tools
@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def square(x: float) -> float:
    """Square a number."""
    return x * x

tools = [add, square]

# 3) Create the LLM (Gemini via Google AI Studio key)
# LangChain's Google integration supports using an API key via env var or api_key param.  [oai_citation:4‡reference.langchain.com](https://reference.langchain.com/python/integrations/langchain_google_genai/ChatGoogleGenerativeAI/?utm_source=chatgpt.com)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"),
)

# 4) Build a tool-calling agent + executor
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use tools when useful."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 5) Run it
result = executor.invoke({"input": "What is the square of (12 + 3)? Use tools."})
print(result["output"])