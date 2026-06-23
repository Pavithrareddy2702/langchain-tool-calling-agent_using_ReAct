import os
import requests
import certifi

from dotenv import load_dotenv

from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq

from langchain import hub
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor

# --------------------------------------------------
# Setup
# --------------------------------------------------

os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

# --------------------------------------------------
# Tools
# --------------------------------------------------

search_tool = TavilySearchResults(max_results=2)


@tool
def get_weather_data(city: str) -> str:
    """
    Get current weather for a city.
    """

    url = (
        f"https://api.weatherstack.com/current?"
        f"access_key={WEATHERSTACK_API_KEY}&query={city}"
    )

    response = requests.get(url)
    data = response.json()

    if "current" not in data:
        return f"Could not fetch weather data for {city}"

    return (
        f"City: {city}\n"
        f"Temperature: {data['current']['temperature']}°C\n"
        f"Weather: {data['current']['weather_descriptions'][0]}\n"
        f"Humidity: {data['current']['humidity']}%"
    )


TOOLS = [search_tool, get_weather_data]


# --------------------------------------------------
# Build Agent
# --------------------------------------------------

def build_agent(model_name):

    llm = ChatGroq(
        model_name=model_name,
        temperature=0,
        groq_api_key=GROQ_API_KEY,
    )

    prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=TOOLS,
        prompt=prompt,
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=TOOLS,
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True,
        return_intermediate_steps=True,
    )

    return agent_executor