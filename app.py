# from contentgen import generate_answer
# from llm_helper import llm
from flask import Flask, request, jsonify
from contentgen import generate_answer   # import your function
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"response": "Please ask a question."})

    answer = generate_answer(user_message)

    return jsonify({"response": answer})


if __name__ == "__main__":
    app.run(debug=True)