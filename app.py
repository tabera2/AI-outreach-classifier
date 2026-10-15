import streamlit as st
from predict import classify_message
from predict import classify_message
from predict_pytorch import classify_message_pytorch


st.title("AI Outreach Classifier")
st.write(
    "Classify incoming messages as donor, patient, "
    "advertiser, or general inquiries."
)
# Select classification model
model_choice = st.selectbox(
    "Choose a classification model:",
    ["Logistic Regression", "PyTorch Neural Network"]
)

# Enter message
message = st.text_area(
    "Enter an outreach message:",
    placeholder="Type your message here..."
)

# Classify message
if st.button("Classify Message"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        if model_choice == "Logistic Regression":
            prediction, confidence = classify_message(message)
        else:
            prediction, confidence = classify_message_pytorch(message)

        st.success(f"Predicted Category: {prediction.capitalize()}")
        st.write(f"Confidence: {confidence:.1%}")