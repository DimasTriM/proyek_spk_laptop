Proyek SPK Pemilihan Laptop (Metode WP)

Ini adalah aplikasi web Sistem Pendukung Keputusan (SPK) untuk merekomendasikan laptop terbaik bagi mahasiswa informatika. Aplikasi ini dibangun menggunakan Python (Flask) sebagai backend dan JavaScript sebagai frontend.

Metode SPK yang digunakan adalah Weighted Product (WP).

✨ Fitur Utama

Peringkat Dinamis: Pengguna dapat mengatur bobot (prioritas) untuk setiap kriteria secara interaktif menggunakan slider.

Perhitungan Transparan: Tersedia tombol "Rincian" untuk melihat perhitungan manual (hasil pangkat) dari setiap laptop, persis seperti di Excel.

Frontend Responsif: Tampilan dibuat modern dan responsif menggunakan Tailwind CSS, sehingga nyaman dibuka di laptop maupun HP.

Backend API: Backend Flask menyediakan API yang aman untuk perhitungan.

Database: Data laptop disimpan dalam database SQLite, yang diisi secara otomatis dari file CSV.

Otentikasi API Key: Endpoint API dilindungi oleh API Key sederhana untuk mencegah penyalahgunaan.

💻 Tumpukan Teknologi (Tech Stack)

Backend: Python 3, Flask

Database: SQLite3

Frontend: HTML, JavaScript (Fetch API), Tailwind CSS

Dataset: Disimpan dan dibaca dari file .csv

🚀 Cara Menjalankan Proyek

Pastikan Anda memiliki Python 3.10+ ter-install di komputer Anda.

1. Clone Repositori

git clone [URL_REPO_GITHUB_ANDA]
cd proyek_spk_laptop


2. Buat dan Aktifkan Virtual Environment

# Buat venv
python -m venv venv

# Aktifkan venv (Windows)
.\venv\Scripts\activate

# Aktifkan venv (Mac/Linux)
source venv/bin/activate


3. Install Semua Kebutuhan (Dependencies)

# Pastikan file requirements.txt ada
pip install -r requirements.txt


4. Buat Database dari CSV
Jalankan script database.py (hanya perlu sekali) untuk membaca file .csv dan membuat file laptops.db.

python database.py


5. Jalankan Server Flask

python app.py


6. Buka Aplikasi
Buka browser Anda dan kunjungi alamat: http://127.0.0.1:5000

🔐 API Key

Aplikasi ini menggunakan API Key statis untuk mengamankan endpoint /api/calculate.

Key di Backend: Didefinisikan di app.py pada variabel API_KEY.

Key di Frontend: Didefinisikan di templates/index.html pada variabel MY_API_KEY.

Pastikan kedua nilai ini sama.

📂 Struktur Proyek

proyek_spk_laptop/
├── .gitignore          # Mengabaikan file yang tidak perlu di-push
├── app.py              # Backend server Flask
├── database.py         # Script untuk membuat DB dari CSV
├── laptops.db          # (Diabaikan oleh .gitignore) File database
├── requirements.txt    # Daftar dependensi Python
├── templates/
│   └── index.html      # Tampilan Frontend
├── venv/               # (Diabaikan oleh .gitignore) Folder environment
└── *.csv               # File data mentah
