import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
client = genai.Client()

MODELO = "gemini-1.5-flash"
chat = client.chats.create(model=MODELO)

def analisar_respostas(respostas):
    prompt = f"""
    Analise as respostas do teste de perfil de investimento abaixo:
    
    {respostas}
    
    Com base nessas respostas:
    1. Identifique o nível de tolerância a risco (conservador, moderado ou arrojado) e explique.
    2. Sugira 2-3 classes de ativos ou estratégias de investimento adequadas.
    3. Explique brevemente por que estas opções se alinham com o perfil identificado.
    
    Formato da resposta:
    - Comece com "Com base nas suas respostas, identifiquei que seu perfil de investimento é..."
    - Use linguagem clara e profissional, evitando jargões complexos
    - Seja específico nas sugestões (ex: "70% renda fixa, 30% ações" ao invés de "investimentos diversificados")
    - Inclua uma breve mensagem sobre a importância de manter a estratégia adequada ao perfil

    Mantenha a resposta objetiva e focada nos dados fornecidos, destacando os pontos mais relevantes e evitando textos extensos.
    """
    
    try:
        resposta = chat.send_message(prompt)
        return resposta.text.strip()

    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return "Não foi possível gerar a análise no momento."
