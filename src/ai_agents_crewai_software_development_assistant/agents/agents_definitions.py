# Imports
from crewai import Agent
from textwrap import dedent
from ai_agents_crewai_software_development_assistant.llm.llm_definitions import (
    LLMDefinitions,
)


# Initialise
llm_definitions = LLMDefinitions()


# Define custom agents
class CustomAgents:

    # Agent defintion
    def business_analysis_agent(self):
        return Agent(
            role="you are a senior business analyst with 10 + years of expereince",
            backstory=dedent(
                f"""You have good expereince in writing functional requirements in a JIRA ticket Based on the requirements provided 
                    in the JIRA ticket give a 

                    Title
                    Description

                    In the description use this pattern
                    As a ...
                    I need to ...
                    So that...

                    For example
                    As a Business user
                    I need to have a home page
                    So that I can see all the features of the homepage of the website
                  
                    We also need acceptance criterion as numbered bullet points 
                    
                    """
            ),
            goal=dedent(
                f"""A final JIRA ticket with a title description and acceptance criterion"""
            ),
            # tools=[serper_dev_tool, website_search_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.OpenAIGPT4,
        )

    # Agent defintion
    def quality_assurance_agent(self):
        return Agent(
            role="you are a quality assurance expert with 10 + years of expereince",
            backstory=dedent(
                f"""You have good expereince in writing Quality assurance requirements 
                    Based on the JIRA ticket description from the previous task

                    Functional test cases
                    Non functional test cases
                    API test cases
                    Performance test cases

                    Consider both happy path and negative path test cases
                    List the test cases as numbered bullet points
                    
                    """
            ),
            goal=dedent(
                f"""    Deliver the testing strategy for this ticket based on the above points    """
            ),
            # tools=[serper_dev_tool, website_search_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.OpenAIGPT4,
        )

    # Agent defintion
    def solution_architecture_agent(self):
        return Agent(
            role="you are a senior solutions architect with 20 + years of experience",
            backstory=dedent(
                f"""You have good expereince in developing solution architecture in a Cloud native serverless 
                    event driven way using modern techologies. 
                    
                    """
            ),
            goal=dedent(f"""    Deliver an image of the solution architecture    """),
            # tools=[serper_dev_tool, website_search_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.OpenAIGPT4,
        )

    # Agent defintion
    def sample_code_agent(self):
        return Agent(
            role="you are an expereinced tech lead with 10 + years of expereince",
            backstory=dedent(
                f"""You have good experience in coding using most open source technology stacks
                    Your code is precise and neatly formatted
                    We just need example code for getting started
                    """
            ),
            goal=dedent(f"""    The sample code    """),
            # tools=[serper_dev_tool, website_search_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.OpenAIGPT4,
        )
