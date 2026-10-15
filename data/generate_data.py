import pandas as pd
from pathlib import Path
import random
import itertools

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
        "How can I become a kidney donor?",
        "What steps should I take to donate my kidney?",
        "Can I give one of my kidneys to someone in need?",
        "Am I eligible to donate a kidney?",
        "I want to donate an organ but don't know where to start.",
        "Can healthy people donate a kidney while they're alive?",
        "Is it possible to donate my kidney to a stranger?",
        "I would like to volunteer as an organ donor.",
        "What medical tests are required before donating a kidney?",
        "How do I start the living donor evaluation process?",
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
        "How can I find a kidney donor?",
        "I need someone who can donate a kidney to me.",
        "Can you help me find a living organ donor?",
        "My doctor says I need a kidney transplant.",
        "I'm on the transplant waiting list.",
        "How can I register as a patient who needs a kidney?",
        "My family is searching for someone willing to donate.",
        "What should I do if I cannot find a matching donor?",
        "I need a transplant but don't know where to start.",
        "Can someone help me find a donor for my mother?",
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
        "I cannot log into my account.",
        "My password reset link is not working.",
        "The website keeps showing an error.",
        "I am having trouble accessing my profile.",
        "How can I update my account information?",
        "The contact form is not submitting.",
        "I forgot my password and need assistance.",
        "Can someone help me troubleshoot a website issue?",
        "I am unable to upload a document.",
        "The registration page is not loading correctly.",
        "Help with my account login issues",
        "I cannot log into my account",
        "I forgot my password",
        "How do I reset my password?",
        "My account is locked",
        "I am having trouble signing in",
        "The website is not letting me log in",
        "I need technical support with my account",
        "How can I update my account information?",
        "I am experiencing problems accessing my profile"
    ],
}

templates = {
    "donor": {
        "intents": [
            "I want to",
            "I would like to",
            "I'm interested in",
            "I'm hoping to",
            "I'd be willing to",
            "I'm considering",
            "I would be happy to",
            "I'm looking into",
            "I'd like information about",
            "I'm exploring how to",
        ],
        "actions": [
            "donate a kidney",
            "become a living organ donor",
            "help someone who needs a transplant",
            "register as a potential donor",
            "learn about kidney donation",
            "support a patient through organ donation",
            "find out whether I qualify to donate",
            "volunteer as a living donor",
            "begin the organ donation process",
            "offer to donate an organ",
        ],
    },
    "patient": {
        "intents": [
            "I need help with",
            "I'm looking for",
            "My family needs help with",
            "Could you assist me with",
            "I would like information about",
            "I'm searching for",
            "I need guidance on",
            "Can you help me with",
            "I'm trying to understand",
            "I would appreciate support with",
        ],
        "actions": [
            "finding a kidney donor",
            "locating a living organ donor",
            "registering as a transplant patient",
            "getting support during a transplant search",
            "finding transplant resources",
            "connecting with potential donors",
            "creating a patient profile",
            "understanding the transplant waiting process",
            "finding help for a family member needing a transplant",
            "navigating the organ donor matching process",
        ],
    },
    "advertiser": {
        "intents": [
            "We are interested in",
            "Our company would like to",
            "Could we discuss",
            "We would like information about",
            "Our marketing team is considering",
            "We are exploring",
            "I'd like to inquire about",
            "Our business wants to",
            "Can you provide details about",
            "We would like to learn about",
        ],
        "actions": [
            "advertising on your website",
            "sponsoring your newsletter",
            "purchasing banner advertising",
            "promoting our healthcare services",
            "running a marketing campaign",
            "sponsoring your online platform",
            "placing advertisements on your website",
            "exploring advertising partnerships",
            "reaching your audience through promotions",
            "purchasing promotional space",
        ],
    },
    "general": {
        "intents": [
            "I would like to know about",
            "Can you provide information about",
            "Could you explain",
            "Where can I find details about",
            "I'm curious about",
            "Can someone help me understand",
            "I'd appreciate information about",
            "I have a question about",
            "Could you tell me about",
            "I'm looking for information about",
        ],
        "actions": [
            "your organization's history",
            "your contact information",
            "your office location",
            "your operating hours",
            "your privacy policy",
            "your customer support options",
            "your website features",
            "your organization's mission",
            "your newsletter subscription",
            "your general services",
        ],
    },
}

random.seed(42)

rows = []

for label, texts in messages.items():

    # Keep the original 10 messages
    for text in texts:
        rows.append({
            "text": text,
            "label": label
        })

    # Generate additional messages
    intents = templates[label]["intents"]
    actions = templates[label]["actions"]

    combinations = list(itertools.product(intents, actions))

    random.shuffle(combinations)

    # Generate 90 additional messages
    remaining = 100 - len(texts)
    for intent, action in combinations[:remaining]:
        text = f"{intent} {action}."

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