import datetime
from config import client
from google.genai import types

class VisualDiagnosticAgent:
    def __init__(self, model_name='models/gemini-2.5-flash'):
        self.model_name = model_name

    def analyze_medical_image(self, image_path, clinical_context=""):
        with open(image_path, "rb") as f:
            img = f.read()

        response = client.models.generate_content(
            model=self.model_name,
            contents=[
                "Analyze this medical image",
                types.Part.from_bytes(data=img, mime_type='image/jpeg')
            ]
        )

        return {
            "analysis": response.text,
            "timestamp": datetime.datetime.now().isoformat()
        }
