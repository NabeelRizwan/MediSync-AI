import datetime
from config import client

class DiagnosticAgent:
    def __init__(self, model_name='models/gemini-2.5-flash'):
        self.model_name = model_name

    def analyze_symptoms(self, patient_summary, research_context):
        prompt = f"""
        Diagnose:
        {patient_summary}

        Context:
        {research_context}
        """

        response = client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )

        return {
            "differential_diagnosis": response.text,
            "timestamp": datetime.datetime.now().isoformat()
        }
