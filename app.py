import streamlit as st
from predict import classify_message

st.set_page_config(
    page_title="AI Outreach Classifier",
    page_icon="📩",
    layout="centered"
)

st.title("📩 AI Outreach Classifier")

st.write(
    "Classify incoming outreach messages into four categories: "
    "Donor, Patient, Advertiser, or General."
)

message = st.text_area(
    "Enter an outreach message:",
    placeholder="Hi, I would like to learn how to become a kidney donor.",
    height=150
)

if st.button("Classify Message"):
    if not message.strip():
        st.warning("Please enter a message before classifying.")
    else:
        prediction, confidence = classify_message(message)
        st.success(f"Predicted Category: {prediction.title()}")
        st.write(f"Confidence: {confidence:.1%}")