# CareerForge AI - API de Análise Inteligente de Currículos

## Visão Geral do Projeto

Esta é a API de Inteligência Artificial para o projeto **CareerForge AI**. Ela serve como um microsserviço especializado, responsável por processar currículos e gerar insights de carreira usando tecnologias de Visão Computacional (OCR) e IA Generativa (Large Language Models).

A API expõe dois endpoints principais:

1.  **Análise de Currículo:** Recebe um arquivo de currículo (PDF ou imagem), extrai o texto e o estrutura em um formato JSON, identificando competências, experiência e formação.
2.  **Geração de Plano de Desenvolvimento:** Com base no perfil de um usuário e nos requisitos de uma vaga, gera um plano de estudos personalizado para ajudar o profissional a preencher suas lacunas de competências.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.9+
- **Framework da API:** Flask
- **Visão Computacional (OCR):** OCR.space API
- **IA Generativa:** Google Gemini Pro API
- **Gerenciamento de Dependências:** Pip com `requirements.txt`

---

## Configuração do Ambiente

Siga os passos abaixo para configurar e rodar o projeto localmente.

### 1. Pré-requisitos

- Python 3.9 ou superior instalado.
- Conta de API para [Google AI Studio (Gemini)](https://aistudio.google.com/).
- Conta de API para [OCR.space](https://ocr.space/).

### 2. Instalação

**a. Clone o repositório:**

```bash
git clone https://github.com/GThomaz03/Global-IoT-2
cd Global-IoT-2
```

**b. Crie e ative um ambiente virtual:**

```bash
# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
.\venv\Scripts\activate
```

**c. Instale as dependências:**

```bash
pip install -r requirements.txt
```

### 3. Variáveis de Ambiente

**a. Crie um arquivo `.env`** na raiz do projeto.

**b. Adicione suas chaves de API** ao arquivo `.env`:

```env
# Chave da API do Google Gemini
GOOGLE_API_KEY="SUA_CHAVE_GEMINI_AQUI"

# (Opcional) Chave da API do OCR.space
OCR_SPACE_API_KEY="SUA_CHAVE_OCR_SPACE_AQUI"
```

---

## Como Executar a API

Com o ambiente virtual ativado, inicie o servidor Flask com o seguinte comando:

```bash
python app.py
```

O servidor estará rodando e acessível em `http://127.0.0.1:5001`.

---

## Documentação dos Endpoints

### 1. Análise de Currículo

- **Endpoint:** `POST /analyze-resume`
- **Descrição:** Faz o upload de um arquivo de currículo e retorna um JSON com o perfil extraído.
- **Tipo de Corpo (Body):** `form-data`
- **Parâmetros:**
  - `key`: `file`
  - `type`: `File`
  - `value`: O arquivo do currículo (ex: `meu_curriculo.pdf`)
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "technical_skills": ["Python", "Flask", "Docker", "Git"],
    "soft_skills": ["Comunicação", "Liderança", "Resolução de Problemas"],
    "experience_years": "5",
    "education": ["Bacharelado em Ciência da Computação"],
    "summary": "Desenvolvedor de software sênior com 5 anos de experiência..."
  }
  ```

### 2. Geração de Plano de Desenvolvimento

- **Endpoint:** `POST /generate-plan`
- **Descrição:** Recebe o perfil do usuário e os requisitos de uma vaga, e retorna um plano de estudos em Markdown.
- **Tipo de Corpo (Body):** `raw (JSON)`
- **Corpo da Requisição (Exemplo):**
  ```json
  {
    "user_profile": {
      "technical_skills": ["Python", "Flask", "SQL"],
      "experience_years": "3"
    },
    "job_requirements": {
      "required_skills": ["Python", "Flask", "SQL", "Docker", "React"],
      "experience_needed": "5+ anos"
    }
  }
  ```
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "development_plan": "# Plano de Desenvolvimento Personalizado\n\n**1. Competências a Desenvolver:**\n- Docker\n- React\n\n**2. Plano de Ação Sugerido:**\n- **Docker:** Faça o curso 'Docker for Beginners' e crie um projeto pessoal..."
  }
  ```
