import sqlite3
from flask import Flask, render_template, request, jsonify

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Ini adalah Kunci API rahasia kita.
API_KEY = "RAHASIA-12345-BUATAN-SAYA"

# Fungsi untuk koneksi ke database
def get_db_connection():
    conn = sqlite3.connect('laptops.db')
    conn.row_factory = sqlite3.Row # Mengubah hasil query menjadi dictionary
    return conn

# Rute 1: Menyajikan halaman web (Frontend)
@app.route('/')
def index():
    return render_template('index.html')

# Rute 2: API untuk perhitungan (Ini yang akan dipanggil oleh JavaScript)
@app.route('/api/calculate', methods=['POST'])
def calculate_spk():
    
    # 1. Autentikasi API Key
    request_api_key = request.headers.get('X-API-Key')
    if request_api_key != API_KEY:
        return jsonify({"error": "Unauthorized: API Key salah atau tidak ada"}), 401

    # 2. Mengambil data bobot dari request yang dikirim JavaScript
    data = request.json
    bobot = {
        'harga': float(data.get('bobot_harga', 0)),
        'cpu':   float(data.get('bobot_cpu', 0)),
        'ram':   float(data.get('bobot_ram', 0)),
        'ssd':   float(data.get('bobot_ssd', 0)),
        'baterai': float(data.get('bobot_baterai', 0)),
        'bobot': float(data.get('bobot_laptop', 0))
    }

    # 3. Mengambil semua data laptop dari database
    conn = get_db_connection()
    laptops = conn.execute("SELECT * FROM laptops").fetchall()
    
    # 4. Proses Perhitungan WP (Metode WP) - INI YANG DIPERBARUI
    hasil_skor = []
    for laptop in laptops:
        # Hitung setiap komponen pangkat SATU PER SATU
        c1 = (laptop['harga'] ** -bobot['harga'])
        c2 = (laptop['cpu_score'] ** bobot['cpu'])
        c3 = (laptop['ram'] ** bobot['ram'])
        c4 = (laptop['ssd'] ** bobot['ssd'])
        c5 = (laptop['baterai'] ** bobot['baterai'])
        c6 = (laptop['bobot_laptop'] ** -bobot['bobot'])
        
        # Hitung Skor Vektor S (total perkalian)
        skor_s = c1 * c2 * c3 * c4 * c5 * c6
        
        # Siapkan data rincian UNTUK DIKIRIM KE MODAL (POP-UP)
        rincian = {
            'c1': {'nama': 'Harga', 'nilai': laptop['harga'], 'bobot': -bobot['harga'], 'hasil': c1},
            'c2': {'nama': 'Skor CPU', 'nilai': laptop['cpu_score'], 'bobot': bobot['cpu'], 'hasil': c2},
            'c3': {'nama': 'RAM', 'nilai': laptop['ram'], 'bobot': bobot['ram'], 'hasil': c3},
            'c4': {'nama': 'SSD', 'nilai': laptop['ssd'], 'bobot': bobot['ssd'], 'hasil': c4},
            'c5': {'nama': 'Baterai', 'nilai': laptop['baterai'], 'bobot': bobot['baterai'], 'hasil': c5},
            'c6': {'nama': 'Bobot Laptop', 'nilai': laptop['bobot_laptop'], 'bobot': -bobot['bobot'], 'hasil': c6}
        }
        
        hasil_skor.append({
            "nama": laptop['nama_laptop'],
            "skor": skor_s,
            "rincian": rincian  # <-- Kita kirim rinciannya juga!
        })

    # 5. Mengurutkan hasil dari skor tertinggi
    hasil_terurut = sorted(hasil_skor, key=lambda x: x['skor'], reverse=True)

    # 6. Menambahkan Peringkat
    hasil_akhir_dengan_peringkat = []
    for i, item in enumerate(hasil_terurut):
        item['peringkat'] = i + 1
        hasil_akhir_dengan_peringkat.append(item)

    conn.close()

    # 7. Mengirimkan hasil akhir (lengkap dengan rincian)
    return jsonify(hasil_akhir_dengan_peringkat)

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)