# Pertemuan 07 - Fungsi Python

- Nama: Gugun Ramdani  
- NIM: 2225250061  
- Kelas: 3A  
- Program Studi: Pendidikan Matematika  
- Mata Kuliah: Algoritma dan Pemrograman

## 1. Tujuan
Mempelajari fungsi, parameter, argumen, return value, dan scope
dalam Python. Program dibuat secara modular agar lebih mudah
dibaca, diuji, diperbaiki, dan digunakan kembali.

## 2. Struktur Folder
```text
1. Pertemuan_07_fungsi_2225250061
2. latihan/
- 01_salam.py
- 02_luas_persegi_panjang.py
- 03_jumlah_n.py
- 04_statistik_sederhana.py
- 05_scope.py
3. praktik/
- utilitas_matematika.py
4. .gitignore
5. kuis formatif_pertemuan 07
6. README.md
```
## 3. Cara Menjalankan
Jalankan setiap latihan melalui terminal VS Code.
Contoh:
```bash
python latihan/01_salam.py
python latihan/02_luas_persegi_panjang.py
python latihan/03_jumlah_n.py
python latihan/04_statistik_sederhana.py
python latihan/05_scope.py
python praktik/utilitas_matematika.py
```
## 4. Struktur Fungsi
- `salam(nama, kelas)`: menampilkan salam berdasarkan nama dan kelas.
- `luas_persegi_panjang(p, l)`: menghitung luas persegi panjang.
- `jumlah_n(n)`: menghitung jumlah bilangan 1 sampai n.
- `statistik(data)`: menentukan nilai minimum, maksimum, dan rata-rata.
- `demo(x)`: menunjukkan perbedaan local scope dan global scope.
- `luas_segitiga(a, t)`: menghitung luas segitiga.
- `faktorial(n)`: menghitung faktorial menggunakan perulangan.
- `tampilkan_menu()`: menampilkan pilihan operasi matematika.

## 5. Hasil Pengujian
| No. | Fungsi | Input | Hasil |
|---|---|---|---|
| 1 | luas_persegi_panjang | 8, 5 | 40 |
| 2 | luas_segitiga | 10, 6 | 30.0 |
| 3 | jumlah_n | 10 | 55 |
| 4 | faktorial | 5 | 120 |
| 5 | faktorial | 0 | 1 |

Hasil aktual diperiksa melalui terminal VS Code.

## 6. Refleksi
Penggunaan fungsi membuat program lebih terstruktur karena
setiap fungsi mempunyai tanggung jawab tertentu. Parameter
memungkinkan fungsi menerima data yang berbeda, sedangkan
return memungkinkan hasil perhitungan digunakan kembali.
Local scope juga membantu mencegah variabel internal fungsi
diakses secara keliru dari luar fungsi.
