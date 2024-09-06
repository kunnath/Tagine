import subprocess

import streamlit as st
import pytesseract
from PIL import Image
from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def extract_text_from_image(image):
    """Extract text from an image using OCR."""
    try:
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(image)
        return text.strip()  # Strip leading/trailing whitespace
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return ""

def evaluate_answer(correct_answer, student_answer):
    """Compare the student's answer with the correct answer using sentence embeddings."""
    # Encode the text
    correct_embedding = model.encode(correct_answer, convert_to_tensor=True)
    student_embedding = model.encode(student_answer, convert_to_tensor=True)
    
    # Compute similarity
    similarity_score = util.pytorch_cos_sim(correct_embedding, student_embedding).item()
    
    return similarity_score

def compare_texts(correct_text, student_text):
    """Compare two texts and highlight differences."""
    stop_words = set(stopwords.words('english'))
    
    # Tokenize and filter stopwords
    correct_tokens = [word.lower() for word in word_tokenize(correct_text) if word.isalnum() and word.lower() not in stop_words]
    student_tokens = [word.lower() for word in word_tokenize(student_text) if word.isalnum() and word.lower() not in stop_words]
    
    correct_freq = FreqDist(correct_tokens)
    student_freq = FreqDist(student_tokens)
    
    correct_set = set(correct_tokens)
    student_set = set(student_tokens)
    
    common_words = correct_set.intersection(student_set)
    diff_words = (correct_set - student_set).union(student_set - correct_set)
    
    return {
        'common_words': common_words,
        'diff_words': diff_words,
        'correct_freq': correct_freq,
        'student_freq': student_freq
    }

# Run the shell script before proceeding
subprocess.run(["/bin/bash", "run.sh"], check=True)

st.title("Answer Evaluation App")



# File upload widgets
correct_answer_image = st.file_uploader("Upload the correct answer image", type=["jpg", "png"])
student_answer_image = st.file_uploader("Upload the student's answer image", type=["jpg", "png"])

if correct_answer_image and student_answer_image:
    # Extract text from images
    correct_answer_text = extract_text_from_image(Image.open(correct_answer_image))
    student_answer_text = extract_text_from_image(Image.open(student_answer_image))

    # Evaluate student's answer
    similarity_score = evaluate_answer(correct_answer_text, student_answer_text)
    
    # Compare texts
    comparison = compare_texts(correct_answer_text, student_answer_text)
    
    st.write(f"Correct Answer Text: {correct_answer_text}")
    st.write(f"Student Answer Text: {student_answer_text}")
    st.write(f"Similarity Score: {similarity_score:.4f}")

    st.write("### Common Words")
    st.write(", ".join(comparison['common_words']))
    
    st.write("### Different Words")
    st.write(", ".join(comparison['diff_words']))
    
    st.write("### Frequency Distribution of Words in Correct Answer")
    st.write(comparison['correct_freq'])
    
    st.write("### Frequency Distribution of Words in Student Answer")
    st.write(comparison['student_freq'])
    
    # Explanation
    st.write("### Explanation")
    st.write("The similarity score may be lower than expected due to differences in vocabulary, phrasing, or content specifics between the correct answer and the student's answer. Differences in wording, missing terms, or different interpretations can contribute to a lower similarity score.")