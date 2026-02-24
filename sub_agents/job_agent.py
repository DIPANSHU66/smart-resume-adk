from google.adk import Agent
from google.adk.tools import google_search

job_agent = Agent(
    name="job_agent",
    model="gemini-1.5-pro",
    description="Analyzes job description and fetches required skills using Google Search.",
    instructions="""
    You are responsible for extracting important skills from the given job description.
    
    If needed, use google_search to find:
    - Common skills required for this role
    - ATS keywords related to this role

    Return a clean list of required technical skills only.
    """,
    tools=[google_search],
)