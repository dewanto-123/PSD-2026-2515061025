# Program Pencarian Data Mahasiswa menggunakan Binary Search

def binary_search_mahasiswa(data, target):
    kiri = 0
    kanan = len(data) - 1
    target = target.lower()
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        nama_tengah = data[tengah][0].lower()
        print(f"Mengecek: {data[tengah][0]}")
        if nama_tengah == target:
            return tengah
        elif nama_tengah < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1

def main():
    mahasiswa = [
        ("Arkan", "231401001"),
        ("Budionowong", "231401002"),
        ("Cantika", "231401003"),
        ("Dewanto", "231401004"),
        ("Ezy", "231401005"),
        ("Flado", "231401006"),
        ("Gusrak", "231401007")
    ]

    print("Daftar Mahasiswa:")
    for nama, nim in mahasiswa:
        print(f" - {nama} : {nim}")

    target = input("\nMasukkan nama mahasiswa yang ingin dicari: ")
    index = binary_search_mahasiswa(mahasiswa, target)

    if index != -1:
        nama, nim = mahasiswa[index]
        print(f"\n{nama} ditemukan dengan NIM {nim}")
    else:
        print("\nNama tidak ditemukan")

if __name__ == "__main__":
    main()