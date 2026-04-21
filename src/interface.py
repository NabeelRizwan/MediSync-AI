def interactive_patient_consultation(orchestrator):
    print("=== MediSync AI ===")

    pid = input("Patient ID: ")
    age = input("Age: ")
    sex = input("Sex: ")
    complaint = input("Symptoms: ")

    data = {
        "patient_id": pid,
        "age": age,
        "sex": sex,
        "chief_complaint": complaint,
        "vital_signs": {},
        "medications": []
    }

    image = input("Image path (optional): ") or None

    result = orchestrator.process_patient_case(
        pid, data, complaint, image
    )

    print("\n--- RESULTS ---")
    print(result["diagnosis"]["differential_diagnosis"])
    print("\nTreatment:\n", result["treatment"]["treatment_plan"])
