class Node:
    def __init__(self, key, value):
        self.key = key          
        self.value = value      
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\nIsi Hash Table Kamus Digital:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"({current.key}: {current.value}) -> ", end="")
                current = current.next

            print("NONE")


def main():
    kamus = HashMapSeparateChaining()

    kamus.insert("algoritma", "langkah-langkah untuk menyelesaikan masalah")
    kamus.insert("komputer", "alat elektronik untuk mengolah data")
    kamus.insert("hashmap", "struktur data yang menyimpan data dalam bentuk key-value")
    kamus.insert("array", "kumpulan data yang disimpan secara berurutan")
    kamus.insert("collision", "kondisi ketika dua key memiliki indeks hash yang sama")

    kamus.display()

    kata = "hashmap"
    hasil = kamus.search(kata)

    if hasil is not None:
        print(f"\nKata '{kata}' ditemukan dengan arti: {hasil.value}")
    else:
        print(f"\nKata '{kata}' tidak ditemukan")

    kamus.remove_key("array")
    print("\nSetelah menghapus kata 'array':")
    kamus.display()


if __name__ == "__main__":
    main()