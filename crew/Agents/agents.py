from crewai_tools import (
  ScrapeWebsiteTool,
  SerperDevTool
)
from crewai import Agent, Task

from groq_client import load_model
llm = load_model(flag=0)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


# Agent 1: Resume Extractor
resume_extractor = Agent(
    role="Resume Data Extractor Expert",
    goal="Make sure you extract all the Main Headings and arrange the details in json format "
         "This will help to provide structured data for further process"
         "resume_content:{resume_content}",
    verbose=True,
    backstory=(
        "As a Resume Data Extractor, your prowess in "
        "extracting critical "
        "information from the resume provided."
        "Your skills help you to extract details in json , where data is extracted in form key value pairs"
    ),
    llm=llm,
    max_iter=5,
    allow_delegation=False
)



# Agent 2: Researcher
job_researcher = Agent(
    role="Tech Job Researcher",
    goal="Extract essential information from job postings to assist job applicants"
        "Analyze the job posting at {job_posting_url} and answer the following: "
        "What are the essential skills and qualifications required for this job?"
        "Extract the job description and responsibilities from the provided URL."
        "What are the top keywords mentioned in the job posting?"
        "Can you summarize the key requirements and preferences for this position?"
        "What are the company's expectations for the ideal candidate?",
    verbose=True,
    backstory=(
        "As a seasoned Job Researcher, I excel in analyzing job postings "
        "to identify critical requirements and skills sought by employers."
        "My expertise enables me to pinpoint necessary qualifications, "
        "enabling effective tailoring of job applications."
        "** extract all the keywords, descriptions, and requirements of the job **"
    ),
    max_iter=5,
    llm=llm,
    tools = [scrape_tool],
    allow_delegation=False
)


# Agent 3: Resume  Talior
Resume_Tailor = Agent(
    role="Expert Resume Tailor",
    goal="You have been provided resume in json format, and a detailed description of a job opening from earlier tasks. Your task is to modify the existing resume json based on job description"
        " You must ensure all the relevant keywords, desciprtion, details are added such that new resume json has high ATS score."
        "You can use your tools to research best keywords for the reevant job description",        
    verbose=True,
    backstory=(
        "As a resume tailor, your prowess in "
        "navigating and extracting critical "
        "information from job postings is unmatched."
        "Your skills help to generate resume "
        "which highly match the job description "
    ),
    llm=llm,
    max_iter=5,
)
