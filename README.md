# Deskripsi Proyek

Rizqullah Aryaputra Piliang & Ikhwan M. Faried

Proyek ini merupakan implementasi dari sistem komunikasi terdistribusi yang melibatkan beberapa script untuk mengatur interaksi antara klien, server, dan koordinator. Sistem ini dirancang untuk mendukung komunikasi multi-threaded, logging, dan koordinasi antar server atau node dalam lingkungan terdistribusi.

## Struktur File

Berikut adalah deskripsi dari file-file yang ada dalam proyek ini:

### 1. `client.py`

Script ini berfungsi sebagai klien dalam sistem komunikasi client-server. Klien bertugas untuk mengirimkan permintaan ke server terdistribusi, menerima respons, serta mengukur waktu respons dan latensi.

### 2. `coor_with_logging.py`

Script ini merupakan versi dari koordinator yang dilengkapi dengan logging. Logging digunakan untuk melacak aktivitas atau interaksi dalam sistem terdistribusi, termasuk mencatat waktu pengiriman pesan, penerimaan pesan, dan event penting lainnya.

### 3. `coordinator.log`

Ini adalah file log yang dihasilkan oleh `coor_with_logging.py`. File ini berisi rekaman aktivitas atau interaksi antara klien dan server dalam sistem. Analisis terhadap file log ini dapat membantu dalam proses debugging dan pemantauan performa sistem.

### 4. `coordinator.py`

Script ini berfungsi sebagai pusat koordinasi dalam sistem terdistribusi. `coordinator.py` bertugas mengatur komunikasi antara node, klien, dan server, serta mengelola alur data yang mengalir dalam sistem.

### 5. `distributed_server.py`

Script ini merupakan server yang beroperasi dalam lingkungan terdistribusi. Server ini kemungkinan besar menerima permintaan dari beberapa klien dan berkomunikasi dengan server lain atau koordinator untuk menyelesaikan tugas tertentu.

### 6. `multi_thread.py`

Script ini mendemonstrasikan implementasi server atau klien yang mendukung eksekusi multi-threading. Multi-threading memungkinkan beberapa proses dijalankan secara bersamaan, sehingga meningkatkan efisiensi dan kecepatan dalam menangani banyak permintaan.

### 7. `single_thread.py`

Berbeda dengan `multi_thread.py`, script ini mengimplementasikan eksekusi dengan menggunakan satu thread saja. Ini bisa digunakan untuk membandingkan performa antara eksekusi multi-threading dan single-threading dalam sistem terdistribusi.

### 8. `test_client.py`

Script ini mungkin digunakan untuk melakukan pengujian pada klien yang berinteraksi dengan server. Pengujian ini bisa mencakup pengiriman permintaan, menerima respons, serta pengukuran waktu eksekusi atau latensi.

### 9. `clien_tes.py`

Ini tampaknya merupakan versi lain dari script klien yang digunakan untuk pengujian. Nama file ini mungkin salah ketik dari `client_test.py`, namun memiliki fungsi yang serupa untuk melakukan pengujian pada klien.

## Cara Menggunakan

1. Jalankan `coordinator.py` untuk memulai server koordinator yang mengatur lalu lintas data antara klien dan server.
2. Jalankan `distributed_server.py` untuk memulai server terdistribusi.
3. Gunakan `client.py` atau `test_client.py` untuk mengirim permintaan ke server.
4. Monitor file log `coordinator.log` untuk melihat aktivitas sistem secara real-time.

## Fitur Utama

- **Multi-threading:** Dukungan untuk eksekusi proses secara paralel melalui thread.
- **Logging:** Pencatatan aktivitas sistem yang dapat digunakan untuk analisis dan debugging.
- **Koordinasi Terdistribusi:** Pengaturan alur komunikasi antara beberapa server dan klien dengan koordinasi yang terpusat.

## Catatan

- Pastikan semua dependencies yang diperlukan sudah terpasang sebelum menjalankan script. Jika ada module atau package yang hilang, instal melalui `pip`.
- Analisis terhadap file log sangat disarankan untuk memahami performa sistem dan menemukan potensi masalah.
