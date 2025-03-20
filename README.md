# Projeto de Tradução com LangChain e ChatGroq

## 📌 Descrição
Este projeto utiliza a biblioteca [LangChain](https://python.langchain.com/) em conjunto com a API do [ChatGroq](https://groq.com/) para traduzir frases para diferentes idiomas. A abordagem utilizada permite o encadeamento de componentes (LLMs, prompts e parsers) para criar fluxos de execução eficientes e personalizáveis.

## 🚀 Funcionalidades
- Integração com a API do ChatGroq para processamento de linguagem natural (LLM).
- Uso de prompts dinâmicos para diferentes estratégias de tradução (Few-shot, Zero-shot, One-shot, Chain of Thoughts).
- Parsing estruturado das respostas do modelo para melhor manipulação dos resultados.
- Configuração simples via variáveis de ambiente.

## 🏗 Estrutura do Projeto
```
📂 projeto-traducao
├── .gitignore
├── requirements.txt
├── .env (deve ser criado manualmente)
├── main.py
└── README.md
```

### 🔧 Dependências
O projeto utiliza as seguintes bibliotecas:
- `langchain-core`
- `langchain-groq`
- `python-dotenv`
- `os` (padrão do Python)

Todas as dependências estão listadas no arquivo `requirements.txt`.

## 📜 Instalação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/projeto-traducao.git
cd projeto-traducao
```

### 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto e adicione a chave de API do Groq:
```env
GROQ_API_KEY=your_api_key_here
```

## 🚀 Como Usar

### Executando o script
```bash
python main.py
```

### Exemplo de Saída
```bash
Guten Morgen, wie geht es Ihnen?
```

## 🛠 Estrutura do Código

### 1️⃣ Importação de bibliotecas
```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os
```

### 2️⃣ Carregamento das variáveis de ambiente
```python
load_dotenv(find_dotenv())
groq_api_key = os.getenv('GROQ_API_KEY')
```

### 3️⃣ Criação do modelo LLM
```python
llm = ChatGroq(
    model='Gemma2-9b-It',
    groq_api_key=groq_api_key,
)
```

### 4️⃣ Definição do prompt template
```python
generic_template = "Traduza a seguinte frase em {language}"

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("user", "{text}")
])
```

### 5️⃣ Encadeamento da execução (Chain)
```python
parser = StrOutputParser()
chain = prompt | llm | parser
```

### 6️⃣ Execução do modelo
```python
result = chain.invoke({'language': 'German', 'text': 'bom dia, como você está?'})
print(result)
```

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir conforme necessário.

## 📩 Contato
Para dúvidas ou sugestões, entre em contato via [raphaelguizan@gmail.com](mailto:raphaelguizan@gmail.com).

