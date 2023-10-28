import streamlit as st
import google.generativeai as genai
import api

# Configure the API key
genai.configure(api_key=api.api_key)

# Set default parameters
defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

# Create a text input for the prompt
prompt = st.text_input("Enter your prompt:")

# When the 'Generate' button is pressed, generate the text
if st.button('Generate'):
    response = genai.generate_text(
      **defaults,
      prompt=prompt
    )
    st.write(response.result)