class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class QueueRumahSakit:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def ambil_antrian(self, nama):
        new_node = Node(nama)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{nama} berhasil masuk antrian rumah sakit")

    def layani_pasien(self):
        if self.is_empty():
            print("Tidak ada pasien dalam antrian")
            return
        pasien = self.front.nama
        print(f"Pasien {pasien} sedang dilayani")
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def lihat_antrian(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print("Daftar antrian pasien:")
        current = self.front
        nomor = 1
        while current is not None:
            print(f"{nomor}. {current.nama}")
            current = current.next
            nomor += 1

def main():
    rs = QueueRumahSakit()
    while True:
        print("\nSISTEM ANTRIAN RUMAH SAKIT ")
        print("1. Ambil Antrian")
        print("2. Layani Pasien")
        print("3. Lihat Antrian")
        print("4. Keluar Program")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            nama = input("Masukkan nama pasien: ")
            rs.ambil_antrian(nama)
        elif pilihan == "2":
            rs.layani_pasien()
        elif pilihan == "3":
            rs.lihat_antrian()
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()