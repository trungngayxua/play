"""
Simple LangChain Agent using Free Gemini API

Prerequisites:
1. Install required packages:
   pip install langchain langchain-google-genai google-generativeai

2. Get a free API key from:
   https://makersuite.google.com/app/apikey
   
3. Set your API key as an environment variable:
   export GOOGLE_API_KEY='your-api-key-here'
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain import hub

# Define some simple tools for the agent
def calculator(expression: str) -> str:
    """Calculates a mathematical expression."""
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"

def string_reverser(text: str) -> str:
    """Reverses a string."""
    return text[::-1]

def word_counter(text: str) -> str:
    """Counts words in a text."""
    words = text.split()
    return f"Word count: {len(words)}"

# Create tools list
tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for performing mathematical calculations. Input should be a valid mathematical expression like '5 + 3' or '10 * 2'"
    ),
    Tool(
        name="StringReverser",
        func=string_reverser,
        description="Reverses any string. Input should be the text you want to reverse."
    ),
    Tool(
        name="WordCounter",
        func=word_counter,
        description="Counts the number of words in a text. Input should be the text you want to count words in."
    )
]

# Initialize Gemini model (using free tier)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Free model
    temperature=0.7,
    google_api_key=os.environ.get("GOOGLE_API_KEY")
)

# Get the ReAct prompt template from LangChain hub
prompt = hub.pull("hwchase17/react")

# Create the agent
agent = create_react_agent(llm, tools, prompt)

# Create the agent executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5
)

# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("LangChain Agent with Gemini API")
    print("=" * 50)
    
    # Test queries
    queries = [
        "What is 25 multiplied by 4?",
        "Reverse the string 'Hello World'",
        "How many words are in 'The quick brown fox jumps over the lazy dog'?"
    ]
    
    for query in queries:
        print(f"\n🔹 Query: {query}")
        print("-" * 50)
        try:
            response = agent_executor.invoke({"input": query})
            print(f"\n✅ Answer: {response['output']}\n")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")
