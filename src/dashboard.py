def generate_dashboard(memory, orchestrator, evaluator):
    print("\n📊 DASHBOARD\n")

    print("Sessions:", len(memory.sessions))
    print("Patients:", len(memory.long_term_memory))
    print("Workflows:", len(orchestrator.workflow_log))

    if evaluator:
        print("Evaluations:", len(evaluator.evaluation_history))
