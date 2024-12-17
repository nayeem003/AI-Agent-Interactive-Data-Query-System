import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_response(context):
    # Initialize Groq client with API Key
    client = Groq(api_key=GROQ_API_KEY)

    try:
        # Pass the context (which includes the dataset summary and query) to Groq's API for query completion
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": context}],
            model="llama3-8b-8192",  # You can adjust the model as needed
        )
        # Return the generated content (response) from the LLM
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error querying LLM: {e}"
