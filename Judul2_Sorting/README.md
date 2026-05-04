# Program Pengurutan Jumlah Follower Akun Media Sosial Menggunakan Insertion Sort

# Deskripsi Singkat
Program ini merupakan program sederhana untuk mengelola dan mengurutkan data jumlah follower akun media sosial menggunakan algoritma Insertion Sort. Pengguna dapat memasukkan beberapa data akun berupa nama akun dan jumlah follower, kemudian program akan menampilkan data sebelum dan sesudah proses pengurutan. Proses pengurutan dilakukan dari jumlah follower yang paling sedikit hingga yang paling banyak, sehingga memudahkan pengguna dalam membandingkan popularitas akun. Algoritma Insertion Sort digunakan karena bekerja dengan cara menyisipkan setiap data ke posisi yang tepat pada bagian data yang sudah terurut, sehingga mudah dipahami dan cocok digunakan untuk jumlah data yang tidak terlalu besar.

# Source Code
<img width="718" height="190" alt="Screenshot 2026-05-04 191201" src="https://github.com/user-attachments/assets/463ddf1f-221e-4c36-bbf9-f0369aa356f3" />
Pada baris 1–8, baris 1 didefinisikan fungsi insertion_sort(arr, n) yang digunakan untuk mengurutkan data akun berdasarkan jumlah follower. Pada baris 2 dilakukan perulangan dari indeks 1 sampai indeks terakhir karena elemen pertama dianggap sudah berada pada posisi yang benar. Baris 3 menyimpan data akun yang sedang diproses ke dalam variabel temp_data, sehingga data tersebut tidak hilang saat terjadi pergeseran. Baris 4 membuat variabel j sebagai indeks untuk memeriksa elemen di sebelah kiri data yang sedang dibandingkan. Pada baris 5–7 dilakukan proses pergeseran data selama indeks j masih valid dan jumlah follower pada data sebelumnya lebih besar daripada jumlah follower pada temp_data. Jika kondisi itu terpenuhi, maka data yang lebih besar digeser ke kanan satu posisi. Baris 8 menempatkan temp_data pada posisi yang tepat setelah proses pergeseran selesai. Dengan cara ini, data akan tersusun dari jumlah follower yang paling kecil ke yang paling besar.

<img width="714" height="139" alt="Screenshot 2026-05-04 191222" src="https://github.com/user-attachments/assets/810531bc-e93b-4d10-a0ee-01a69257d8f7" />
Pada baris 10–15, baris 10 didefinisikan fungsi main() sebagai pusat jalannya program. Baris 11–15 digunakan untuk meminta input jumlah akun media sosial yang akan diurutkan. Input tersebut dikonversi menjadi bilangan bulat dengan int(), sehingga jika pengguna memasukkan selain angka maka program akan menampilkan pesan Input tidak valid! dan berhenti melalui perintah return. Bagian ini penting agar program tidak error ketika jumlah data yang dimasukkan salah.

<img width="752" height="400" alt="Screenshot 2026-05-04 191302" src="https://github.com/user-attachments/assets/a816bdf8-374c-4bad-b48e-9b1798f296b3" />
Pada baris 17–28, baris 17 membuat list kosong arr yang akan digunakan untuk menyimpan nama akun dan jumlah follower. Baris 18 menampilkan pesan agar pengguna memasukkan data akun. Baris 19–28 adalah perulangan untuk mengisi data sebanyak n kali. Baris 21 menampilkan nomor akun yang sedang diinput. Baris 21 meminta nama akun media sosial. Baris 22–28 digunakan untuk meminta jumlah follower, tetapi dibuat dalam perulangan while True agar input harus berupa angka. Jika pengguna memasukkan data selain angka, maka baris 27 akan menampilkan pesan kesalahan dan pengguna diminta mengulang kembali. Setelah data valid, baris 28 menyimpan data dalam bentuk list berisi nama akun dan jumlah follower

<img width="752" height="73" alt="7" src="https://github.com/user-attachments/assets/bddaf292-5519-4503-8051-806eac1da1ee" />
<img width="798" height="198" alt="Screenshot 2026-05-04 191601" src="https://github.com/user-attachments/assets/ae6246e2-3ada-4653-b527-d01890fe1536" />
Pada baris 30–38, baris 30 menampilkan data sebelum diurutkan agar pengguna dapat melihat kondisi awal data. Baris 31–32 melakukan perulangan untuk menampilkan setiap akun beserta jumlah follower-nya. Baris 34 memanggil fungsi insertion_sort(arr, n) untuk mengurutkan data berdasarkan jumlah follower dari yang paling sedikit ke yang paling banyak. Baris 36–38 menampilkan hasil akhir setelah proses pengurutan selesai. Di sini terlihat bahwa urutan data sudah berubah sesuai jumlah follower yang paling kecil sampai yang paling besar. Baris 40–41 digunakan agar fungsi main() hanya dijalankan ketika file Python ini dijalankan secara langsung.

# Output Program
<img width="414" height="461" alt="Screenshot 2026-05-04 220654" src="https://github.com/user-attachments/assets/a7dd8e94-9c47-4778-aaba-7b7f652ab71c" />
Hasil output tersebut menunjukkan bahwa sebelum proses pengurutan, data akun masih berada sesuai urutan input pengguna. Setelah fungsi insertion_sort() dijalankan, data berubah menjadi urutan yang lebih rapi berdasarkan jumlah follower dari yang paling sedikit ke yang paling banyak. Pada hasil akhir terlihat bahwa @dewaok dengan 800 follower berada di urutan pertama karena jumlahnya paling kecil, kemudian disusul @opmrf dengan 5000 follower, dan yang terakhir @jiplokasi dengan 6001 follower. Ini membuktikan bahwa program berhasil melakukan pengurutan menggunakan metode Insertion Sort sesuai tujuan.

# Link YouTube
https://youtu.be/kTNdMUoheLg

