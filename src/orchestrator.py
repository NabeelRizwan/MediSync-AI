import datetime

class MediSyncOrchestrator:
    def __init__(self, research, diagnostic, treatment, visual, memory, context):
        self.research = research
        self.diagnostic = diagnostic
        self.treatment = treatment
        self.visual = visual
        self.memory = memory
        self.context = context

    def process_patient_case(self, patient_id, patient_data, complaint):
        session_id = self.memory.create_session(patient_id, patient_data)

        summary = self.context.compact_patient_data(patient_data)

        research = self.research.search_medical_literature(complaint)
        diagnosis = self.diagnostic.analyze_symptoms(summary, research["findings"])
        treatment = self.treatment.generate_treatment_plan(
            diagnosis["differential_diagnosis"], summary
        )

        return {
            "session_id": session_id,
            "research": research,
            "diagnosis": diagnosis,
            "treatment": treatment
        }
