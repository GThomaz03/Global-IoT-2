# app.py
from flask import Flask, request, jsonify
import json
from ocr_service import extract_text_from_file
from generative_service import analyze_resume_text, generate_development_plan

app = Flask(__name__)

@app.route('/analyze-resume', methods=['POST'])
def analyze_resume_endpoint():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Arquivo sem nome"}), 400

    try:
        # Detecta o tipo de arquivo pela extensão
        file_extension = file.filename.rsplit('.', 1)[1].lower()
        file_type = 'pdf' if file_extension == 'pdf' else 'image'

        file_content = file.read()
        
        extracted_text = extract_text_from_file(file_content, file_type)
        
        if not extracted_text.strip():
             return jsonify({"error": "Nenhum texto foi extraído do arquivo. Verifique a qualidade da imagem/documento."}), 400

        analysis_json_str = analyze_resume_text(extracted_text)
        analysis_json = json.loads(analysis_json_str)
        
        return jsonify(analysis_json), 200

    except Exception as e:
        return jsonify({"error": f"Ocorreu um erro interno: {str(e)}"}), 500



@app.route('/generate-plan', methods=['POST'])
def generate_plan_endpoint():
    try:
        data = request.get_json()
        user_profile = data.get('user_profile')
        job_requirements = data.get('job_requirements')

        if not user_profile or not job_requirements:
            return jsonify({"error": "user_profile e job_requirements são obrigatórios"}), 400
        
        # Converte os dicionários Python em strings JSON formatadas para o prompt
        user_profile_str = json.dumps(user_profile, indent=2)
        job_req_str = json.dumps(job_requirements, indent=2)

        # Passo 3: Gerar plano de estudos com IA Generativa
        plan_markdown = generate_development_plan(user_profile_str, job_req_str)
        
        return jsonify({"development_plan": plan_markdown}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Use uma porta diferente para não conflitar com outras APIs