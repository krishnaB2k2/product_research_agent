import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerpApiGoogleShoppingTool
)





@CrewBase
class ProductRecommendationEngineCrew:
    """ProductRecommendationEngine crew"""

    
    @agent
    def requirements_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["requirements_analyst"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def product_research_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["product_research_specialist"],
            
            
            tools=[				SerpApiGoogleShoppingTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def product_ranking_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["product_ranking_analyst"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def recommendation_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["recommendation_specialist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    

    
    @task
    def analyze_user_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_user_requirements"],
            markdown=False,
            
            
        )
    
    @task
    def research_product_options(self) -> Task:
        return Task(
            config=self.tasks_config["research_product_options"],
            markdown=False,
            
            
        )
    
    @task
    def rank_product_options(self) -> Task:
        return Task(
            config=self.tasks_config["rank_product_options"],
            markdown=False,
            
            
        )
    
    @task
    def generate_personalized_recommendations(self) -> Task:
        return Task(
            config=self.tasks_config["generate_personalized_recommendations"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ProductRecommendationEngine crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


