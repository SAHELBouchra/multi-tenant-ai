class AIAgent:
    def __init__(self, model):
        self.model = model

    def build_prompt(self, question: str, documents: str) -> str:
        return f"""
Tu es un assistant IA professionnel.

RÈGLES STRICTES :
- Tu dois répondre UNIQUEMENT à partir des documents fournis.
- Si l'information n'est pas présente, répond exactement :
  "Aucune réponse possible pour ce client."
- N'invente jamais d'information.
- N'utilise aucune connaissance externe.

DOCUMENTS DU CLIENT :
{documents}

QUESTION :
{question}

RÉPONSE :
"""

    def run(self, question: str, documents: str) -> str:
        if not documents.strip():
            return "Aucune réponse possible pour ce client."

        prompt = self.build_prompt(question, documents)
        response = self.model.generate_content(prompt)
        return response.text.strip()
