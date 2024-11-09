import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba, uygulama çalışıyor!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


'''

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
        return jsonify({"error": "Kodun çalıştırılma süresi aşıldı."})
    
    return jsonify({"output": output, "error": error})

@app.route('/')
def home():
    return "Python Kod Çalıştırıcı API'ye Hoş Geldiniz. Kod çalıştırmak için /run endpoint'ini kullanın."

if __name__ == '__main__':
    app.run(debug=True)


'''