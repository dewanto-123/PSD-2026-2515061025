class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

class Node:
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def tambah(self, mahasiswa):
        if self.root is None:
            self.root = Node(mahasiswa)
            return True

        return self._tambah_recursive(self.root, mahasiswa)

    def _tambah_recursive(self, node, mahasiswa):
        if mahasiswa.nim < node.mahasiswa.nim:
            if node.left is None:
                node.left = Node(mahasiswa)
                return True
            return self._tambah_recursive(node.left, mahasiswa)

        elif mahasiswa.nim > node.mahasiswa.nim:
            if node.right is None:
                node.right = Node(mahasiswa)
                return True
            return self._tambah_recursive(node.right, mahasiswa)

        else:
            return False

    def cari(self, nim):
        return self._cari_recursive(self.root, nim)

    def _cari_recursive(self, node, nim):
        if node is None:
            return None

        if nim == node.mahasiswa.nim:
            return node

        elif nim < node.mahasiswa.nim:
            return self._cari_recursive(node.left, nim)

        else:
            return self._cari_recursive(node.right, nim)

    def tampilkan_inorder(self):
        if self.root is None:
            print("Belum ada data mahasiswa.")
        else:
            print("\nDaftar Mahasiswa Urut Berdasarkan NIM")
            print("-" * 75)
            print(f"{'NIM':<15}{'Nama':<25}{'Jurusan':<25}{'IPK'}")
            print("-" * 75)
            self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            tampilkan_mahasiswa(node.mahasiswa)
            self._inorder_recursive(node.right)

    def ubah(self, nim):
        node = self.cari(nim)

        if node is None:
            print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.")
            return

        print("\nData lama:")
        print("-" * 75)
        print(f"{'NIM':<15}{'Nama':<25}{'Jurusan':<25}{'IPK'}")
        print("-" * 75)
        tampilkan_mahasiswa(node.mahasiswa)

        print("\nMasukkan data baru")
        nama = input("Masukkan Nama     : ")
        jurusan = input("Masukkan Jurusan  : ")
        ipk = input_ipk()

        node.mahasiswa.nama = nama
        node.mahasiswa.jurusan = jurusan
        node.mahasiswa.ipk = ipk

        print("Data mahasiswa berhasil diubah.")
        print("Catatan: NIM tidak diubah karena NIM adalah key pada BST.")

    def hapus(self, nim):
        self.root, berhasil = self._hapus_recursive(self.root, nim)

        if berhasil:
            print("Data mahasiswa berhasil dihapus.")
        else:
            print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.")

    def _hapus_recursive(self, node, nim):
        if node is None:
            return node, False

        if nim < node.mahasiswa.nim:
            node.left, berhasil = self._hapus_recursive(node.left, nim)
            return node, berhasil

        elif nim > node.mahasiswa.nim:
            node.right, berhasil = self._hapus_recursive(node.right, nim)
            return node, berhasil

        else:
            if node.left is None and node.right is None:
                return None, True

            elif node.left is None:
                return node.right, True

            elif node.right is None:
                return node.left, True

            else:
                pengganti = self._cari_min_node(node.right)
                node.mahasiswa = pengganti.mahasiswa
                node.right, _ = self._hapus_recursive(node.right, pengganti.mahasiswa.nim)
                return node, True

    def cari_min(self):
        if self.root is None:
            return None
        return self._cari_min_node(self.root)

    def _cari_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def cari_max(self):
        if self.root is None:
            return None

        node = self.root
        while node.right is not None:
            node = node.right
        return node

def tampilkan_mahasiswa(mahasiswa):
    print(
        f"{mahasiswa.nim:<15}"
        f"{mahasiswa.nama:<25}"
        f"{mahasiswa.jurusan:<25}"
        f"{mahasiswa.ipk:.2f}"
    )

def input_ipk():
    while True:
        try:
            ipk = float(input("Masukkan IPK      : "))

            if 0.0 <= ipk <= 4.0:
                return ipk
            else:
                print("IPK harus berada di antara 0.00 sampai 4.00.")

        except ValueError:
            print("IPK harus berupa angka.")

def input_mahasiswa():
    while True:
        nim = input("Masukkan NIM      : ").strip()
        if nim != "":
            break
        print("NIM tidak boleh kosong.")

    nama = input("Masukkan Nama     : ")
    jurusan = input("Masukkan Jurusan  : ")
    ipk = input_ipk()

    return Mahasiswa(nim, nama, jurusan, ipk)

def tampilkan_menu():
    print("PROGRAM PENDATAAN MAHASISWA DENGAN BST")
    print("1. Tambah Data Mahasiswa")
    print("2. Cari Data Mahasiswa")
    print("3. Tampilkan Semua Data Mahasiswa")
    print("4. Ubah Data Mahasiswa")
    print("5. Hapus Data Mahasiswa")
    print("6. Tampilkan NIM Terkecil dan Terbesar")
    print("7. Keluar")

def main():
    bst = BinarySearchTree()

    while True:
        tampilkan_menu()

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka.")
            continue

        if pilihan == 1:
            print("\nTambah Data Mahasiswa")
            mahasiswa = input_mahasiswa()

            berhasil = bst.tambah(mahasiswa)

            if berhasil:
                print("Data mahasiswa berhasil ditambahkan.")
            else:
                print("Gagal menambahkan data. NIM sudah terdaftar.")

        elif pilihan == 2:
            nim = input("Masukkan NIM yang dicari: ").strip()
            hasil = bst.cari(nim)

            if hasil is not None:
                print("\nData mahasiswa ditemukan:")
                print("-" * 75)
                print(f"{'NIM':<15}{'Nama':<25}{'Jurusan':<25}{'IPK'}")
                print("-" * 75)
                tampilkan_mahasiswa(hasil.mahasiswa)
            else:
                print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.")

        elif pilihan == 3:
            bst.tampilkan_inorder()

        elif pilihan == 4:
            nim = input("Masukkan NIM mahasiswa yang ingin diubah: ").strip()
            bst.ubah(nim)

        elif pilihan == 5:
            nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ").strip()
            bst.hapus(nim)

        elif pilihan == 6:
            min_node = bst.cari_min()
            max_node = bst.cari_max()

            if min_node is None or max_node is None:
                print("Belum ada data mahasiswa.")
            else:
                print("\nMahasiswa dengan NIM terkecil:")
                print("-" * 75)
                print(f"{'NIM':<15}{'Nama':<25}{'Jurusan':<25}{'IPK'}")
                print("-" * 75)
                tampilkan_mahasiswa(min_node.mahasiswa)

                print("\nMahasiswa dengan NIM terbesar:")
                print("-" * 75)
                print(f"{'NIM':<15}{'Nama':<25}{'Jurusan':<25}{'IPK'}")
                print("-" * 75)
                tampilkan_mahasiswa(max_node.mahasiswa)

        elif pilihan == 7:
            print("Program selesai.")
            break

        else:
            print("Pilihan menu tidak tersedia.")

if __name__ == "__main__":
    main()