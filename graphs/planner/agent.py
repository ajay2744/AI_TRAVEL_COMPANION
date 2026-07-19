from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from .prompts import SYSTEM_PROMPT
from .tools import tools
from graphs.models import PlannerOutput

load_dotenv()

llm = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    temperature=0.3,
)
planner_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
    response_format=PlannerOutput,
)

# planner_agent = create_agent(
#     model=llm,
#     tools=tools,
#     system_prompt=SYSTEM_PROMPT,
# )