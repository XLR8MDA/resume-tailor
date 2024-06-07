from crew.Agents.agents import job_researcher,resume_extractor,Resume_Tailor
from crew.Tasks.tasks import research_task,Resume_extracter_Task,Resume_Tailor_task
from crewai import Crew


# Define the crew with agents and tasks
extractor_crew = Crew(
    agents=[job_researcher,resume_extractor,Resume_Tailor],
    tasks=[research_task,Resume_extracter_Task,Resume_Tailor_task],
    verbose=True,
)