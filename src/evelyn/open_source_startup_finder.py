# Import necessary modules
import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "REPLACE_ME"

# Initialize search tool
search_tool = DuckDuckGoSearchRun()

# Define venture capital analyst agents
analyst1 = Agent(
    role='Venture Capital Analyst',
    goal='Find a list of earning management system (LMS) startup who is open-source',
    backstory="""You are a venture capital analyst tasked with identifying the most promising Learning Management System (LMS) startup for investment.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

# Define tasks for each aspect of the requirements
task1 = Task(
    description="""Find learning management system (LMS) startups founded in the last 5 years""",
    expected_output="Provide a list of promising LMS startups founded after 2019",
    agent=analyst1
)


task2 = Task(
    description="""Find learning management system (LMS) who is similar to Sana Lab""",
    expected_output="Provide a list of promising LMS startups that do similar tasks as Sana Lab",
    agent=analyst1
)

task3 = Task(
    description="""Focus on LMS startups raising seed/series A funding using crunchbase data""",
    expected_output="Filter out LMS startups currently raising series B and later funding using crunchbase data",
    agent=analyst1
)

# Function to coordinate tasks and get the crew to work
def open_source_startup_finder():
    # Create a crew consisting of the analyst agent and the tasks
    crew = Crew(
        agents=[analyst1],
        tasks=[task1, task3],
        verbose=2,  # You can set it to 1 or 2 for different logging levels
    )

    # Get the crew to work
    result = crew.kickoff()

    print("######################")
    print(result)

# Call the function to start the analysis process
open_source_startup_finder()
