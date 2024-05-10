# 1.Ilham memiliki sebuah list yang berisi angka-angka acak. Anda ingin menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0, dan akan mengurutkan dari nilai yang terbesar ke yang terkecil. Bantu Ilham untuk menyelesaikan persoalan tersebut menggunakan array method.
# Input: [8, 3, 12, 4, 7, 2]
# Output: [12, 8, 7, 4, 0, 0]

# 2.Budi memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang merupakan bilangan ganjil dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Bantu budi untuk menyelesaikan persoalan tersebut menggunakan array method.
# Input: [7, 4, 9, 2, 5, 1]
# Output: [2, 4]

# 3.Rani memiliki sebuah list yang berisi buah-buahan. Dia ingin menghapus semua kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut secara alfabetis. Bantulah Rani untuk mencapai ini.
# Input: kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
# Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

# 4.Dewi memiliki dua list yang berisi nama-nama buah-buahan. Dia ingin menggabungkan kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama. Setelah itu, dia ingin mengurutkan sisa buah-buahan secara alfabetis. Bantu Dewi
# Input: ["apel", "jeruk", "mangga"], ["apel", "anggur", "nanas"]
# Output: ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']

# 5.Dina memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang kurang dari 10 dan lebih dari 100, dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Implementasikan ini dengan menggunakan metode-metode yang tepat dari list.
# Input: [105, 20, 8, 150, 30, 5, 200]
# Output: [20, 30]

# 1)
numbers = [8, 3, 12, 4, 7, 2]
# Mengganti nilai kurang dari 5 dengan 0
numbers = [0 if num < 5 else num for num in numbers]
# Mengurutkan dari nilai terbesar ke terkecil
numbers.sort(reverse=True)
# Output hasil
print(numbers)

# 2)
# List input dari Budi
numbers = [7, 4, 9, 2, 5, 1]
# Menghapus nilai-nilai ganjil
even_numbers = [number for number in numbers if number % 2 == 0]
# Mengurutkan nilai-nilai yang tersisa dari terkecil ke terbesar
sorted_numbers = sorted(even_numbers)
# Menampilkan output
print("Input:", numbers)
print("Output:", sorted_numbers)

# 3)
kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
# Menghapus kata dengan panjang kurang dari lima karakter
kata = [k for k in kata if len(k) >= 5]
# Mengurutkan sisa kata secara alfabetis
kata.sort()
print(kata)

# 4)
def gabung_dan_urutkan(list1, list2):
    # Gabungkan kedua list
    gabungan = list1 + list2
    # Hapus semua buah yang memiliki nama yang sama
    unik = list(set(gabungan))
    # Urutkan sisa buah-buahan secara alfabetis
    hasil = sorted(unik)
    return hasil
# List buah-buahan Dewi
buah_dewi1 = ["apel", "jeruk", "mangga"]
buah_dewi2 = ["apel", "anggur", "nanas"]
# Panggil fungsi gabung_dan_urutkan
hasil_gabung_dan_urutkan = gabung_dan_urutkan(buah_dewi1, buah_dewi2)
# Cetak hasil
print("Output:", hasil_gabung_dan_urutkan)

# 5)
# Input list
nilai = [105, 20, 8, 150, 30, 5, 200]
# Menghapus nilai yang kurang dari 10 dan lebih dari 100
nilai_baru = [x for x in nilai if 10 <= x <= 100]
# Mengurutkan nilai yang tersisa
nilai_baru.sort()
# Output
print(nilai_baru)