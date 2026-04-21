from src.memory import MemoryBank
from src.context import ContextCompactor
from src.agents.research_agent import ResearchAgent
from src.agents.diagnostic_agent import DiagnosticAgent
from src.agents.treatment_agent import TreatmentAgent
from src.agents.visual_agent import VisualDiagnosticAgent
from src.orchestrator import MediSyncOrchestrator
from src.evaluator import AgentEvaluator
from src.interface import interactive_patient_consultation
from src.dashboard import generate_dashboard

def main():
    memory = MemoryBank()
    context = ContextCompactor()

    research = ResearchAgent()
    diagnostic = DiagnosticAgent()
    treatment = TreatmentAgent()
    visual = VisualDiagnosticAgent()

    evaluator = AgentEvaluator()

    orchestrator = MediSyncOrchestrator(
        research, diagnostic, treatment, visual, memory, context
    )

    interactive_patient_consultation(orchestrator)

    generate_dashboard(memory, orchestrator, evaluator)

if __name__ == "__main__":
    main()
