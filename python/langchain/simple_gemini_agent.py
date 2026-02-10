"""
Simplified LangChain Agent using Free Gemini API
(Without hub dependency)

Prerequisites:
1. Install: pip install langchain langchain-google-genai google-generativeai
2. Get free API key: https://makersuite.google.com/app/apikey
3. Set environment variable: export GOOGLE_API_KEY='your-api-key-here'
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool, AgentType

# Simple tools
def calculator(expression: str) -> str:
    """Calculates mathematical expressions."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

def get_weather(location: str) -> str:
    """Mock weather tool (replace with real API)."""
    return f"The weather in {location} is sunny and 72°F"

# Create tools
tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Calculate math expressions like '5+3' or '10*2'"
    ),
    Tool(
        name="Weather",
        func=get_weather,
        description="Get weather for a location. Input: city name"
    )
]

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5,
    google_api_key=os.environ.get("GEMINI_API_KEY")
)

# Create agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# Run
if __name__ == "__main__":
    print("🤖 Gemini Agent Ready!\n")
    
    # Test
    result = agent.run("What is 15 times 8?")
    print(f"\nResult: {result}")
