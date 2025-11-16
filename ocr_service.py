# ocr_service.py
import os
import requests
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env

OCR_SPACE_API_KEY = os.getenv("OCR_SPACE_API_KEY") # Pegue no site deles

def extract_text_from_file(file_content, file_type):
    """Usa a API do ocr.space para extrair texto."""
    payload = {
        'isOverlayRequired': False,
        'apikey': OCR_SPACE_API_KEY,
        'language': 'por',
    }
    
    file_extension = 'pdf' if file_type == 'pdf' else 'png' # Ou outro formato de imagem
    files = {
        f'filename.{file_extension}': (f'resume.{file_extension}', file_content)
    }
    
    response = requests.post(
        'https://api.ocr.space/parse/image',
        files=files,
        data=payload,
    )
    response.raise_for_status() # Lança um erro se a requisição falhar

    result = response.json()
    if result.get('IsErroredOnProcessing'):
        raise Exception(result.get('ErrorMessage')[0])
    
    return result['ParsedResults'][0]['ParsedText']