import json
import logging

logger = logging.getLogger(__name__)

class ContextCompactor:
    def __init__(self, max_tokens=8000):
        self.max_tokens = max_tokens

    def compact_patient_data(self, patient_data):
        essential = ["age", "sex", "chief_complaint", "vital_signs", "medications"]
        compacted = {k: v for k, v in patient_data.items() if k in essential}

        summary = f"Patient: {compacted.get('age')}yo {compacted.get('sex')}\n"
        summary += f"Chief Complaint: {compacted.get('chief_complaint')}\n"
        summary += f"Vitals: {json.dumps(compacted.get('vital_signs', {}))}\n"
        summary += f"Meds: {', '.join(compacted.get('medications', []))}"

        return summary
