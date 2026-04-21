def interactive_patient_consultation(orchestrator):
    print("MediSync AI")

    pid = input("Patient ID: ")
    complaint = input("Symptoms: ")

    data = {
        "patient_id": pid,
        "age": input("Age: "),
        "sex": input("Sex: "),
        "chief_complaint": complaint
    }

    result = orchestrator.process_patient_case(pid, data, complaint)

    print("\nDiagnosis:\n", result["diagnosis"]["differential_diagnosis"])
    print("\nTreatment:\n", result["treatment"]["treatment_plan"])
