import os
import google.cloud.logging

from flask import Flask, jsonify, make_response, request

from src.gemini_handler import get_clean_product_name

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "app_credentials.json"

app = Flask(__name__)


@app.before_first_request
def setup_logging():
    # Instantiates a client
    client = google.cloud.logging.Client()

    # Retrieves a Cloud Logging handler based on the environment
    # you're running in and integrates the handler with the
    # Python logging module. By default this captures all logs
    # at INFO level and higher
    client.get_default_handler()
    client.setup_logging()


@app.route("/clean_product", methods=["POST"])
def clean_product():
    """Endpoint to process the JSON and return clean product name."""
    resp_data = []
    json_data = request.get_json()
    for product in json_data:
        resp_data.append(get_clean_product_name(product))
    return make_response(
        jsonify({"data": resp_data}),
        200,
    )


# if __name__ == "__main__":
#     app.run(debug=True)
