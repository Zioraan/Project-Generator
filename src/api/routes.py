"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
import openai

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/generate', methods=['POST'])
def generate_text():
    try:
        # Get the prompt from the incoming request
        data = request.get_json()
        prompt = data.get('prompt', '')

        # Use OpenAI to generate text based on the prompt
        response = openai.Completion.create(
            model="text-davinci-003",  # You can use GPT-3 or GPT-4 if you have access
            prompt=prompt,
            max_tokens=100
        )

        # Return the response text from OpenAI
        return jsonify({
            "response": response.choices[0].text.strip()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400