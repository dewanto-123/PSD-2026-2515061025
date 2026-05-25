# Program Pendataan Mahasiswa Berdasarkan NIM

# Deskripsi Singkat
Program pendataan mahasiswa berdasarkan NIM yang menggunakan Binary Search Tree (BST) ini merupakan program yang digunakan untuk menyimpan, mengelola, dan mencari data mahasiswa secara terstruktur berdasarkan NIM sebagai key utama. Program ini memiliki beberapa fitur seperti menambahkan data mahasiswa, mencari data berdasarkan NIM, menampilkan seluruh data secara urut, mengubah data, menghapus data, serta menampilkan NIM terkecil dan terbesar. Dengan menggunakan metode BST ini, proses pencarian dan pengelolaan data menjadi jauh lebih cepat dan efisien karena data disusun secara otomatis berdasarkan urutan NIM.

# Source Code
<img width="802" height="886" alt="Screenshot 2026-05-25 224327" src="https://github.com/user-attachments/assets/81e68942-47ed-4183-bc62-aeefa1199313" />
<img width="786" height="826" alt="Screenshot 2026-05-25 224350" src="https://github.com/user-attachments/assets/a87112a9-b39d-4bbf-b35a-30592f37203f" />
<img width="884" height="852" alt="Screenshot 2026-05-25 224415" src="https://github.com/user-attachments/assets/440ca787-9110-4476-bbda-55af17f78c36" />
<img width="942" height="833" alt="Screenshot 2026-05-25 224438" src="https://github.com/user-attachments/assets/231dc1e4-2f03-4873-9461-1b762279299d" />
<img width="935" height="863" alt="Screenshot 2026-05-25 224454" src="https://github.com/user-attachments/assets/74e4f188-5c4d-42ea-8bb0-81c95d93943b" />
<img width="671" height="860" alt="Screenshot 2026-05-25 224510" src="https://github.com/user-attachments/assets/3f2b85f0-f351-47f2-ac25-970eb0089a0a" />
<img width="850" height="856" alt="Screenshot 2026-05-25 224526" src="https://github.com/user-attachments/assets/84fbf770-5962-4cf5-87dc-fbd3ebaf4c74" />
<img width="862" height="492" alt="Screenshot 2026-05-25 224540" src="https://github.com/user-attachments/assets/0e49e275-f0a4-4490-ba09-6d871a387335" />

Baris 1–6

Pada baris 1–6 dibuat class Mahasiswa yang digunakan untuk menyimpan data mahasiswa. Pada baris 2 dibuat constructor __init__() yang berfungsi untuk menerima data saat object dibuat. Pada baris 3–6 data seperti NIM, nama, jurusan, dan IPK disimpan ke dalam object menggunakan keyword self. Dengan adanya class ini, setiap mahasiswa dapat disimpan sebagai satu object yang memiliki atribut masing-masing.


Baris 8–12

Pada baris 8–12 dibuat class Node yang digunakan sebagai node atau simpul pada Binary Search Tree. Setiap node menyimpan satu data mahasiswa pada variabel self.mahasiswa. Selain itu, node juga memiliki pointer left dan right yang digunakan untuk menghubungkan node ke subtree kiri dan subtree kanan. Nilai awal kedua pointer tersebut adalah None, yang berarti node belum memiliki anak.


Baris 14–16

Pada baris 14–16 dibuat class BinarySearchTree sebagai struktur utama BST. Pada constructor __init__() dibuat variabel root dengan nilai awal None. Hal ini menandakan bahwa tree masih kosong dan belum memiliki node pertama.


Baris 18–23

Pada baris 18–23 dibuat fungsi tambah() yang digunakan untuk menambahkan data mahasiswa ke dalam BST. Pada baris 19 dilakukan pengecekan apakah root masih kosong. Jika kosong, maka data mahasiswa pertama akan dijadikan root pada BST. Jika root sudah ada, maka proses penambahan data akan dilanjutkan menggunakan fungsi recursive _tambah_recursive() agar posisi node sesuai aturan BST.


Baris 25–38

Pada baris 25–38 dibuat fungsi _tambah_recursive() yang digunakan untuk menentukan posisi node berdasarkan nilai NIM. Jika NIM mahasiswa lebih kecil dari node sekarang, maka data dimasukkan ke subtree kiri. Jika subtree kiri kosong, dibuat node baru. Jika masih ada node lain, maka fungsi dipanggil kembali secara recursive. Sebaliknya, jika NIM lebih besar maka data dimasukkan ke subtree kanan. Jika NIM sama dengan node yang sudah ada, maka program mengembalikan False karena BST tidak memperbolehkan data NIM duplikat.


Baris 41–42

Pada baris 41–42 dibuat fungsi cari() yang digunakan untuk mencari data mahasiswa berdasarkan NIM. Fungsi ini bekerja dengan memanggil fungsi recursive _cari_recursive() yang akan melakukan pencarian pada BST.


Baris 44–55

Pada baris 44–55 dibuat fungsi _cari_recursive() untuk melakukan proses pencarian data secara recursive. Jika node kosong, maka data tidak ditemukan. Jika NIM sama dengan node sekarang, maka data berhasil ditemukan. Jika NIM lebih kecil dari node saat ini, maka pencarian dilanjutkan ke subtree kiri. Jika lebih besar, maka pencarian dilanjutkan ke subtree kanan.


Baris 57–65

Pada baris 57–65 dibuat fungsi tampilkan_inorder() yang digunakan untuk menampilkan seluruh data mahasiswa secara urut berdasarkan NIM. Fungsi ini menggunakan traversal inorder. Jika BST kosong maka program menampilkan pesan bahwa belum ada data mahasiswa. Jika ada data, maka program akan menampilkan header tabel dan memanggil fungsi _inorder_recursive().


Baris 67–71

Pada baris 67–71 dibuat fungsi _inorder_recursive() yang digunakan untuk traversal inorder secara recursive. Traversal inorder bekerja dengan urutan kiri, root, lalu kanan. Karena BST menggunakan aturan nilai kecil di kiri dan nilai besar di kanan, maka traversal inorder akan menghasilkan data yang otomatis terurut berdasarkan NIM.


Baris 73–96

Pada baris 73–96 dibuat fungsi ubah() yang digunakan untuk mengubah data mahasiswa. Program terlebih dahulu mencari data mahasiswa berdasarkan NIM menggunakan fungsi cari(). Jika data tidak ditemukan maka program menampilkan pesan error. Jika data ditemukan, program akan menampilkan data lama kemudian meminta user memasukkan data baru berupa nama, jurusan, dan IPK. NIM tidak diubah karena NIM merupakan key utama pada BST.


Baris 98–104

Pada baris 98–104 dibuat fungsi hapus() yang digunakan untuk menghapus data mahasiswa berdasarkan NIM. Fungsi ini memanggil fungsi recursive _hapus_recursive() untuk melakukan proses penghapusan node. Setelah proses selesai, program akan menampilkan pesan apakah data berhasil dihapus atau tidak ditemukan.


Baris 106–132

Pada baris 106–132 dibuat fungsi _hapus_recursive() yang digunakan untuk menghapus node pada BST. Jika node kosong maka data tidak ditemukan. Jika NIM lebih kecil maka proses penghapusan dilakukan ke subtree kiri, sedangkan jika lebih besar dilakukan ke subtree kanan. Pada bagian ini juga terdapat tiga kondisi penghapusan node, yaitu node tanpa anak, node dengan satu anak, dan node dengan dua anak. Jika node memiliki dua anak, maka node akan diganti dengan node terkecil dari subtree kanan.


Baris 134–137

Pada baris 134–137 dibuat fungsi cari_min() yang digunakan untuk mencari NIM terkecil pada BST. Fungsi ini bekerja dengan memanggil _cari_min_node() untuk mencari node paling kiri pada BST karena node paling kiri selalu memiliki nilai terkecil.


Baris 139–142

Pada baris 139–142 dibuat fungsi _cari_min_node() untuk mencari node dengan nilai terkecil. Program akan terus bergerak ke subtree kiri sampai tidak ada lagi node di sebelah kiri. Node terakhir tersebut merupakan node dengan nilai terkecil.


Baris 144–151

Pada baris 144–151 dibuat fungsi cari_max() yang digunakan untuk mencari NIM terbesar pada BST. Program akan terus bergerak ke subtree kanan sampai mencapai node paling kanan. Node paling kanan merupakan node dengan nilai terbesar pada BST.


Baris 153–159

Pada baris 153–159 dibuat fungsi tampilkan_mahasiswa() yang digunakan untuk menampilkan data mahasiswa dalam bentuk tabel. Data yang ditampilkan meliputi NIM, nama, jurusan, dan IPK. Fungsi ini memanfaatkan format string agar tampilan data menjadi lebih rapi dan teratur.


Baris 161–172

Pada baris 161–172 dibuat fungsi input_ipk() yang digunakan untuk menerima input IPK dari user sekaligus melakukan validasi data. Program menggunakan try-except untuk menangani kesalahan input. Jika input bukan angka maka program akan menampilkan pesan error. Selain itu, program juga memastikan nilai IPK berada pada rentang 0.00 sampai 4.00.


Baris 174–185

Pada baris 174–185 dibuat fungsi input_mahasiswa() yang digunakan untuk menerima input data mahasiswa dari user. Data yang dimasukkan meliputi NIM, nama, jurusan, dan IPK. Pada bagian ini juga dilakukan validasi agar NIM tidak boleh kosong sebelum data mahasiswa dibuat menjadi object.


Baris 187–195

Pada baris 187–195 dibuat fungsi tampilkan_menu() yang digunakan untuk menampilkan menu utama program. Menu yang tersedia terdiri dari tambah data mahasiswa, cari data mahasiswa, tampilkan semua data, ubah data, hapus data, tampilkan NIM terkecil dan terbesar, serta menu keluar program.


Baris 197–268

Pada baris 197–268 dibuat fungsi main() sebagai program utama. Pada bagian ini dibuat object BST dan program dijalankan menggunakan perulangan while True sehingga menu akan terus tampil sampai user memilih keluar. Program juga melakukan validasi input agar pilihan menu harus berupa angka.


Baris 209–218

Pada baris 209–218 dibuat proses untuk menu nomor 1 yaitu tambah data mahasiswa. Program akan meminta user memasukkan data mahasiswa, kemudian data tersebut dimasukkan ke dalam BST menggunakan fungsi tambah().


Baris 220–231

Pada baris 220–231 dibuat proses untuk menu nomor 2 yaitu mencari data mahasiswa berdasarkan NIM. Jika data ditemukan maka program akan menampilkan data mahasiswa dalam bentuk tabel. Jika tidak ditemukan maka program menampilkan pesan error.


Baris 233–234

Pada baris 233–234 dibuat proses untuk menu nomor 3 yaitu menampilkan seluruh data mahasiswa secara urut menggunakan traversal inorder pada BST.


Baris 236–238

Pada baris 236–238 dibuat proses untuk menu nomor 4 yaitu mengubah data mahasiswa berdasarkan NIM yang dimasukkan user.


Baris 240–242

Pada baris 240–242 dibuat proses untuk menu nomor 5 yaitu menghapus data mahasiswa berdasarkan NIM menggunakan fungsi hapus().


Baris 244–261

Pada baris 244–261 dibuat proses untuk menu nomor 6 yaitu menampilkan mahasiswa dengan NIM terkecil dan terbesar. Program menggunakan fungsi cari_min() dan cari_max() untuk mendapatkan data tersebut.


Baris 263–265

Pada baris 263–265 dibuat proses untuk menu nomor 7 yaitu keluar dari program. Program menampilkan pesan “Program selesai.” kemudian menghentikan perulangan menggunakan break.


Baris 267–268

Pada baris 267–268 dibuat kondisi else untuk menangani jika user memasukkan pilihan menu yang tidak tersedia pada program.


Baris 270–271

Pada baris 270–271 digunakan kondisi:

if __name__ == "__main__":
    main()

Bagian ini digunakan untuk menjalankan fungsi main() saat file Python dijalankan secara langsung.

# Output Program
<img width="412" height="908" alt="Screenshot 2026-05-25 230422" src="https://github.com/user-attachments/assets/3c66b6be-43ec-4af9-8471-6c1ba6f2f7f9" />
<img width="432" height="688" alt="Screenshot 2026-05-25 230454" src="https://github.com/user-attachments/assets/08309f47-54ab-42dd-944a-a0ac14583b90" />
<img width="711" height="758" alt="Screenshot 2026-05-25 230508" src="https://github.com/user-attachments/assets/83be9221-a2c4-40fb-9668-8b581538c6bb" />
<img width="711" height="758" alt="Screenshot 2026-05-25 230508" src="https://github.com/user-attachments/assets/423ec696-6838-46ad-843d-3d1f4f095530" />
<img width="739" height="707" alt="Screenshot 2026-05-25 230523" src="https://github.com/user-attachments/assets/44c62b7d-55b0-472e-9d83-9b16bc8d923f" />
<img width="740" height="466" alt="Screenshot 2026-05-25 230534" src="https://github.com/user-attachments/assets/5025c20b-bb8f-4b8d-bd40-90882851658c" />

Pada saat program pertama kali dijalankan, sistem akan menampilkan menu utama program pendataan mahasiswa menggunakan Binary Search Tree (BST). Menu tersebut berisi beberapa pilihan seperti tambah data mahasiswa, cari data mahasiswa, tampilkan seluruh data, ubah data, hapus data, menampilkan NIM terkecil dan terbesar, serta keluar dari program. User diminta memilih menu dengan memasukkan angka sesuai fitur yang ingin digunakan.

Ketika user memilih menu nomor 1 yaitu tambah data mahasiswa, program akan meminta user memasukkan data berupa NIM, nama, jurusan, dan IPK. Pada contoh output, user menambahkan beberapa data mahasiswa seperti Arkan, Budiono, Caroline, dan Dewa dengan NIM yang berbeda-beda. Setelah data berhasil dimasukkan, program akan menampilkan pesan bahwa data mahasiswa berhasil ditambahkan. Data tersebut kemudian disimpan ke dalam struktur Binary Search Tree berdasarkan urutan NIM.

Selanjutnya, saat user memilih menu nomor 3 yaitu tampilkan semua data mahasiswa, program akan menampilkan seluruh data mahasiswa secara terurut berdasarkan NIM. Walaupun data dimasukkan tidak berurutan, BST menggunakan traversal inorder sehingga hasil output otomatis tersusun dari NIM terkecil ke terbesar. Pada output terlihat bahwa data mahasiswa tampil berurutan mulai dari NIM 260102, 260105, 260110, hingga 260116.

Pada saat user memilih menu nomor 2 yaitu cari data mahasiswa, program meminta user memasukkan NIM yang ingin dicari. Dalam contoh output, user mencari data dengan NIM 260102. Program kemudian berhasil menemukan data tersebut dan menampilkan informasi mahasiswa berupa NIM, nama, jurusan, dan IPK. Hal ini menunjukkan bahwa proses pencarian pada BST berjalan dengan baik menggunakan perbandingan nilai NIM.

Ketika user memilih menu nomor 4 yaitu ubah data mahasiswa, program terlebih dahulu meminta NIM mahasiswa yang ingin diubah. Pada contoh output, data dengan NIM 260105 dipilih untuk diubah. Program kemudian menampilkan data lama mahasiswa sebelum user memasukkan data baru. Setelah user memasukkan data baru seperti nama, jurusan, dan IPK, program akan menyimpan perubahan tersebut dan menampilkan pesan bahwa data berhasil diubah. Program juga memberikan catatan bahwa NIM tidak dapat diubah karena NIM digunakan sebagai key utama pada Binary Search Tree.

Pada saat user memilih menu nomor 5 yaitu hapus data mahasiswa, program meminta user memasukkan NIM mahasiswa yang ingin dihapus. Dalam contoh output, data mahasiswa dengan NIM 260102 berhasil dihapus dari BST. Setelah proses selesai, program menampilkan pesan bahwa data mahasiswa berhasil dihapus. Dengan demikian data tersebut tidak lagi tersimpan di dalam struktur tree.

Ketika user memilih menu nomor 6 yaitu menampilkan NIM terkecil dan terbesar, program akan mencari node paling kiri dan paling kanan pada BST. Node paling kiri merupakan data dengan NIM terkecil, sedangkan node paling kanan merupakan data dengan NIM terbesar. Pada contoh output, mahasiswa dengan NIM terkecil adalah 260105, sedangkan mahasiswa dengan NIM terbesar adalah 260116. Data lengkap mahasiswa tersebut kemudian ditampilkan dalam bentuk tabel.

Terakhir, saat user memilih menu nomor 7 yaitu keluar, program menghentikan seluruh proses perulangan dan menampilkan pesan “Program selesai.” sebagai tanda bahwa program telah selesai dijalankan dan sistem keluar dari aplikasi.

# Link YouTube
