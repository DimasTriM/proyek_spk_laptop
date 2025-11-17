Proyek SPK Pemilihan Laptop (Metode WP)

Pratinjau tampilan UI

![](docs/images/screenshot-main.png)

Pratinjau Rincian

![](docs/images/screenshot-rincian.png)


Aplikasi web Sistem Pendukung Keputusan (SPK) untuk merekomendasikan laptop terbaik bagi mahasiswa informatika. Aplikasi ini dibangun menggunakan Python (Flask) sebagai backend, JavaScript (Fetch API) sebagai frontend, dan di-container-isasi menggunakan Docker.

Metode SPK yang digunakan adalah Weighted Product (WP).

📸 Tangkapan Layar (Portofolio)

Tampilan antarmuka utama yang modern dan panel rincian perhitungan manual yang transparan.

Tampilan Utama (Peringkat Dinamis)

Rincian Perhitungan (Modal)

✨ Fitur Utama

Peringkat Dinamis: Pengguna dapat mengatur bobot (prioritas) untuk setiap kriteria secara interaktif menggunakan slider.

Perhitungan Transparan: Tombol "Rincian" di setiap baris hasil menampilkan pop-up modal dengan rincian perhitungan (Nilai ^ Bobot) untuk setiap kriteria.

Frontend Responsif: Tampilan modern dan responsif dibangun menggunakan Tailwind CSS, nyaman dibuka di desktop maupun mobile.

Backend API (Flask): Backend Flask menyediakan API yang aman untuk perhitungan.

Database SQLite: Data laptop disimpan dalam database SQLite (laptops.db) yang dibuat secara otomatis.

Otentikasi API Key: Endpoint API /api/calculate dilindungi oleh API Key statis untuk mencegah penyalahgunaan.

Containerisasi Docker: Seluruh aplikasi (Backend, Database setup, Frontend) dibungkus dalam satu image Docker yang siap dijalankan di mana saja dengan satu perintah.

💻 Tumpukan Teknologi (Tech Stack)

Backend: Python 3, Flask, Gunicorn

Database: SQLite3

Frontend: HTML, JavaScript (Fetch API), Tailwind CSS

DevOps: Docker, Docker Compose (implied)

🚀 Cara Menjalankan Proyek

Ada dua cara untuk menjalankan proyek ini. Cara Docker adalah yang paling direkomendasikan.

Metode 1: Docker (Cara yang Direkomendasikan)

Metode ini akan membangun dan menjalankan aplikasi di dalam container yang terisolasi. Ini adalah cara "produksi".

Pastikan Docker Desktop sudah ter-install dan sedang berjalan.

Buka terminal (CMD, PowerShell, atau Bash) sebagai Administrator.

Pindah (cd) ke folder proyek ini.

Build Image Docker:

docker build -t spk-laptop-app .

(Jika ada cache lama, gunakan: docker build --no-cache -t spk-laptop-app .)

Run Container:

docker run -p 5000:5000 spk-laptop-app

Buka browser dan kunjungi: http://localhost:5000

Metode 2: Manual Lokal (Untuk Development/Debug)

Metode ini menjalankan server secara langsung di komputermu menggunakan Python venv.

Buat & Aktifkan Virtual Environment:

# Buat venv

python -m venv venv

# Aktifkan venv (Windows)

.\venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Buat Database (Wajib, 1x saja):
Script ini akan membuat file laptops.db dan mengisinya dengan data.

python database.py

Jalankan Server Flask:

python app.py

Buka browser dan kunjungi: http://localhost:5000
