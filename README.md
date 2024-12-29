E-Commerce API
🚀 E-Commerce API adalah sebuah RESTful API yang dirancang untuk mendukung platform e-commerce dengan fitur-fitur utama seperti pengelolaan produk, kategori produk, serta keranjang belanja. Selain itu, API ini juga dilengkapi dengan integrasi layanan RajaOngkir untuk mempermudah pengguna dalam melakukan pengecekan ongkir berdasarkan kota, provinsi, dan berbagai perusahaan jasa pengiriman.

✨ Fitur Utama
Manajemen Produk:
CRUD (Create, Read, Update, Delete) untuk produk.
Setiap produk memiliki detail seperti nama, deskripsi, harga, dan kategori.
Kategori Produk:
CRUD untuk kategori produk untuk mempermudah pengelompokan barang.
Keranjang Belanja (Cart):
Tambahkan produk ke keranjang belanja.
Hitung total belanja pengguna.
Perbarui atau hapus produk dari keranjang.
Integrasi API RajaOngkir:
Pengecekan daftar kota dan provinsi di Indonesia.
Perhitungan ongkos kirim dari berbagai jasa pengiriman.
🛠️ Teknologi yang Digunakan
Backend Framework: Django/Flask/FastAPI (sesuaikan dengan yang Anda gunakan).
Database: PostgreSQL/MySQL/SQLite.
Integrasi Eksternal: API RajaOngkir untuk informasi pengiriman.
Authentication: JWT (Json Web Token) untuk keamanan pengguna.
📌 Cara Menggunakan
Clone repository ini ke dalam perangkat Anda.
Install dependencies menggunakan pip install -r requirements.txt.
Konfigurasikan .env file dengan API Key RajaOngkir dan database Anda.
Jalankan server dengan perintah:
bash
Salin kode
python manage.py runserver
Akses dokumentasi API pada endpoint /docs atau /swagger.
🔗 Integrasi RajaOngkir
Pastikan Anda telah mendaftarkan akun dan mendapatkan API Key RajaOngkir. Informasi lebih lanjut tersedia di RajaOngkir.

📋 Dokumentasi Endpoint
Produk

GET /products – Melihat semua produk.
POST /products – Menambahkan produk baru.
PUT /products/{id} – Mengubah data produk.
DELETE /products/{id} – Menghapus produk.
Kategori Produk

GET /categories – Melihat semua kategori.
POST /categories – Menambahkan kategori baru.
Keranjang Belanja

POST /cart – Menambahkan produk ke keranjang.
GET /cart – Melihat isi keranjang.
DELETE /cart/{id} – Menghapus produk dari keranjang.
RajaOngkir

GET /shipping/provinces – Melihat daftar provinsi.
GET /shipping/cities – Melihat daftar kota berdasarkan provinsi.
POST /shipping/cost – Menghitung ongkos kirim.
🏗️ Pengembangan
Proyek ini masih dalam tahap pengembangan dan terbuka untuk kontribusi. Jika Anda memiliki ide, saran, atau menemukan bug, silakan buat Issue atau ajukan Pull Request.

📧 Kontak
Jika Anda memiliki pertanyaan lebih lanjut, jangan ragu untuk menghubungi saya melalui email.
