"""
See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

API_TOKEN = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_TOKEN)


def get_clean_product_name(data):
    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    # data = {"id": 1, "product_name" : "Pixel 7 Brand New" }

    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

    product_name = data["product_name"]
    prompt = f"""Extract only the product name from the text: {product_name}\n
    Don't return anything else."""
    response = model.generate_content(prompt)
    # print(response.usage_metadata)
    data["product_name_clean"] = str(response.text).strip(" \n")
    print(data)
    return data
