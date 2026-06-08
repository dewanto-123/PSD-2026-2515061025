# Program Pencarian Arti Menggunakan HashMap Separate Chaining

# Deskripsi Singkat
Program ini merupakan aplikasi kamus digital sederhana yang memanfaatkan struktur data HashMap untuk menyimpan dan menemukan arti kata dengan cepat. Dalam sistem ini, setiap kata berperan sebagai key, sedangkan arti atau terjemahannya disimpan sebagai value. Penggunaan HashMap memungkinkan proses pencarian data dilakukan secara efisien tanpa harus menelusuri seluruh data yang tersimpan. Untuk mengatasi kemungkinan terjadinya collision (dua atau lebih key menghasilkan indeks hash yang sama), program menerapkan metode Separate Chaining, yaitu menyimpan beberapa data yang memiliki indeks sama dalam satu bucket. Dengan pendekatan tersebut, proses penyimpanan maupun pencarian data tetap dapat berjalan secara optimal meskipun terjadi tabrakan hash.

# Source Code

