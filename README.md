# FAQ Customer Support Chatbot

This is a simple AI-driven chatbot built with Streamlit and spaCy to assist users with frequently asked questions (FAQs) related to customer support.

## Watch Demo
[![Watch the video](https://img.youtube.com/vi/sImf3MkfvfM/0.jpg)](https://www.youtube.com/watch?v=sImf3MkfvfM)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Using Docker](#using-docker)
- [Usage](#usage)
- [Training](#training)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Customer Support Chatbot is designed to provide quick answers to common queries that users might have regarding policies and services. It uses natural language processing (NLP) to match user questions with predefined FAQs and provides appropriate responses.

## Features

- **FAQ Handling**: Answers questions based on a set of predefined FAQs stored in a JSON file.
- **Greeting and Farewell**: Recognizes basic greetings and farewells and responds accordingly.
- **Interactive Interface**: Allows users to interact with the chatbot through a web-based UI powered by Streamlit.
- **Fallback Response**: Provides a default response when a user query does not match any FAQ above a certain similarity threshold.

## Demo

You can see a live demo of the chatbot [here](https://customer-support-chatbotapp-intent-classification.streamlit.app/).

## Setup

### Prerequisites

Ensure you have the following installed:

- Python (>=3.10)
- pip (package installer for Python)
- [Poetry](https://python-poetry.org/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Jayanth-MKV/customer-support-chatbotapp-intent-classification
   cd customer-support-chatbot
   ```

2. Install the required Python packages using Poetry:

   ```bash
   poetry install
   ```

3. Run the app:

   ```bash
    poetry run streamlit run app.py
   ```

### Using Docker (recommended)

If you prefer using Docker, you can pull the Docker image and run the application in a container:

1. Pull the Docker image:

   ```bash
    docker pull jayanthmkv/customer-support-intent-classification-chatbot:latest
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8501:8501 jayanthmkv/customer-support-intent-classification-chatbot:latest
   ```

## Usage

1. **Run the Application**:

   If you are using Poetry:

   ```bash
   poetry run streamlit run app.py
   ```

   If you are using Docker, the application should be running after the container starts. You can check at [http://localhost:8501](http://localhost:8501)

2. **Interact with the Chatbot**:
   
   - Once the application starts, you'll see the chat interface.
   - Type your question or select from predefined FAQ buttons.
   - Click "Send" to see the bot's response.
   - The chat history will be displayed in the interface.

## Training

## Obtained 97% accuracy on spacy Kaggle and also nearly 99% with 30 epochs 

### The current intent_model has 99% accuracy

This Uses spaCy for intent classification and Streamlit for the user interface.
refer these : 
1. https://www.width.ai/post/spacy-text-classification
2. https://spacy.io/usage/training
3. https://www.kaggle.com/jayanthmkv/intent-classify-spacy

### Training the Model

1. Prepare your training data in a CSV file named `intent_data.csv` with columns:
   - utterance: The user's message
   - intent: The corresponding intent
   - category: (optional) Category of the intent
   - tags: (optional) Any relevant tags

from here ( https://www.kaggle.com/datasets/scodepy/customer-support-intent-dataset )

2. Install required libraries:
   ```
      pip install spacy pandas scikit-learn
   ```

3. Run the training script:
   ```python
   python train_model.py
   ```

   This script will:
   - Load the data from `intent_data.csv`
   - Split the data into training and testing sets
   - Create a spaCy text classification model
   - Train the model on the data
   - Save the trained model as "intent_model"
   - build the application

The chatbot application:
- Loads the trained spaCy model
- Uses regular expressions to identify greetings and farewells
- Classifies other user inputs using the spaCy model
- Provides responses based on the classified intent
- Uses a confidence threshold to determine when to use fallback responses
- Displays the conversation history in a user-friendly interface

## Customization

- Adjust the `CONFIDENCE_THRESHOLD` in `chatbot_app.py` to fine-tune the chatbot's response behavior.
- Modify the `intents_responses` dictionary in `chatbot_app.py` to change or add specific responses for each intent.
- Update the greeting and farewell patterns in `chatbot_app.py` to recognize different expressions.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](MIT) file for details.