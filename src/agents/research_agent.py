import datetime
from config import client

class ResearchAgent:
    def __init__(self, model_name='models/gemini-2.5-flash'):
        self.model_name = model_name
        self.search_history = []

    def search_medical_literature(self, query):
        prompt = f"Medical research on: {query}"

        response = client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )

        result = {
            "query": query,
            "findings": response.text,
            "timestamp": datetime.datetime.now().isoformat()
        }

        self.search_history.append(result)
        return result
