from crewai import Task
from crew.Agents.agents import *

Resume_extracter_Task = Task(
    description=(
        "Go through the resume context provided below several times"
        "use your extraction skills to succesfully extract all informations in key value pairs."
        "**extract each and every thing from the resume, do not summarise, add or remove any details. if required then use nested dictionary to save the data** \n"
        "Resume Context:{resume_content}"
    ),
    expected_output=(
        "save the structured json , dont summarise, keep all the details"
    ),
    agent = resume_extractor,
    output_file="resume_json.md",
    async_execution=True
)


research_task = Task(
    description=(
        "Use the tools to gather content and identify and categorize the job requirements. "
        "Extract all the keywords , metadata extractable from the job details," 
        "Always be highly accurate"
       
    ),
    expected_output=(
        "save the output in jd_json.md file"
    ),
    agent=job_researcher,
    output_file="jd_json.md" , 
    async_execution=True
)


Resume_Tailor_task = Task(
    description=(
        "analyse the resume json, job_description_json provided"
        "generate a new tailored resume for the job description."
        "Ensure all the keywords as per job description are mentioned in the resume naturally."
        "Do not modify personal details, education details and achievements."
        "Feel free to change summary,projects,skills and whatever neccessary to increase ATS score only"
        "try to include as my words as possible."
        "whereever you encounter large text, use bullet points,make a complete mardown format output"
    ),
    expected_output=(
        "a newly tailored resume in markdown format such that it matches the job description with highest possible ATS score."
        "**Always return the Markdown only, dont add any of your comments or responses such as 'Here is the tailored resume in markdown format:'"
    ),
    context = [research_task,Resume_extracter_Task],
    agent=Resume_Tailor,
    output_file="modified_resume.md",
  
)