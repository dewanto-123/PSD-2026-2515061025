def insertion_sort(arr, n):
    for i in range(1, n):
        temp_data = arr[i]
        j = i - 1
        while j >= 0 and arr[j][1] > temp_data[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp_data

def main():
    try:
        n = int(input("Masukkan jumlah akun media sosial: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan nama akun dan jumlah followernya:")
    for i in range(n):
        print(f"Akun ke-{i + 1}")
        nama = input("Nama akun: ")
        while True:
            try:
                follower = int(input("Jumlah follower: "))
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
        arr.append([nama, follower])

    print("\nArray sebelum diurutkan:")
    for akun in arr:
        print(akun[0], "-", akun[1], "follower")

    insertion_sort(arr, n)

    print("\nArray setelah diurutkan (Insertion Sort):")
    for akun in arr:
        print(akun[0], "-", akun[1], "follower")

if __name__ == "__main__":
    main()