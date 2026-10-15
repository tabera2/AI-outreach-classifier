# AI Outreach Classifier

An AI-powered text classification application that categorizes incoming outreach messages using traditional machine learning and a PyTorch neural network.

Built as an independent proof of concept inspired by the communication needs of organizations like MatchingDonors, this project demonstrates how machine learning can help automate message classification and support more efficient outreach management.

## Live Demo

**[Try the AI Outreach Classifier](https://ai-outreach-classifier.streamlit.app)**

**[GitHub Repository](https://github.com/tabera2/AI-outreach-classifier)**

## Overview

Organizations that receive inquiries from potential donors, patients, advertisers, and other visitors often need to manually review and categorize messages before directing them to the appropriate team.

This project explores how machine learning can automate the initial classification process.

Users can enter an outreach message, select a machine learning model, and receive a predicted category along with a confidence score.

## Features

- **Message Classification:** Automatically categorizes messages into donor, patient, advertiser, or general inquiries.
- **Multiple Machine Learning Models:** Supports Logistic Regression and a PyTorch neural network.
- **Model Comparison:** Allows users to switch between models and compare predictions.
- **Confidence Scores:** Displays the predicted probability for the selected category.
- **Interactive Web Interface:** Built with Streamlit for real-time message classification.
- **Reusable Models:** Saves trained models and preprocessing components for inference without retraining.

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core application development |
| scikit-learn | TF-IDF vectorization, Logistic Regression, and model evaluation |
| PyTorch | Neural network development and training |
| Pandas | Dataset preparation and processing |
| Joblib | Model and preprocessing serialization |
| Streamlit | Interactive web application |
| Git & GitHub | Version control and source code management |

## How It Works

The application supports two machine learning pipelines.

### Model 1: Logistic Regression

The first model uses TF-IDF to convert incoming messages into numerical features, followed by Logistic Regression for classification.

```text
Incoming Message
       |
       v
TF-IDF Vectorization
       |
       v
Logistic Regression
       |
       v
Predicted Category + Confidence
```

### Model 2: PyTorch Neural Network

The second model uses a feedforward neural network implemented with PyTorch.

The architecture consists of:

- Input layer containing TF-IDF features
- Fully connected hidden layer with 64 neurons
- ReLU activation function
- Output layer with four category scores
- Softmax function for prediction probabilities

```text
Incoming Message
       |
       v
TF-IDF Vectorization
       |
       v
Fully Connected Layer (64 neurons)
       |
       v
ReLU Activation
       |
       v
Output Layer (4 categories)
       |
       v
Softmax Probabilities
       |
       v
Predicted Category + Confidence
```

## Classification Categories

The application classifies incoming messages into four categories:

| Category | Description |
|----------|-------------|
| Donor | Individuals interested in becoming organ donors |
| Patient | Individuals seeking organ donors or transplant-related assistance |
| Advertiser | Organizations interested in advertising or promotional opportunities |
| General | Account support, website assistance, and other inquiries |

### Example

**Input:**

```text
I am interested in becoming a living kidney donor.
```

**Output:**

```text
Predicted Category: Donor
Confidence: Model-dependent
```

Users can select either Logistic Regression or PyTorch Neural Network to compare predictions.

## Dataset

The models were trained using a synthetic dataset containing 400 labeled outreach messages.

The dataset contains:

- 100 donor inquiries
- 100 patient inquiries
- 100 advertiser inquiries
- 100 general inquiries

The data was divided into:

- **Training Set:** 80% (320 messages)
- **Testing Set:** 20% (80 messages)

Both models use TF-IDF vectorization with unigrams and bigrams to represent message content.

## Model Training

### Logistic Regression

The baseline classifier was implemented using scikit-learn.

The training pipeline includes:

1. Loading and preprocessing the dataset.
2. Splitting messages into training and testing sets.
3. Converting text into TF-IDF features.
4. Training a Logistic Regression classifier.
5. Evaluating predictions.
6. Saving the trained pipeline using Joblib.

### PyTorch Neural Network

A second classifier was developed using PyTorch to explore neural network-based text classification.

The model uses:

- **Architecture:** Feedforward neural network
- **Hidden Layer:** 64 neurons
- **Activation Function:** ReLU
- **Loss Function:** CrossEntropyLoss
- **Optimizer:** Adam
- **Learning Rate:** 0.001
- **Training Epochs:** 50

The trained model weights are saved using `torch.save()`, while the TF-IDF vectorizer and label encoder are saved using Joblib.

## Model Evaluation

The PyTorch model achieved **97.5% test accuracy** on the synthetic dataset.

### PyTorch Classification Report

| Category | Precision | Recall | F1-Score |
|----------|-----------|--------|----------|
| Advertiser | 1.00 | 0.95 | 0.97 |
| Donor | 0.95 | 1.00 | 0.98 |
| General | 0.95 | 1.00 | 0.98 |
| Patient | 1.00 | 0.95 | 0.97 |

### Overall Performance

| Metric | Result |
|--------|--------|
| Test Accuracy | 97.5% |
| Macro Precision | 98% |
| Macro Recall | 98% |
| Macro F1-Score | 97% |

The model correctly classified 78 out of 80 testing messages.

**Evaluation Limitation:** The dataset was generated synthetically using predefined examples and templates. Similar language patterns may appear in both training and testing sets, potentially inflating evaluation results.

These metrics should not be interpreted as expected performance on real-world outreach messages. Additional evaluation using independent, human-reviewed data is necessary.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tabera2/AI-outreach-classifier.git
cd AI-outreach-classifier
```

### 2. Create a Virtual Environment

Python 3.11 is recommended.

```bash
python3.11 -m venv .venv
```

Activate the environment.

**macOS/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Project Structure

```text
AI-outreach-classifier/
|
|-- app.py
|-- predict.py
|-- predict_pytorch.py
|-- train.py
|-- train_pytorch.py
|-- pytorch_model.py
|-- requirements.txt
|-- README.md
|
|-- data/
|   |-- generate_data.py
|   |-- outreach_messages.csv
|
|-- models/
|   |-- outreach_classifier.joblib
|   |-- outreach_pytorch.pth
|   |-- pytorch_vectorizer.joblib
|   |-- pytorch_label_encoder.joblib
```

## Future Improvements

- Expand the dataset with more diverse and natural language examples.
- Evaluate both models using independently collected, human-reviewed messages.
- Explore pretrained transformer models for improved contextual understanding.
- Improve probability calibration and introduce confidence-based human review.
- Implement automated message routing based on predicted categories.
- Add a feedback mechanism to collect corrections and improve future predictions.
- Explore integration with outreach management platforms.

## Potential Applications

This project demonstrates how machine learning could support organizations that manage large volumes of incoming inquiries.

Potential applications include:

- Automated message categorization
- Outreach request organization
- Customer support ticket classification
- Message routing to appropriate departments
- Administrative workflow optimization

For organizations supporting patients and potential organ donors, this type of system could help staff organize incoming communications more efficiently while keeping sensitive decisions under human oversight.

## Disclaimer

This project is an independent proof of concept and is not affiliated with or endorsed by MatchingDonors.

The application uses synthetic training data and is not intended to make medical decisions, determine donor eligibility, or provide transplant recommendations.

It is designed for educational and demonstration purposes.