import time
import datetime
import re
from config import client
from google.genai import types

class TreatmentAgent:
    def __init__(self, model_name='models/gemini-2.5-flash'):
        self.model_name = model_name
        self.treatment_plans = []

    def generate_treatment_plan(self, diagnosis, patient_summary, max_iterations=1):
        base_prompt = f"""
        Diagnosis: {diagnosis}
        Patient: {patient_summary}

        Provide COMPLETE treatment plan with:
        - Immediate actions
        - Medications
        - Monitoring
        - Patient education
        - Alternatives
        """

        max_retries = 5
        complete_plan = ""

        for retry in range(max_retries):
            try:
                response = client.models.generate_content(
                    model=self.model_name,
                    contents=base_prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.1,
                        max_output_tokens=4000
                    )
                )

                text = self._clean_output(response.text)
                complete_plan = text

                if all(k in text for k in ["Immediate", "Medication", "Monitoring"]):
                    break

                time.sleep(2)

            except Exception as e:
                if "503" in str(e):
                    time.sleep(10)
                else:
                    raise

        result = {
            "diagnosis": diagnosis,
            "treatment_plan": complete_plan,
            "timestamp": datetime.datetime.now().isoformat()
        }

        self.treatment_plans.append(result)
        return result

    def _clean_output(self, text):
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()
