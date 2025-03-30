from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = {
    "message": "Hello, World!",
    "status": "success"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify(data), 200

@app.route("/echo", methods=["POST"])
def echo():
    if not request.is_json:
        return jsonify({"error": "Invalid request, JSON expected"}), 400
    
    req_data = request.get_json()
    return jsonify({"you_sent": req_data}), 200

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "API is running"}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
