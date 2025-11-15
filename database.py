import sqlite3
import csv
import os

DB_FILE = 'laptops.db'
CSV_FILE = 'SPK WP.xlsx - Dataset.csv' # Pastikan nama file ini sama

# 1. Hapus file database lama jika ada, agar datanya fresh
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"File database '{DB_FILE}' lama dihapus.")

# 2. Membuat koneksi ke database baru
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# 3. Membuat tabel 'laptops'
cursor.execute('''
CREATE TABLE IF NOT EXISTS laptops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_laptop TEXT NOT NULL,
    harga INTEGER,
    cpu_score INTEGER,
    ram INTEGER,
    ssd INTEGER,
    baterai REAL,
    bobot_laptop REAL
)
''')
print("Tabel 'laptops' berhasil dibuat.")

# 4. Membaca file CSV dan memasukkan data
laptop_data_from_csv = []
try:
    with open(CSV_FILE, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Lewati baris header (No, Nama Laptop, Harga, ...)
        header = next(csv_reader) 
        
        # Baca sisa baris data
        for row in csv_reader:
            # Pastikan baris tidak kosong
            if not row or not row[1]:
                continue
                
            # Ambil data dari kolom yang sesuai
            # [1] Nama, [2] Harga, [3] CPU, [4] RAM, [5] SSD, [6] Baterai, [7] Bobot
            nama = row[1]
            harga = int(float(row[2].replace('.', ''))) # Bersihkan format angka jika perlu
            cpu = int(row[3])
            ram = int(row[4])
            ssd = int(row[5])
            baterai = float(row[6])
            bobot = float(row[7])
            
            laptop_data_from_csv.append(
                (nama, harga, cpu, ram, ssd, baterai, bobot)
            )

except FileNotFoundError:
    print(f"ERROR: File '{CSV_FILE}' tidak ditemukan.")
    print("Pastikan file CSV ada di folder yang sama dengan database.py")
    conn.close()
    exit()
except Exception as e:
    print(f"Terjadi error saat membaca CSV: {e}")
    conn.close()
    exit()

# 5. Masukkan semua data dari CSV ke database
cursor.executemany('''
INSERT INTO laptops (nama_laptop, harga, cpu_score, ram, ssd, baterai, bobot_laptop)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', laptop_data_from_csv)

conn.commit()
conn.close()

print(f"Berhasil! {len(laptop_data_from_csv)} data laptop telah dimasukkan ke '{DB_FILE}' dari '{CSV_FILE}'.")