from src.memory import MemoryBank
from src.context import ContextCompactor
from src.agents.research_agent import ResearchAgent
from src.agents.diagnostic_agent import DiagnosticAgent
from src.agents.treatment_agent import TreatmentAgent
from src.agents.visual_agent import VisualDiagnosticAgent
from src.orchestrator import MediSyncOrchestrator
from src.evaluator import AgentEvaluator
from src.interface import interactive_patient_consultation

def main():
    print("🚀 MediSync AI Starting...")

    memory_bank = MemoryBank()
    context_compactor = ContextCompactor()
    research_agent = ResearchAgent()
    diagnostic_agent = DiagnosticAgent()
    treatment_agent = TreatmentAgent()
    visual_agent = VisualDiagnosticAgent()
    evaluator = AgentEvaluator()

    orchestrator = MediSyncOrchestrator(
        research_agent,
        diagnostic_agent,
        treatment_agent,
        visual_agent,
        memory_bank,
        context_compactor
    )

    interactive_patient_consultation()

if __name__ == "__main__":
    main()
