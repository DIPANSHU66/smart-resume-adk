from google.adk import Agent
from sub_agents.resume_agent import resume_agent
from sub_agents.job_agent import job_agent
from sub_agents.ats_agent import ats_agent
from sub_agents.report_agent import report_agent

root_agent = Agent(
    name="resume_orchestrator",
    model="gemini-1.5-pro",
    description="Main orchestrator for Smart Resume Analyzer",
    instructions="""
    Workflow:
    1. Extract resume text using resume_agent.
    2. Extract required skills from job description using job_agent.
    3. Compare resume and job skills using ats_agent.
    4. Generate ATS improvement report using report_agent.

    Provide final ATS analysis summary.
    """,
    sub_agents=[
        resume_agent,
        job_agent,
        ats_agent,
        report_agent,
    ],
)