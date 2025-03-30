import openai
import numpy as np
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Set the API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_prediction(prompt, samples=30, temperature=0.7):
    outputs = []
    for _ in range(samples):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        try:
            val = float(response['choices'][0]['message']['content'].strip())
            outputs.append(val)
        except ValueError:
            print("Non-numeric response received:", response['choices'][0]['message']['content'])
            continue
    return outputs

# Example prediction
context = "This is a temperature forecasting task in Montreal. Units are in Celsius.\n"
training_data = "Jan, -5\nFeb, -3\nMar, 2\nApr, 10\nMay, 16\nJun, 20\n"
query = "Jul,"

prompt = context + training_data + query
samples = get_prediction(prompt, samples=30)
print("Median:", np.median(samples))
print("95% CI:", np.percentile(samples, [2.5, 97.5]))
