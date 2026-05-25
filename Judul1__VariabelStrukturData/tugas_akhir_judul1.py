class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.rear  = None

    def create_new_node(self, n):
        new_node = Node(n)
        return new_node

    def insert_node(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear  = new_node
        else:
            new_node.prev  = self.rear
            self.rear.next = new_node
            self.rear      = new_node

    def traverse_forward(self):
        print("Traversal maju (Start → End): ", end="")
        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def traverse_backward(self):
        print("Traversal mundur (End → Start): ", end="")
        current = self.rear
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()

    def cari_petak(self, nama):
    #nMencari petak berdasarkan nama (case-insensitive).
        current = self.start
        posisi  = 1
        while current is not None:
            if nama.lower() in current.data.lower():
                return current, posisi
            current = current.next
            posisi += 1
        return None, -1

    def tampilkan_semua(self):
       # Menampilkan semua petak beserta nomornya.
        current = self.start
        nomor   = 1
        print("\n{'No':<5} {'Nama Petak'}")
        print("-" * 40)
        while current is not None:
            print(f"{nomor:<5} {current.data}")
            current = current.next
            nomor  += 1
        print("-" * 40)
        print(f"Total petak: {nomor - 1}\n")

    def gerak_pemain(self, posisi_awal, langkah):
        
    #  Mensimulasikan pergerakan pemain dari posisi_awal sebanyak langkah.
    #  Posisi berbasis 1. Jika melewati petak terakhir, kembali ke awal (GO).
       
        # Hitung total node
        total = 0
        cur   = self.start
        while cur is not None:
            total += 1
            cur    = cur.next

        posisi_baru = ((posisi_awal - 1 + langkah) % total) + 1

        # Ambil node di posisi baru
        cur   = self.start
        nomor = 1
        while cur is not None and nomor < posisi_baru:
            cur   = cur.next
            nomor += 1

        return posisi_baru, cur.data if cur else "?"


def main():
    dll = DoublyLinkedList()
    petak_monopoli = [
        "GO",
        "Mediterranean Avenue  [$60]",
        "Community Chest",
        "Baltic Avenue         [$60]",
        "Income Tax            [-$200]",
        "Reading Railroad      [$200]",
        "Oriental Avenue       [$100]",
        "Chance",
        "Vermont Avenue        [$100]",
        "Connecticut Avenue    [$120]",
        "Just Visiting / Jail",
        "St. Charles Place     [$140]",
        "Electric Company      [$150]",
        "States Avenue         [$140]",
        "Virginia Avenue       [$160]",
        "Pennsylvania Railroad [$200]",
        "St. James Place       [$180]",
        "Community Chest",
        "Tennessee Avenue      [$180]",
        "New York Avenue       [$200]",
        "Free Parking",
        "Kentucky Avenue       [$220]",
        "Chance",
        "Indiana Avenue        [$220]",
        "Illinois Avenue       [$240]",
        "B&O Railroad          [$200]",
        "Atlantic Avenue       [$260]",
        "Ventnor Avenue        [$260]",
        "Water Works           [$150]",
        "Marvin Gardens        [$280]",
        "Go To Jail",
        "Pacific Avenue        [$300]",
        "North Carolina Avenue [$300]",
        "Community Chest",
        "Pennsylvania Avenue   [$320]",
        "Short Line Railroad   [$200]",
        "Chance",
        "Park Place            [$350]",
        "Luxury Tax            [-$100]",
        "Boardwalk             [$400]",
    ]

    for nama in petak_monopoli:
        new_node = dll.create_new_node(nama)
        if new_node is not None:
            dll.insert_node(new_node)

 
    print("=" * 50)
    print("   SIMULASI PAPAN MONOPOLI - Doubly Linked List")
    print("=" * 50)

    while True:
        print("\nMENU:")
        print("1. Tampilkan semua petak")
        print("2. Traversal maju")
        print("3. Traversal mundur")
        print("4. Cari petak")
        print("5. Simulasi gerak pemain")
        print("6. Keluar")

        try:
            pilihan = int(input("Pilih menu (1-6): "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            dll.tampilkan_semua()

        elif pilihan == 2:
            dll.traverse_forward()

        elif pilihan == 3:
            dll.traverse_backward()

        elif pilihan == 4:
            kata = input("Masukkan nama petak yang dicari: ")
            node, pos = dll.cari_petak(kata)
            if node:
                print(f"Petak ditemukan di posisi {pos}: {node.data}")
                if node.prev:
                    print(f"  Sebelumnya : {node.prev.data}")
                if node.next:
                    print(f"  Sesudahnya : {node.next.data}")
            else:
                print("Petak tidak ditemukan.")

        elif pilihan == 5:
            try:
                pos_awal = int(input("Posisi awal pemain (1-40): "))
                dadu     = int(input("Jumlah langkah (lemparan dadu): "))
            except ValueError:
                print("Masukkan angka yang valid!")
                continue

            pos_baru, nama_petak = dll.gerak_pemain(pos_awal, dadu)
            print(f"Pemain bergerak {dadu} langkah.")
            print(f"Posisi baru: [{pos_baru}] {nama_petak}")

        elif pilihan == 6:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid, melakukan traversal maju")
            dll.traverse_forward()

main()