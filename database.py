import sqlite3
import os
import sys

DB_FILE = 'laptops.db'

# --- DATA HARD-CODED (Versi 1) ---
# Kita masukkan datanya langsung di sini, jadi tidak perlu file CSV
laptop_data = [
    ('Acer Swift Go 14', 11500000, 17500, 16, 512, 10, 1.25),
    ('Lenovo Ideapad Slim 5i', 12999000, 18100, 16, 512, 9, 1.40),
    ('Asus Zenbook 14 OLED', 16499000, 20500, 16, 1024, 12, 1.30),
    ('Dell Inspiron 13', 10999000, 16900, 8, 512, 8, 1.28),
    ('HP Pavilion Plus 14', 13500000, 18500, 16, 512, 8, 1.35),
    ('MSI Modern 14', 9800000, 15500, 8, 512, 7, 1.40),
    ('Axioo Pongo 7', 15250000, 22500, 16, 512, 6, 1.70),
    ('Lenovo Yoga Slim 7 Pro', 18999000, 24000, 16, 1024, 11, 1.38),
    ('Macbook Air M2', 17500000, 19500, 8, 256, 15, 1.24),
    ('Acer Aspire 5', 8900000, 14800, 8, 512, 7, 1.50),
    ('Asus Vivobook Pro 14', 14800000, 21500, 16, 512, 9, 1.45),
    ('HP Envy x360', 16200000, 20100, 16, 512, 10, 1.33),
    ('Samsung Galaxy Book3', 13999000, 18300, 16, 512, 11, 1.17),
    ('Dell XPS 13', 22500000, 25500, 16, 1024, 12, 1.15),
    ('Lenovo ThinkPad E14', 14100000, 19800, 16, 512, 9, 1.55),
    ('Huawei Matebook D14', 10500000, 16200, 16, 512, 10, 1.39),
    ('Advan WorkPro', 7999000, 14500, 8, 256, 6, 1.30),
    ('Asus TUF Gaming F15', 15999000, 23500, 8, 512, 6, 2.20),
    ('Lenovo Legion 5', 19500000, 26000, 16, 512, 5, 2.40),
    ('Zyrex Sky 232', 6500000, 9500, 8, 256, 5, 1.35)
]
# -----------------------------------

# 1. Hapus file database lama jika ada
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"File database '{DB_FILE}' lama dihapus.")

# 2. Membuat koneksi ke database baru
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# 3. Membuat tabel 'laptops'
try:
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
    # PERBAIKAN PENTING: Commit (simpan) tabelnya SEKARANG JUGA!
    conn.commit() 
    print("Tabel 'laptops' berhasil dibuat.")

except Exception as e:
    print(f"ERROR saat CREATE TABLE: {e}")
    conn.close()
    sys.exit(1) # Keluar dengan status error

# 4. Memasukkan semua data laptop
try:
    cursor.executemany('''
    INSERT INTO laptops (nama_laptop, harga, cpu_score, ram, ssd, baterai, bobot_laptop)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', laptop_data)
    
    # PERBAIKAN PENTING: Commit (simpan) data yang baru dimasukkan
    conn.commit()
    conn.close()
    print(f"Berhasil! {len(laptop_data)} data laptop telah dimasukkan ke '{DB_FILE}'.")

except Exception as e:
    print(f"ERROR saat INSERT data: {e}")
    conn.close()
    sys.exit(1) # Keluar dengan status error