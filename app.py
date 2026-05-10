from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='public')

API_URL = "https://cloud.flowiseai.com/api/v1/prediction/0dd4bc76-534b-405a-97fc-4160253a1ba4"

@app.route("/")
def home():
    return send_from_directory("public", "index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    question = data.get("question")

    try:
        response = requests.post(
            API_URL,
            json={
                "question": question
            }
        )

        result = response.json()

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "text": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True, port=5000)