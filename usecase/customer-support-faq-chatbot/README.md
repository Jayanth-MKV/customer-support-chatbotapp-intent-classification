# FAQ Customer Support Chatbot

This is a simple AI-driven chatbot built with Streamlit and spaCy to assist users with frequently asked questions (FAQs) related to customer support.

## Watch Demo
[![Watch the video](https://img.youtube.com/vi/BXHUBCi_xwY/0.jpg)](https://www.youtube.com/watch?v=BXHUBCi_xwY)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Using Docker](#using-docker)
- [Usage](#usage)
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

You can see a live demo of the chatbot [here](https://faqchatbot.streamlit.app/).

## Setup

### Prerequisites

Ensure you have the following installed:

- Python (>=3.10)
- pip (package installer for Python)
- [Poetry](https://python-poetry.org/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Jayanth-MKV/FAQ-Chatbot-CustomerSupport.git
   cd customer-support-chatbot
   ```

2. Install the required Python packages using Poetry:

   ```bash
   poetry install
   ```

3. Download the spaCy model:

   ```bash
   python -m spacy download en_core_web_md
   ```

4. Run the app:

   ```bash
    poetry run streamlit run app.py
   ```

### Using Docker

If you prefer using Docker, you can pull the Docker image and run the application in a container:

1. Pull the Docker image:

   ```bash
    docker pull jayanthmkv/faq-chatbot-spacy
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8501:8501 jayanthmkv/faq-chatbot-spacy
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