from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

# Flask uygulamasını başlat
app = Flask(__name__)
CORS(app)  # Tüm kaynaklardan gelen isteklere izin ver

# Kod çalıştırma endpoint'i
@app.route('/run', methods=['POST'])
def run_code():
    # JSON formatında gelen kodu al
    code = request.json.get("code", "")
    
    try:
        # Kullanıcının kodunu çalıştır
        result = subprocess.run(
            ["python3", "-c", code],  # python3 komutu ile çalıştırıyoruz
            capture_output=True,      # Çıktıyı yakalıyoruz
            text=True,                # Çıktıyı metin olarak işle
            timeout=5                 # Maksimum çalışma süresi (5 saniye)
        )
        # Kod çalıştırıldıktan sonra stdout ve stderr'i al
        output = result.stdout
        error = result.stderr
    except subprocess.TimeoutExpired:
        # Kod belirlenen sürede tamamlanmazsa hata döndür
        return jsonify({"error": "Kodun çalıştırılma süresi aşıldı."})
    
    # Çıktıyı JSON formatında döndür
    return jsonify({"output": output, "error": error})

# Ana sayfa yönlendirmesi
@app.route('/')
def home():
    return "Python Kod Çalıştırıcı API'ye Hoş Geldiniz. Kod çalıştırmak için /run endpoint'ini kullanın."

# Uygulamayı başlat
if __name__ == '__main__':
    app.run(debug=True)
