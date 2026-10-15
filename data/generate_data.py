import pandas as pd
from pathlib import Path

messages = {
    "donor": [
        "I want to become a living kidney donor.",
        "How can I register to donate an organ?",
        "I am interested in helping someone who needs a transplant.",
        "What are the requirements for becoming an organ donor?",
        "Can I donate a kidney to someone I do not know?",
        "I would like to learn about living organ donation.",
        "Where can I sign up as a potential donor?",
        "I am healthy and interested in kidney donation.",
        "Can you explain the organ donor registration process?",
        "I want to help patients waiting for a transplant.",
    ],
    "patient": [
        "I need help finding a kidney donor.",
        "My father is waiting for a liver transplant.",
        "How can patients register on your website?",
        "I am searching for a living kidney donor.",
        "My mother needs an organ transplant urgently.",
        "What resources are available for transplant patients?",
        "I want to create a patient profile.",
        "How can I connect with potential organ donors?",
        "My brother has been waiting for a transplant.",
        "Can your organization help me find a donor?",
    ],
    "advertiser": [
        "I would like to advertise on your website.",
        "What are your advertising rates?",
        "Our company wants to sponsor your newsletter.",
        "Do you offer banner advertising opportunities?",
        "We are interested in promoting our healthcare services.",
        "Can we purchase advertising space on your platform?",
        "I would like information about sponsorship packages.",
        "Our business wants to reach your website audience.",
        "Who should I contact about advertising partnerships?",
        "We are interested in running a marketing campaign.",
    ],
    "general": [
        "How can I contact your organization?",
        "Where is your office located?",
        "What are your operating hours?",
        "Can you tell me more about your organization?",
        "Is there a phone number I can call?",
        "How long has your organization been operating?",
        "Where can I find your privacy policy?",
        "Do you have a customer support email?",
        "I would like more information about your services.",
        "How can I subscribe to your newsletter?",
    ],
}

rows = []

for label, texts in messages.items():
    for text in texts:
        rows.append({
            "text": text,
            "label": label
        })

df = pd.DataFrame(rows)

output_path = Path(__file__).parent / "outreach_messages.csv"

df.to_csv(output_path, index=False)
print("Dataset created successfully!")
print(f"Total messages: {len(df)}")
print("\nCategory distribution:")
print(df["label"].value_counts())