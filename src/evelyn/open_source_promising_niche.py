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
    role='Senior Research Analyst at a leading venture capital firm',
    goal='Identify the more promising market niche to invest in between LMS and Microservice Orchestration and explain why it makes sense to invest there',
    backstory="""You are a senior research analyst at a leading venture capital firm. Your objective is to identify the most promising market niche for investment.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

# Define the task to find the most promising market niche to invest in
task1 = Task(
    description="""Find the most promising market niche to invest in and explain why it makes sense to invest there""",
    expected_output="Describe the market niche, reasons for its potential, and examples of successful companies in that niche",
    agent=researcher1
)

# Function to find the most promising market niche to invest in
def find_promising_market_niche():
    # Create a crew consisting of the researcher agent and the task
    crew = Crew(
        agents=[researcher1],
        tasks=[task1],
        verbose=2,  # You can set it to 1 or 2 for different logging levels
    )

    # Get the crew to work
    result = crew.kickoff()

    print("######################")
    print(result)

# Call the function to start the search process
find_promising_market_niche()
