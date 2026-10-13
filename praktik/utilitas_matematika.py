def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif.")

    total = 0
    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif.")

    hasil = 1
    for i in range(2, n + 1):
        hasil *= i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")


def baca_bilangan_nonnegatif(pesan):
    nilai = input(pesan).strip()

    try:
        n = int(nilai)
    except ValueError:
        raise ValueError("Masukkan bilangan bulat yang valid.")

    if n < 0:
        raise ValueError("Bilangan harus nonnegatif.")

    return n


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi: ").strip()

        try:
            if pilihan == "1":
                p = float(input("Panjang: "))
                l = float(input("Lebar: "))

                if p < 0 or l < 0:
                    print("Panjang dan lebar tidak boleh negatif.")
                else:
                    hasil = luas_persegi_panjang(p, l)
                    print("Luas persegi panjang =", hasil)

            elif pilihan == "2":
                a = float(input("Alas: "))
                t = float(input("Tinggi: "))

                if a < 0 or t < 0:
                    print("Alas dan tinggi tidak boleh negatif.")
                else:
                    hasil = luas_segitiga(a, t)
                    print("Luas segitiga =", hasil)

            elif pilihan == "3":
                n = baca_bilangan_nonnegatif("Masukkan n: ")
                print("Jumlah 1 sampai", n, "=", jumlah_n(n))

            elif pilihan == "4":
                n = baca_bilangan_nonnegatif("Masukkan n: ")
                print("Faktorial", n, "=", faktorial(n))

            elif pilihan == "0":
                print("Program selesai. Terima kasih!")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih 0-4.")

        except ValueError as e:
            print("Input tidak valid:", e)


if __name__ == "__main__":
    main()