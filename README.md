# Tagine
# Answer Evaluation App

## Overview

The Answer Evaluation App is a Streamlit-based application that allows users to evaluate and compare student answers against a correct answer using Optical Character Recognition (OCR) and sentence embeddings. The app extracts text from uploaded images, computes similarity scores, and provides insights into text differences and frequencies.

## Features

- Upload images containing the correct answer and the student's answer.
- Extract text from images using Tesseract OCR.
- Compare answers using sentence embeddings and compute a similarity score.
- Highlight common and different words between the correct answer and the student's answer.
- Display frequency distributions of words in both answers.
- Explanation of the similarity score and factors affecting it.

## Installation

### Prerequisites

- Python 3.7 or later
- Tesseract OCR (make sure it is installed on your system)

### Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>

#!/bin/bash

1.	Create run.sh Script
Ensure you have a run.sh script in your project directory with the following content:
# Activate the virtual environment
source venv/bin/activate

# Install required packages from requirements.txt
pip install -r requirements.txt

   chmod +x run.sh

streamlit run app.py


Usage Instructions

	1.	Open the application in your browser as directed by the Streamlit output.
	2.	Upload the image files containing the correct answer and the student’s answer.
	3.	The app will process the images, extract text, and display a similarity score.
	4.	Review the common and different words, frequency distributions, and the explanation of the similarity score.

    This `README.md` provides a comprehensive guide on how to set up and use the app, including prerequisites, installation steps, and troubleshooting tips. Adjust any placeholders and details according to your specific project setup and repository.