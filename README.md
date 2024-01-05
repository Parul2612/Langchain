# Pet Name Generator
## Overview
This repository contains a Streamlit web application for generating pet names based on animal type and color. The pet names are generated using the LangChain library and Google's Generative AI model.
## Files and Structure
### pet_name_generator.py: 
This Python script defines the main logic for generating pet names. It uses the LangChain library and Google's Generative AI model.

### app.py: 
This is the Streamlit web application script. It uses streamlit for the user interface and interacts with the pet name generator script.

### langchain_helper.py: 
This file includes helper functions for interacting with the LangChain library and Google's Generative AI model.

### .env: 
An environment file to store any necessary credentials or API keys.
## Dependencies
Make sure to install the required dependencies using the following:

 `pip install langchain streamlit python-dotenv`
## How to Run
### 1. Clone the repository:

`git clone https://github.com/Parul2612/Langchain.git`

### 2. Create a virtual environment:

`python -m venv venv``
`venv\Scripts\Activate\ps1`
### 3. Install dependencies:
`pip install -q --upgrade google-generativeai langchain-google-genai python-dotenv`

### 4. Run the Streamlit app:
`streamlit run app.py`

Open your browser and go to [http://localhost:8501](url) to use the Pets Name Generator.
