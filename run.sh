#!/bin/bash

# Activate the virtual environment
source /home/adminuser/venv/bin/activate

# Install required packages from requirements.txt
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py