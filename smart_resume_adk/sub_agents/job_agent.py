from google.adk import Agent
from google.adk.tools import google_search


job_agent = Agent(
    name="job_agent",
    model="gemini-1.5-flash",
    description="Extract job skills",
    instruction="""
    You are responsible for extracting skills.
    Return technical skills only.
    """,
    tools=[google_search],
)