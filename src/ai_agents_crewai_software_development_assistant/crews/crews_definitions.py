# Imports
from crewai import Crew
from ai_agents_crewai_software_development_assistant.agents.agents_definitions import (
    CustomAgents,
)
from ai_agents_crewai_software_development_assistant.tasks.tasks_definitions import (
    CustomTasks,
)

## Initalize
custom_agents = CustomAgents()
custom_tasks = CustomTasks()
business_analysis_agent = custom_agents.business_analysis_agent()
quality_assurance_agent = custom_agents.quality_assurance_agent()
solution_architecture_agent = custom_agents.solution_architecture_agent()
sample_code_agent = custom_agents.sample_code_agent()


# Define your crews
class CustomCrews:

    # Crew definitions
    def software_development_crew(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        # Define your custom crew here

        # Variables specific to this crew here here
        requirements = """

        We need a drop down for products. All products should be listed in the drop down

         """

        technology_stack = """

       node js 20 Serverless AWS DynamoDB

         """

        # Capture inputs here if required

        # Return an instance of crew
        return Crew(
            agents=[
                business_analysis_agent,
                quality_assurance_agent,
                solution_architecture_agent,
                sample_code_agent,
            ],
            tasks=[
                custom_tasks.business_analysis_task(
                    business_analysis_agent, requirements
                ),
                custom_tasks.quality_assurance_task(quality_assurance_agent),
                custom_tasks.solution_archiecture_task(
                    quality_assurance_agent, technology_stack
                ),
                custom_tasks.sample_code_task(sample_code_agent, technology_stack),
            ],
            verbose=True,
        )
