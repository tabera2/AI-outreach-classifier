import joblib
from pathlib import Path

# Locate the saved model
MODEL_PATH = Path(__file__).resolve().parent / "models" / "outreach_classifier.joblib"

# Load the trained model
model = joblib.load(MODEL_PATH)

print("Model loaded successfully!")

def classify_message(message):
    prediction = model.predict([message])[0]
    return prediction


if __name__ == "__main__":
    message = input("Enter an outreach message: ")
    category = classify_message(message)
    print(f"\nPredicted category: {category}")