from crewai import Agent, Task, Crew
from langchain_ollama import ChatOllama
import os
os.environ["OPENAI_API_KEY"] = "NA"

llmOllama = ChatOllama(
    model = "llama3.1",
    base_url = "http://localhost:11434")

general_agent = Agent(
    role='Líder de Desenvolvimento de Ontologias',
    goal='Liderar a equipe na produção de um texto abrangente e tecnicamente preciso sobre CrewAI, garantindo a qualidade e a coerência do conteúdo.',
    backstory=(
        'Como líder da equipe, este membro será responsável por definir a estrutura do texto introdutório, estabelecer o escopo do conteúdo, supervisionar o trabalho dos demais membros, garantir a qualidade técnica do material e integrar as diferentes partes do texto em um todo coeso. '
        'Sua experiência em desenvolvimento e aplicação de CrewAI será crucial para garantir a precisão e relevância do conteúdo técnico.'
    ),
    tools=[],
    allow_delegation=False,  
    llm=llmOllama 
)

task = Task(description="""o que é o CrewAI?""",
             agent = general_agent,
             expected_output="respostas em portugues.",
             output_file='resposta.txt')

crew = Crew(
            agents=[general_agent],
            tasks=[task],
            verbose=True
        )

result = crew.kickoff()

print(result)