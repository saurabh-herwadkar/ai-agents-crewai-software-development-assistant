# Imports
from crewai import Task
from textwrap import dedent


# Define your tasks here
class CustomTasks:

    # Task definition
    def business_analysis_task(self, agent, requirements):
        return Task(
            description=dedent(
                f"""
            Convert the given requirements into a JIRA ticket
            Information should not contain any aggressive or inflammatory content
            Do not use hyperbole or exaggeration
            Use LLM only
    
            Use this topic: {requirements}
            
        """
            ),
            expected_output="First share the supplied requirements as requirements: In Maximum 1000 words based on the given requirments title description and acceptance criterion",
            agent=agent,
        )

    # Task definition
    def quality_assurance_task(self, agent):
        return Task(
            description=dedent(
                f"""
            Based on the created JIRA ticket in the previous task
            Generate a testing strategy for the ticket
            Use LLM only 
    
           
            
        """
            ),
            expected_output="In Maximum 1000 words the testing strategy based on the JIRA defintion from the previous task",
            agent=agent,
        )

    # Task definition
    def solution_archiecture_task(self, agent, technology_stack):
        return Task(
            description=dedent(
                f"""
            Based on the created JIRA ticket and the testing strategy in the previous task
            Also take the provided technology stack into consideration
            The provided technology stack is {technology_stack}
            Generate a solution architecture image for this ticket
            Use LLM only 
    
           
            
        """
            ),
            expected_output="First share the supplied technology stack as technologystack: then share the solution architecture diagram",
            agent=agent,
        )

    # Task definition
    def sample_code_task(self, agent, technology_stack):
        return Task(
            description=dedent(
                f"""
            Based on the previous JIRA ticket, testing strategy and solution architecture
            Geenrate sample code code should be precise, neatly formatted and mature 
            Also take the provided technology stack into consideration
            The provided technology stack is {technology_stack}
            Use LLM only 
    
           
            
        """
            ),
            expected_output="Sahre the formatted sample code",
            agent=agent,
        )
