from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = {
    "message": "Hello, World!",
    "status": "success"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify(data)

@app.route("/echo", methods=["POST"])
def echo():
    req_data = request.get_json()
    return jsonify({"you_sent": req_data})

if __name__ == "__main__":
    app.run(debug=True)
