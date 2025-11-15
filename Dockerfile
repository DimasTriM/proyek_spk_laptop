# 1. Mulai dari "kotak makan" Python 3.11 versi ringan
FROM python:3.11-slim

# 2. Membuat folder di dalam kotak untuk menaruh proyek kita
WORKDIR /app

# 3. Salin "daftar bumbu" (requirements.txt) dulu
COPY requirements.txt .

# 4. "Aduk bumbu" / Install semua library
# --no-cache-dir agar lebih hemat tempat
RUN pip install --no-cache-dir -r requirements.txt

# 5. Salin semua file proyek kita ke dalam kotak
COPY . .

# 6. "Masak" bahan mentah (CSV) menjadi database (laptops.db)
# Ini menjalankan script database.py di dalam container
RUN python database.py

# 7. Beri tahu Docker bahwa aplikasi kita akan berjalan di port 5000
EXPOSE 5000

# 8. Perintah untuk "menghidangkan" masakan saat kotak dibuka
# Ini adalah cara standar menjalankan Flask dengan Gunicorn
# "app:app" artinya: "cari file bernama app.py, dan di dalamnya jalankan object bernama app"
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]