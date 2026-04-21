import datetime

class MediSyncOrchestrator:
    def __init__(self, research, diagnostic, treatment, visual, memory, context):
        self.research = research
        self.diagnostic = diagnostic
        self.treatment = treatment
        self.visual = visual
        self.memory = memory
        self.context = context
        self.workflow_log = []

    def process_patient_case(self, patient_id, patient_data, complaint, image_path=None):
        start = datetime.datetime.now()

        session_id = self.memory.create_session(patient_id, patient_data)

        summary = self.context.compact_patient_data(patient_data)

        visual_result = None
        if image_path:
            visual_result = self.visual.analyze_medical_image(image_path, summary)

        research = self.research.search_medical_literature(complaint)

        diagnosis = self.diagnostic.analyze_symptoms(
            summary, research["findings"]
        )

        treatment = self.treatment.generate_treatment_plan(
            diagnosis["differential_diagnosis"], summary
        )

        self.memory.store_long_term(patient_id, {
            "diagnosis": diagnosis,
            "treatment": treatment
        })

        duration = (datetime.datetime.now() - start).total_seconds()

        result = {
            "session_id": session_id,
            "duration": duration,
            "visual": visual_result,
            "research": research,
            "diagnosis": diagnosis,
            "treatment": treatment
        }

        self.workflow_log.append(result)
        return result
