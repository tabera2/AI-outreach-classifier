import torch
import joblib
from pytorch_model import OutreachNeuralNetwork


# Load preprocessing tools
vectorizer = joblib.load("models/pytorch_vectorizer.joblib")
label_encoder = joblib.load("models/pytorch_label_encoder.joblib")

# Initialize neural network
input_size = len(vectorizer.get_feature_names_out())

model = OutreachNeuralNetwork(
    input_size=input_size,
    num_classes=len(label_encoder.classes_)
)

# Load trained weights
model.load_state_dict(
    torch.load(
        "models/outreach_pytorch.pth",
        map_location="cpu",
        weights_only=True
    )
)

model.eval()


def classify_message_pytorch(message):
    # Convert text into TF-IDF features
    features = vectorizer.transform([message])

    # Convert features into a PyTorch tensor
    input_tensor = torch.tensor(
        features.toarray(),
        dtype=torch.float32
    )

    # Generate prediction
    with torch.no_grad():
        outputs = model(input_tensor)

        probabilities = torch.softmax(outputs, dim=1)

        predicted_index = torch.argmax(
            probabilities,
            dim=1
        ).item()

        confidence = probabilities[0][predicted_index].item()

    # Convert numerical prediction into category name
    prediction = label_encoder.inverse_transform(
        [predicted_index]
    )[0]

    return prediction, confidence


if __name__ == "__main__":
    test_messages = [
        "I want to become a kidney donor.",
        "My father needs a kidney transplant.",
        "Our company wants to advertise on your website.",
        "I cannot log into my account."
    ]

    for message in test_messages:
        prediction, confidence = classify_message_pytorch(message)

        print(f"\nMessage: {message}")
        print(f"Prediction: {prediction}")
        print(f"Confidence: {confidence:.1%}")