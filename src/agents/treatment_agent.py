import datetime
import re
from config import client

class TreatmentAgent:
    def __init__(self, model_name='models/gemini-2.5-flash'):
        self.model_name = model_name

    def generate_treatment_plan(self, diagnosis, patient_summary):
        prompt = f"""
        Diagnosis: {diagnosis}
        Patient: {patient_summary}

        Provide treatment plan.
        """

        response = client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )

        text = self.clean(response.text)

        return {
            "treatment_plan": text,
            "timestamp": datetime.datetime.now().isoformat()
        }

    def clean(self, text):
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()
