from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get("code", "")
    
    try:
        result = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout
        error = result.stderr
    except subprocess.TimeoutExpired:
        return jsonify({"error": "ERR_TIMEOUT."})
    
    return jsonify({"output": output, "error": error})

@app.route('/')
def home():
    return "Working!"

if __name__ == '__main__':
    app.run(debug=True)
