# IMPORTANDO BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

# CARREGANDO VARIÁVEIS DE AMBIENTE
load_dotenv(find_dotenv())
groq_api_key = os.getenv('GROQ_API_KEY')

# CRIAR O MODELO GROQ
llm = ChatGroq(
    model = 'Gemma2-9b-It', # MODELO DE LLM UTILIZADO
    groq_api_key = groq_api_key, # CHAVE DE API DO GROQ
)

# CRIAR O PROMPT (FEW-SHOT, ZERO-SHOT, ONE-SHOT, CHAIN OF THOUGHTS)
messages = [
    SystemMessage(content="Translate the following sentence from english to french"),
    HumanMessage(content="Hello, how are you?")
]

#PARSER DE SAÍDA: isso é necessário para que o sistema entenda a saída do modelo
parser = StrOutputParser()

# Prompt Template: Usando LCEL - chain the Components
generic_template = "Traduza a seguinte frase em {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", generic_template),
        ("user", "{text}") 
    ]
)

#CHAIN
chain = prompt | llm | parser

# EXecutar a chain
result = chain.invoke({'language':'German', 'text':'bom dia, como você está?'})
print(result)