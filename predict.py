import joblib
from pathlib import Path

# Locate the saved model
MODEL_PATH = Path(__file__).resolve().parent / "models" / "outreach_classifier.joblib"

# Load the trained model
model = joblib.load(MODEL_PATH)

print("Model loaded successfully!")

def classify_message(message):
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]
    confidence = max(probabilities)
    return prediction, confidence

def show_probabilities(message):
    probabilities = model.predict_proba([message])[0]
    for category, probability in zip(model.classes_, probabilities):
        print(f"{category}: {probability:.1%}")


if __name__ == "__main__":
    message = input("Enter an outreach message: ")
    category, confidence = classify_message(message)

    print(f"\nPredicted category: {category}")
    print(f"Confidence: {confidence:.1%}")
    print("\nAll category probabilities:")
    show_probabilities(message)