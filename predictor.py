from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
my_client = Groq(api_key=os.getenv("Groq_api_key"))

def get_prediction(name, glucose, haemoglobin, cholesterol):
    my_prompt = f"""
    Patient Name: {name}
    Glucose: {glucose} mg/dL
    Haemoglobin: {haemoglobin} g/dL
    Cholesterol: {cholesterol} mg/dL
    Write a short health remark in 2 to 3 plain sentences only.
    Just a simple health observation.
    """
    result = my_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": my_prompt}]
    )
    return result.choices[0].message.content
