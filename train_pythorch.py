import torch
import torch.nn as nn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import os
import joblib



class OutreachNeuralNetwork(nn.Module):
    def __init__(self, input_size, num_classes=4):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        return self.network(x)

# Load dataset
df = pd.read_csv("data/outreach_messages.csv")
X = df["text"]
y = df["label"]

# Convert category names into numerical labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

# Convert text into numerical features
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    sublinear_tf=True
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Convert features into PyTorch tensors
X_train_tensor = torch.tensor(
    X_train_tfidf.toarray(),
    dtype=torch.float32
)

X_test_tensor = torch.tensor(
    X_test_tfidf.toarray(),
    dtype=torch.float32
)

y_train_tensor = torch.tensor(y_train, dtype=torch.long)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

print("Training data:", X_train_tensor.shape)
print("Testing data:", X_test_tensor.shape)
print("Categories:", label_encoder.classes_)

# Initialize the neural network
torch.manual_seed(42)

input_size = X_train_tensor.shape[1]
model = OutreachNeuralNetwork(input_size=input_size)

# Configure training
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

epochs = 50

# Training loop
for epoch in range(epochs):

    # Forward pass
    outputs = model(X_train_tensor)

    # Calculate loss
    loss = criterion(outputs, y_train_tensor)

    # Backpropagation
    optimizer.zero_grad()
    loss.backward()

    # Update model weights
    optimizer.step()

    # Display progress every 10 epochs
    if (epoch + 1) % 10 == 0:
        print(
            f"Epoch [{epoch + 1}/{epochs}], "
            f"Loss: {loss.item():.4f}"
        )

model.eval()

# Disable gradient calculations during evaluation
with torch.no_grad():
    # Generate predictions for the test dataset
    outputs = model(X_test_tensor)

    # Select the category with the highest score
    predictions = torch.argmax(outputs, dim=1)

# Convert predictions to NumPy arrays
y_pred = predictions.numpy()
y_true = y_test_tensor.numpy()

# Calculate accuracy
accuracy = accuracy_score(y_true, y_pred)

print(f"\nPyTorch Test Accuracy: {accuracy:.2%}")

# Show performance for each category
print("\nClassification Report:")
print(
    classification_report(
        y_true,
        y_pred,
        labels=list(range(len(label_encoder.classes_))),
        target_names=label_encoder.classes_,
        zero_division=0
    )
)

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save trained neural network weights
torch.save(
    model.state_dict(),
    "models/outreach_pytorch.pth"
)

# Save TF-IDF vectorizer and label encoder
joblib.dump(
    vectorizer,
    "models/pytorch_vectorizer.joblib"
)

joblib.dump(
    label_encoder,
    "models/pytorch_label_encoder.joblib"
)

print("\nPyTorch model and preprocessing tools saved successfully!")