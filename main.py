from src.preprocessing import preprocess_input
from src.diagnosis import predict_disease
from src.ocr import extract_text_from_image

def main():
    print("=== MediSync AI ===")

    choice = input("1. Symptom Diagnosis\n2. Prescription OCR\nChoose option: ")

    if choice == "1":
        symptoms = input("Enter symptoms: ")
        processed = preprocess_input(symptoms)
        result = predict_disease(processed)
        print(f"Diagnosis: {result}")

    elif choice == "2":
        path = input("Enter image path: ")
        text = extract_text_from_image(path)
        print("Extracted Text:", text)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
