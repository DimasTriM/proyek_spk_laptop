# Proyek SPK Pemilihan Laptop (Metode WP)

## 🖼️ Pratinjau Tampilan UI

### Tampilan Utama (Peringkat Dinamis)
![Screenshot Main](docs/images/screenshot-main.png)

### Rincian Perhitungan (Modal)
![Screenshot Rincian](docs/images/screenshot-rincian.png)

---

## 📋 Deskripsi Proyek

Aplikasi web **Sistem Pendukung Keputusan (SPK)** untuk merekomendasikan laptop terbaik bagi mahasiswa informatika. Aplikasi ini dibangun menggunakan:

• **Backend:** Python (Flask)  
• **Frontend:** JavaScript (Fetch API)  
• **Containerization:** Docker  

Metode SPK yang digunakan adalah **Weighted Product (WP)**.

---

## ✨ Fitur Utama

• **Peringkat Dinamis:** Pengguna dapat mengatur bobot (prioritas) untuk setiap kriteria secara interaktif menggunakan slider.

• **Perhitungan Transparan:** Tombol "Rincian" di setiap baris hasil menampilkan pop-up modal dengan rincian perhitungan (Nilai ^ Bobot) untuk setiap kriteria.

• **Frontend Responsif:** Tampilan modern dan responsif dibangun menggunakan Tailwind CSS, nyaman dibuka di desktop maupun mobile.

• **Backend API (Flask):** Backend Flask menyediakan API yang aman untuk perhitungan.

• **Database SQLite:** Data laptop disimpan dalam database SQLite (`laptops.db`) yang dibuat secara otomatis.

• **Otentikasi API Key:** Endpoint API `/api/calculate` dilindungi oleh API Key statis untuk mencegah penyalahgunaan.

• **Containerisasi Docker:** Seluruh aplikasi (Backend, Database setup, Frontend) dibungkus dalam satu image Docker yang siap dijalankan di mana saja dengan satu perintah.

---

## 💻 Tumpukan Teknologi (Tech Stack)

• **Backend:** Python 3, Flask, Gunicorn  
• **Database:** SQLite3  
• **Frontend:** HTML, JavaScript (Fetch API), Tailwind CSS  
• **DevOps:** Docker, Docker Compose  

---

## 🚀 Cara Menjalankan Proyek

Ada dua cara untuk menjalankan proyek ini. **Metode Docker** adalah yang paling direkomendasikan.

---

### Metode 1: Docker (Direkomendasikan) 🐳

Metode ini akan membangun dan menjalankan aplikasi di dalam container yang terisolasi. Ini adalah cara "produksi".

**Langkah-langkah:**

1. Pastikan Docker Desktop sudah ter-install dan sedang berjalan.

2. Buka terminal (CMD, PowerShell, atau Bash) sebagai Administrator.

3. Pindah (`cd`) ke folder proyek ini.

4. **Build Image Docker:**
   ```bash
   docker build -t spk-laptop-app .
   ```
   
   *Jika ada cache lama, gunakan:*
   ```bash
   docker build --no-cache -t spk-laptop-app .
   ```

5. **Run Container:**
   ```bash
   docker run -p 5000:5000 spk-laptop-app
   ```

6. Buka browser dan kunjungi: `http://localhost:5000`

---

### Metode 2: Manual Lokal (Development/Debug) 🛠️

Metode ini menjalankan server secara langsung di komputermu menggunakan Python venv.

**Langkah-langkah:**

1. **Buat & Aktifkan Virtual Environment:**

   ```bash
   # Buat venv
   python -m venv venv
   
   # Aktifkan venv (Windows)
   .\venv\Scripts\activate
   
   # Aktifkan venv (Linux/Mac)
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Buat Database (Wajib, 1x saja):**
   
   Script ini akan membuat file `laptops.db` dan mengisinya dengan data.
   ```bash
   python database.py
   ```

4. **Jalankan Server Flask:**
   ```bash
   python app.py
   ```

5. Buka browser dan kunjungi: `http://localhost:5000`

---

## 📝 Lisensi

MIT License

---

## 👨‍💻 Kontributor

Dibuat dengan ❤️ untuk tugas SPK - Mahasiswa Informatika

---

## 📞 Kontak & Dukungan

Jika ada pertanyaan atau masalah, silakan buka **Issue** di repository ini.
