from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-1.5-flash",
    name="resume_orchestrator",
    description="Smart Resume Agent"
)