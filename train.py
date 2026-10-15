import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load dataset
DATA_PATH = Path(__file__).resolve().parent / "data" / "outreach_messages.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print(df.head())
print(f"\nTotal messages: {len(df)}")

# Separate input messages from their labels
X = df["text"]
y = df["label"]

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# Create a machine learning pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train the model
model.fit(X_train, y_train)
print("\nModel trained successfully!")

# Predict labels for the test dataset
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2%}")

# Display precision, recall, and F1-score
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Test on new, independently written messages
new_messages = [
    "I am willing to give one of my kidneys to help save a life.",
    "My sister has kidney failure and we are desperate for help.",
    "Our agency specializes in digital promotions for nonprofit organizations.",
    "I cannot access my account after resetting my password.",
    "I recently learned that I might be eligible to donate an organ.",
    "My husband has been undergoing dialysis for three years.",
    "We would love to feature your organization in our upcoming campaign.",
    "I tried submitting the contact form, but it keeps showing an error."
]

expected_labels = [
    "donor",
    "patient",
    "advertiser",
    "general",
    "donor",
    "patient",
    "advertiser",
    "general"
]

predictions = model.predict(new_messages)

print("\nIndependent Message Predictions:")
print("-" * 70)

for message, expected, predicted in zip(
    new_messages, expected_labels, predictions
):
    result = "CORRECT" if expected == predicted else "INCORRECT"

    print(f"\nMessage: {message}")
    print(f"Expected: {expected}")
    print(f"Predicted: {predicted}")
    print(f"Result: {result}")

independent_accuracy = accuracy_score(expected_labels, predictions)

print(f"\nIndependent Test Accuracy: {independent_accuracy:.2%}")
# Save the trained model
MODEL_PATH = Path(__file__).resolve().parent / "models" / "outreach_classifier.joblib"

# Create the models directory if it doesn't exist
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

# Save the complete pipeline
joblib.dump(model, MODEL_PATH)

print(f"\nModel saved successfully to: {MODEL_PATH}")