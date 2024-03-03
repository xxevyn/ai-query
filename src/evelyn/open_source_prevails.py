# Import necessary modules
import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "REPLACE_ME"

# Initialize search tool
search_tool = DuckDuckGoSearchRun()

# Create a senior research analyst agent
researcher1 = Agent(
    role='Senior Research Analyst at a leading venture capital firm that only invests in open source firms',
    goal='Find market niches where open source surpasses closed source',
    backstory="""You are a senior research analyst at a leading venture capital firm.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

# Define the tasks to find market niches where open-source software prevails over closed source
task1 = Task(
    description="""Find a market niche where open-source software prevails over closed source""",
    expected_output="Describe the market, reasons why open source prevails, and examples of open source companies dominating the niche",
    agent=researcher1
)

task2 = Task(
    description="""Find another market niche where open-source software prevails over closed source""",
    expected_output="Describe the market, reasons why open source prevails, and examples of open source companies dominating the niche",
    agent=researcher1
)

# Function to search for market niches where open-source software prevails over closed source
def open_source_prevails():
    # Create a crew consisting of the researcher agent and the tasks
    crew = Crew(
        agents=[researcher1],
        tasks=[task1, task2],
        verbose=2,  # You can set it to 1 or 2 for different logging levels
    )

    # Get the crew to work
    result = crew.kickoff()

    print("######################")
    print(result)

# Call the function to start the search process
open_source_prevails()
