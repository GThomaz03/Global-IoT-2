# generative_service.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-pro')

def analyze_resume_text(resume_text):
    """Envia o texto do currículo para o Gemini e pede uma análise estruturada."""
    
    # --- AQUI ESTÁ A ENGENHARIA DE PROMPT! ---
    prompt = f"""
    Você é um assistente de RH sênior, especialista em análise de currículos para a área de tecnologia.
    Analise o texto do currículo a seguir e extraia as seguintes informações em um formato JSON VÁLIDO.
    
    O JSON deve ter EXATAMENTE a seguinte estrutura:
    {{
      "technical_skills": ["lista de competências técnicas"],
      "soft_skills": ["lista de competências comportamentais"],
      "experience_years": "número aproximado de anos de experiência total",
      "education": ["lista de formações acadêmicas"],
      "summary": "Um resumo profissional de 2 a 3 frases sobre o candidato."
    }}
    
    Se uma informação não for encontrada, retorne um array vazio ou uma string vazia.
    NÃO inclua nenhuma explicação ou texto antes ou depois do JSON.
    
    Texto do Currículo:
    ---
    {resume_text}
    ---
    """
    
    response = model.generate_content(prompt)
    # Limpeza para garantir que apenas o JSON seja retornado
    cleaned_response = response.text.strip().replace("```json", "").replace("```", "")
    return cleaned_response

def generate_development_plan(user_profile_json, job_requirements_json):
    """Gera um plano de estudos com base no perfil do usuário e nos requisitos da vaga."""
    
    prompt = f"""
    Você é um coach de carreira e mentor técnico.
    Um profissional com o seguinte perfil:
    --- Perfil do Usuário ---
    {user_profile_json}
    ---
    
    Deseja se candidatar a uma vaga com os seguintes requisitos:
    --- Requisitos da Vaga ---
    {job_requirements_json}
    ---
    
    Sua tarefa é identificar as lacunas de competências (gaps) entre o perfil do usuário e os requisitos da vaga.
    Com base nesses gaps, crie um plano de estudos e desenvolvimento prático e detalhado.
    
    O plano deve ser formatado em Markdown e conter:
    1.  **Competências a Desenvolver:** Liste as principais competências que o usuário precisa adquirir.
    2.  **Plano de Ação Sugerido:** Para cada competência, sugira de 2 a 3 passos práticos, como "Fazer o curso X na plataforma Y", "Desenvolver um projeto pessoal Z que use esta tecnologia", "Ler a documentação oficial sobre W".
    3.  **Dica de Ouro:** Uma dica final para ajudar o profissional a se destacar.
    """
    
    response = model.generate_content(prompt)
    return response.text