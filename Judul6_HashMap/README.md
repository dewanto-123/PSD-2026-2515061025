# Program Pencarian Arti Menggunakan HashMap Separate Chaining

# Deskripsi Singkat
Program ini merupakan aplikasi kamus digital sederhana yang memanfaatkan struktur data HashMap untuk menyimpan dan menemukan arti kata dengan cepat. Dalam sistem ini, setiap kata berperan sebagai key, sedangkan arti atau terjemahannya disimpan sebagai value. Penggunaan HashMap memungkinkan proses pencarian data dilakukan secara efisien tanpa harus menelusuri seluruh data yang tersimpan. Untuk mengatasi kemungkinan terjadinya collision (dua atau lebih key menghasilkan indeks hash yang sama), program menerapkan metode Separate Chaining, yaitu menyimpan beberapa data yang memiliki indeks sama dalam satu bucket. Dengan pendekatan tersebut, proses penyimpanan maupun pencarian data tetap dapat berjalan secara optimal meskipun terjadi tabrakan hash.

# Source Code
<img width="347" height="92" alt="Screenshot 2026-06-08 212650" src="https://github.com/user-attachments/assets/c012466d-3235-41cf-a20a-e3655f8bfcdc" />

Baris 1–5 dibuat class Node yang berfungsi untuk menyimpan satu data dalam HashMap. Baris 2 merupakan constructor yang menerima key dan value. Baris 3 menyimpan kata sebagai key, baris 4 menyimpan arti kata sebagai value, dan baris 5 membuat next bernilai None sebagai penunjuk ke node berikutnya jika terjadi collision.

<img width="366" height="76" alt="Screenshot 2026-06-08 212739" src="https://github.com/user-attachments/assets/872385dc-d393-4a24-b6fc-bcf3d24f5b3d" />
Baris 8–11 dibuat class HashMapSeparateChaining sebagai struktur utama HashMap. Baris 9 adalah constructor dengan ukuran awal 10. Baris 10 menyimpan ukuran HashMap ke variabel SIZE, sedangkan baris 11 membuat array table yang seluruh isinya masih kosong atau None.

<img width="400" height="96" alt="Screenshot 2026-06-08 212834" src="https://github.com/user-attachments/assets/22db863c-6827-4226-912a-869310da97e7" />

Baris 13–17 dibuat fungsi hash_function() untuk menentukan indeks bucket. Baris 14 membuat variabel total bernilai 0. Baris 15–16 menjumlahkan nilai ASCII dari setiap karakter pada key. Baris 17 mengembalikan hasil modulo antara total nilai ASCII dengan ukuran HashMap agar indeks tetap berada dalam batas tabel.

<img width="468" height="247" alt="Screenshot 2026-06-08 212959" src="https://github.com/user-attachments/assets/eed96857-95cc-419f-9faa-71538af3b8c2" />

Baris 19–31 dibuat fungsi insert() untuk menambahkan data kata dan artinya ke dalam HashMap. Baris 20 menentukan indeks penyimpanan menggunakan fungsi hash. Baris 21 mengambil isi bucket pada indeks tersebut. Baris 23–27 mengecek apakah key sudah ada; jika sudah ada, value akan diperbarui. Baris 29 membuat node baru, baris 30 menghubungkan node baru dengan node lama pada bucket yang sama, dan baris 31 menyimpan node baru sebagai data pertama pada bucket.

<img width="436" height="191" alt="Screenshot 2026-06-08 213019" src="https://github.com/user-attachments/assets/10533bd4-af69-434b-8d06-4ea84ab5c390" />

Baris 33–42 dibuat fungsi search() untuk mencari data berdasarkan key. Baris 34 menentukan indeks dari key yang dicari. Baris 35 mengambil node pertama pada bucket tersebut. Baris 37–40 melakukan penelusuran linked list. Jika key ditemukan, baris 39 mengembalikan node tersebut. Jika tidak ditemukan sampai akhir, baris 42 mengembalikan None.

<img width="507" height="322" alt="Screenshot 2026-06-08 213042" src="https://github.com/user-attachments/assets/0d3a0244-53e0-4928-9a5d-3a0075a63bea" />

Baris 44–60 dibuat fungsi remove_key() untuk menghapus data dari HashMap. Baris 45 menentukan indeks key yang akan dihapus. Baris 46 mengambil node pertama pada bucket, dan baris 47 menyiapkan variabel prev. Baris 49–58 menelusuri linked list untuk mencari key. Jika data ditemukan, baris 51–54 mengatur ulang hubungan node agar data tersebut terhapus. Baris 55 mengembalikan True, sedangkan baris 60 mengembalikan False jika key tidak ditemukan.

<img width="613" height="207" alt="Screenshot 2026-06-08 213057" src="https://github.com/user-attachments/assets/79d6fdf7-df34-4b83-bc4e-f3f36fc3918b" />

Baris 62–72 dibuat fungsi display() untuk menampilkan isi HashMap. Baris 63 mencetak judul tampilan. Baris 64–66 melakukan perulangan setiap bucket. Baris 68–70 mencetak seluruh data dalam bucket menggunakan linked list. Baris 72 mencetak NONE sebagai penanda akhir atau bucket kosong.

<img width="748" height="192" alt="Screenshot 2026-06-08 213118" src="https://github.com/user-attachments/assets/6cb5cf79-befd-47ff-90ba-691e8c31eb0c" />

Baris 75–84 dibuat fungsi main() sebagai program utama. Baris 76 membuat objek HashMap bernama kamus. Baris 78–82 memasukkan beberapa data kata dan arti ke dalam HashMap menggunakan fungsi insert(). Baris 84 memanggil fungsi display() untuk menampilkan seluruh isi HashMap.

<img width="631" height="206" alt="Screenshot 2026-06-08 213134" src="https://github.com/user-attachments/assets/6fbcf091-33cd-475a-8129-95fbf0d8d5d8" />

Baris 86–96 berisi proses pencarian dan penghapusan data. Baris 86 menentukan kata yang dicari, yaitu "hashmap". Baris 87 mencari kata tersebut menggunakan fungsi search(). Baris 89–92 menampilkan hasil pencarian, apakah kata ditemukan atau tidak. Baris 94 menghapus kata "array", baris 95 menampilkan keterangan setelah penghapusan, dan baris 96 menampilkan kembali isi HashMap.

<img width="288" height="45" alt="Screenshot 2026-06-08 213145" src="https://github.com/user-attachments/assets/feb2b8e6-b7f1-4bb4-8007-883cc84bf0af" />

Baris 99–100 digunakan untuk menjalankan program. Baris 99 memastikan file sedang dijalankan secara langsung, lalu baris 100 memanggil fungsi main() agar seluruh program dieksekusi.

# Output Program
<img width="675" height="480" alt="Screenshot 2026-06-08 214611" src="https://github.com/user-attachments/assets/2d46dd84-f878-4ed9-a219-a86197a16e61" />

Program pertama-tama menampilkan seluruh isi Hash Table Kamus Digital yang sudah berisi beberapa data kata beserta artinya. Setiap data ditampilkan berdasarkan indeks bucket hasil dari fungsi hash. Pada output terlihat beberapa bucket berisi data, sedangkan bucket yang kosong ditampilkan dengan tulisan NONE.

Selanjutnya program melakukan pencarian kata "hashmap". Karena kata tersebut tersedia di dalam HashMap, program berhasil menemukan datanya dan menampilkan arti dari kata tersebut, yaitu "struktur data yang menyimpan data dalam bentuk key-value".

Setelah itu, program menjalankan proses penghapusan terhadap kata "array". Setelah data dihapus, isi Hash Table ditampilkan kembali. Pada tampilan kedua, kata "array" sudah tidak muncul lagi di bucket sebelumnya. Hal ini menunjukkan bahwa fungsi remove_key() berhasil menghapus data dari HashMap.

# Link YouTube
