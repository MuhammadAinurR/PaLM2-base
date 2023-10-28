demo : https://chatbot-palm-rofiq.streamlit.app/

# Streamlit Text Generation App
This is a simple Streamlit web application that allows you to generate text using the Google Generative AI API. You can provide a text prompt, and the application will generate text based on the provided input.

# Getting Started
Before using this application, you need to configure the Google Generative AI API by providing your API key. Make sure you have obtained an API key and have it ready. You will need to replace api.api_key with your actual API key in the code.

    # Configure the API key
    genai.configure(api_key=api.api_key)

# Default Parameters
The application provides some default parameters for text generation. These parameters control the behavior of the text generation process. You can modify these defaults according to your preferences:

- model: The specific model to use for text generation. The default model is 'models/text-bison-001'.
- temperature: A parameter controlling the randomness of generated text. The lower the value, the more deterministic the text.
- candidate_count: Number of candidate texts to consider for selection.
- top_k: Controls the diversity of generated text by considering only the top-k words with the highest probabilities.
- top_p: A threshold that controls the diversity of generated text by considering words with cumulative probabilities up to this threshold.

# Input Prompt
You can enter your desired text prompt in the text input field provided by the application. This prompt will serve as the starting point for text generation.

# Generating Text
Once you have entered your prompt, click the 'Generate' button. The application will send the prompt to the Google Generative AI API with the specified parameters and display the generated text as a response.

# Running the Application
You can run this Streamlit app by executing it in your Python environment. Make sure you have installed Streamlit and any other necessary dependencies.

    streamlit run chatbot.py

# Note
Please ensure that you have the required API key and any other dependencies properly set up before running the application. The provided code assumes that you have already obtained the API key and have the necessary models accessible through the Google Generative AI API.

# example of application usage
![img_sample](https://github.com/MuhammadAinurR/PaLM2-base/blob/main/img/app_sample.png)

# Another example that you can develop from here
- ## Generate Next Research Direction suggestion
<br> just drop your abstract and it will generate your next paper direction suggestion
<br> demo : https://next-research-direction.streamlit.app/

<br> ![img_sample2](https://github.com/MuhammadAinurR/PaLM2-base/blob/main/img/app_sample2.png)

- ## Interaction with specific character personality
<br> you also can getting answer just like you have dialogue with gandalf (Gandalf the Grey, a wizard of Middle-earth)

<br> ![img_sample3](https://github.com/MuhammadAinurR/PaLM2-base/blob/main/img/app_sample3.png)
