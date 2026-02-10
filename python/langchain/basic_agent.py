from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="gemini-3.0-flash-preview",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
# from langchain.agents import create_agent
# from langchain_google_genai import ChatGoogleGenerativeAI
#
# def get_weather(city: str) -> str:
#     """ Return weather for a particular city"""
#     return f"It's always a sunny in {city}!"
#
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash"
# )
#
# agent = create_agent(
#     model=llm,
#     tools=[get_weather],
#     system_prompt="You are hitler",
# )
#
#  # Run the agent
# agent.invoke(
#   {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
# )
#
#
