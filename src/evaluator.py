class AgentEvaluator:
    def evaluate_workflow(self, result):
        return {
            "completeness": 100 if result else 0
        }
