import os


def BersihkanLayar(pesan):
    input(pesan)
    os.system("cls")
    from IPython.display import clear_output

    clear_output()


def cls():
    os.system("cls")
    from IPython.display import clear_output

    clear_output()


# def Tampilkan_Tipe_Kamar(Tipe_Kamar):
#   for i in range(len(Tipe_Kamar)):
#     print(Tipe_Kamar[i])


def Tampilkan_Tipe_Kamar(Tipe_Kamar):
    notipe = 1
    for b in Tipe_Kamar:
        # print(notipe,b,Tipe_Kamar.values())
        print(notipe, b, " Rp.", Tipe_Kamar.get(b))
        notipe += 1
    BersihkanLayar("\ntekan enter untuk melanjutkan...")


def Cari_Tipe_kamar(Tipe_Kamar):
    ketemu = False
    for b in Tipe_Kamar:
        if tipe in b:
            print("Tipe kamar  : " + tipe)
            print("Harga kamar : Rp.", Tipe_Kamar.get(b))
            BersihkanLayar("\ntekan enter untuk melanjutkan")
            ketemu = True
            return tipe
    if ketemu == False:
        BersihkanLayar(
            "Maaf Tipe Kamar yang Anda cari tidak ditemukan. \ntekan enter untuk melanjutkan"
        )


def Isi_Data_Kamar(Tipe_Kamar):
    ketemu = False
    for b, h in Tipe_Kamar.items():
        if b == kamar:
            harga = h
            print("Tipe kamar " + kamar + " Rp. " + str(h))
            ketemu = True
        if ketemu == False:
            continue

def Payment(Tipe_Kamar):
    for b, h in Tipe_Kamar.items():
        if b == kamar:
            harga = h
    totbay = harga * hari
    return totbay


def Update_Kamar2(Tipe_Kamar):
    Tipe_Kamar[kbaru] = hargabaru
    BersihkanLayar("Data berhasil disimpan, \ntekan enter untuk melanjutkan")


def Delete_Kamar(Tipe_Kamar):
    ketemu = False
    if kbaru in Tipe_Kamar:
        del Tipe_Kamar[kbaru]
        ketemu == True
        BersihkanLayar(
            "Data " + kbaru + " berhasil dihapus, tekan enter untuk melanjutkan"
        )
    elif ketemu == False:
        BersihkanLayar("Data kamar salah, tekan enter untuk melanjutkan")


def Tampilkan_Tambahan(Tambahan):
    notambah = 1
    for b in Tambahan:
        print(notambah, b)
        notambah += 1


def Payment_Lainnya(Tambahan):
    for b, h in Tambahan.items():
        if b == tambah:
            harga_tambahan = h
    totlan = (harga_tambahan * hari) + jumlah
    return totlan


def Lainnya(Tambahan):
    ketemu = False
    for b, h in Tambahan.items():
        if b == tambah:
            print("Tambahan " + tambah + " Per Item Rp." + str(h))
            harga_tambahan = h
            ketemu = True
    if ketemu == False:
        BersihkanLayar(
            "Maaf tipe tambahan salah, silahkan isi form kembali. \ntekan enter untuk melanjutkan"
        )


def Total_Semua():
    subtot = Payment_Lainnya(Tambahan) + Payment(Tipe_Kamar)
    return subtot


def lok():
    listipekamar = tuple(Tipe_Kamar)
    lantai_1 = "Lantai 1 :", listipekamar[0:5]
    lantai_2 = "Lantai 2 :", listipekamar[5:99]
    print(*lantai_1, end="\n")
    print(*lantai_2, end="\n")


# def lok(listlokkamar,listtipekamar):
#   listlokkamar = list(lokkamar)
#   listtipekamar = list(Tipe_Kamar)
#   lokkamar = Tipe_Kamar[listlokkamar]


# Program Utama
print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")

lismenu = [
    "MENU: ",
    "\n[1] Tampilkan Semua Tipe Kamar",
    "\n[2] Cari Tipe Kamar",
    "\n[3] Booking Kamar Sekarang",
    "\n[4] Update Kamar",
    "\n[5] Delete Kamar",
    "\n[6] Cek lokasi kamar",
    "\n[7] Exit",
]

tambahan = {
    "[1] Tambah bantal": 50000,
    "[2] Tambah selimut": 50000,
    "[3] Tambah extra bed": 200000,
}

lokkamar = (
    "\nLantai 1: \nStandar Room \nSuperior Room \nDeluxe Room \nFamily Room\n",
    "\nLantai 2: \nJunior Suite Room \nSuite Room \nPresidential Suite Room \nPenthouse Room\n",
)

Tipe_Kamar = {
    "Standard Room": 500000,
    "Superior Room": 800000,
    "Deluxe Room": 1000000,
    "Family Room": 1500000,
    "Junior Suite Room": 2000000,
    "Suite Room": 2800000,
    "Presidential Suite Room": 3500000,
    "Penthouse Room": 5000000,
}

Tambahan = {"Selimut": 50000, "Bantal": 50000, "Extra Bed": 200000}

# dictlisttipekamar = dict(lantai_1 = )
# Tipe_Kamar.append(lokkamar)
# print(listipekamar)

# def tdict(dic):
#   dic = dict(kamarbaru = kbaru,hbaru = hargabaru)
#   Tipe_Kamar.append(dic)

# Tipe_Kamar2 = ['1.Standard Room                Rp.500000',
# '2.Superior Room                Rp.800000',
# '3.Deluxe Room                  Rp.1000000',
# '4.Family Room                  Rp.1500000',
# '5.Junior Suite Room            Rp.2000000',
# '6.Suite Room                   Rp.2800000',
# '7.Presidential Suite Room      Rp.3500000',
# '8.Penthouse Room               Rp.5000000'
# ]

list_booking = []
pilih = "0"
while pilih != "7":
    print(*lismenu)

    pilih = input("Pilihan menu: ")

    if pilih == "1":
        print("\nType Of Room in Dayeuhkolot Tropicana Hotel & Resort: ")
        Tampilkan_Tipe_Kamar(Tipe_Kamar)
        # BersihkanLayar("\ntekan enter untuk melanjutkan...")
        print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")

    elif pilih == "2":
        tipe = input("\nMasukkan tipe kamar yang Anda cari : ")
        Cari_Tipe_kamar(Tipe_Kamar)
        print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")

    elif pilih == "3":
        print("  _____________________\n   ---ISI DATA DIRI---")
        nama = input("\nMasukkan nama Anda : ")
        nikktp = input("Masukkan NIK KTP Anda : ")
        email = input("Masukkan Email Anda: ")
        print("  ______________________\n   ---ISI DATA KAMAR---")
        kamar = input("\nMasukkan tipe kamar yang ingin Anda booking : ")
        Isi_Data_Kamar(Tipe_Kamar)
        hari = int(input("Berapa malam Anda mem-Booking Tipe Kamar tersebut: "))
        # print("Participant: ")
        # adult = int(input("How many Adult: "))
        # child = int(input("How many Child: "))
        print("  __________________________\n   ---TAMBAHAN LAINNYA---")
        pil = input("Apakah Anda membutuhkan Selimut, Bantal atau Extra Bed (y/t): ")
        if pil == "y":
            Tampilkan_Tambahan(Tambahan)
            tambah = input("Masukkan Tambahan yang Anda perlukan: ")
            jumlah = int(input("Masukan jumlah barang: "))
            Lainnya(Tambahan)
            Payment_Lainnya(Tambahan)
            print("  __________________________\n   ---SELESAIKAN PAYMENT---")
            Payment(Tipe_Kamar)
            payment = input(
                "\nChoose Your Payment! \n [1] Debit Card \n [2] Credit card \nMasukkan pilihan Payment Anda: "
            )
            if payment == "1":
                print("\nPayment yang Anda pilih adalah Debit Card")
                nokartu = int(input("Masukan No kartu anda: "))
                print(
                    " ___________________________\n     ---HASIL PAYMENT---\n =========================="
                )
                print(
                    "No kartu : ",
                    nokartu,
                    "\nAtas nama: ",
                    nama,
                    "\nNIK KTP  :",
                    nikktp,
                    "\nEmail    :",
                    email,
                    "\nTipe Kamar:",
                    kamar,
                    "\nTotal harga kamar   :",
                    Payment(Tipe_Kamar),
                    "\nTotal harga tambahan:",
                    Payment_Lainnya(Tambahan),
                    "\nTotal Keseluruhan   :",
                    Total_Semua(),
                    "\nVirtual Code        : 7001889235677",
                )
                print("Data booking Anda berhasil ditambahkan")
                print("Silahkan Tunggu Hasil Cetak Booking melalui Email: ", email)
                BersihkanLayar("Terima Kasih, tekan enter untuk kembali ke menu")
                print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")
                del Tipe_Kamar[kamar]
                if Tipe_Kamar == False:
                    print("Maaf kamar tidak tersedia")
                    continue

            elif payment == "2":
                print("\nPayment yang Anda pilih adalah Credit Card")
                nokartu = int(input("Masukan No kartu anda: "))
                print(
                    " ________________________\n     ---HASIL PAYMENT---\n ============================="
                )
                print(
                    "No kartu : ",
                    nokartu,
                    "\nAtas nama: ",
                    nama,
                    "\nNIK KTP  :",
                    nikktp,
                    "\nEmail    :",
                    email,
                    "\nTipe Kamar:",
                    kamar,
                    "\nTotal harga kamar   :",
                    Payment(Tipe_Kamar),
                    "\nTotal harga tambahan:",
                    Payment_Lainnya(Tambahan),
                    "\nTotal Keseluruhan   :",
                    Total_Semua(),
                    "\nVirtual Code       : 7001889235677",
                )
                print("Data booking Anda berhasil ditambahkan")
                print("Silahkan Tunggu Hasil Cetak Booking melalui Email: ", email)
                BersihkanLayar("Terima Kasih, tekan enter untuk kembali ke menu")
                print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")
                del Tipe_Kamar[kamar]
            else:
                BersihkanLayar(
                    "Pilihan menu anda tidak dikenali, tekan enter untuk melanjutkan"
                )

        elif pil == "t":
            print("  __________________________\n   ---SELESAIKAN PAYMENT---")
            Payment(Tipe_Kamar)
            payment = input(
                "\nChoose Your Payment! \n [1] Debit Card \n [2] Credit card \nMasukkan pilihan Payment Anda: "
            )
            if payment == "1":
                print("\nPayment yang Anda pilih adalah Debit Card")
                nokartu = int(input("Masukan No kartu anda: "))
                print(
                    " ___________________________\n     ---HASIL PAYMENT---\n ==========================="
                )
                print(
                    "No kartu : ",
                    nokartu,
                    "\nAtas nama: ",
                    nama,
                    "\nNIK KTP  :",
                    nikktp,
                    "\nEmail    :",
                    email,
                    "\nTipe Kamar:",
                    kamar,
                    "\nTotal harga kamar   :",
                    Payment(Tipe_Kamar),
                    "\nTotal Keseluruhan   :",
                    Payment(Tipe_Kamar),
                    "\nVirtual Code : 7001889235677",
                )
                print("Data booking Anda berhasil ditambahkan")
                print("Silahkan Tunggu Hasil Cetak Booking melalui Email: ", email)
                BersihkanLayar("Terima Kasih, tekan enter untuk kembali ke menu")
                print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")
                del Tipe_Kamar[kamar]

            elif payment == "2":
                print("\nPayment yang Anda pilih adalah Credit Card")
                nokartu = int(input("Masukan No kartu anda: "))
                print(
                    " ________________________\n     ---HASIL PAYMENT---\n ============================="
                )
                cetakan = print(
                    "No kartu : ",
                    nokartu,
                    "\nAtas nama: ",
                    nama,
                    "\nNIK KTP  :",
                    nikktp,
                    "\nEmail    :",
                    email,
                    "\nTipe Kamar:",
                    kamar,
                    "\nTotal harga kamar   :",
                    Payment(Tipe_Kamar),
                    "\nTotal Keseluruhan   :",
                    Payment(Tipe_Kamar),
                    "\nVirtual Code : 7001889235677",
                )
                print("Data booking Anda berhasil ditambahkan")
                print("Silahkan Tunggu Hasil Cetak Booking melalui Email: ", email)
                BersihkanLayar("Terima Kasih, tekan enter untuk kembali ke menu")
                print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")
                del Tipe_Kamar[kamar]

            else:
                BersihkanLayar(
                    "Pilihan menu anda tidak dikenali, tekan enter untuk melanjutkan"
                )
        else:
            BersihkanLayar("User tidak dikenal, tekan enter untuk melanjutkan")
            print("Pilihan Anda tidak sesuai, Mohon pengisian Booking di Ulang")

    elif pilih == "4":
        username = input("Masukan username admin: ")
        password = input("Masukan Password admin: ")
        if username == "admin" and password == "admin":
            namaadmin = "Lord Matin"
            print("Welcome", namaadmin)
            kbaru = input("Masukan tipe kamar baru: ")
            hargabaru = input("Masukan Harga Baru: ")
            Update_Kamar2(Tipe_Kamar)
            print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")
        else:
            BersihkanLayar("User tidak dikenal, tekan enter untuk melanjutkan")
            print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")

    elif pilih == "5":
        username = input("Masukan username admin: ")
        password = input("Masukan Password admin: ")
        if username == "admin" and password == "admin":
            namaadmin = "Lord Matin"
            print("Welcome", namaadmin)
            kbaru = input("Masukan tipe kamar yang akan dihapus: ")
            Delete_Kamar(Tipe_Kamar)
            print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")

        else:
            BersihkanLayar("User tidak dikenal, tekan enter untuk melanjutkan")
            print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")

    elif pilih == "8":
        print("daft")
        cetakan.append(list_booking)

    elif pilih == "6":
        # print("\nLokasi Kamar : ")
        lok()
        BersihkanLayar("tekan enter untuk melanjutkan")
        print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")

    elif pilih == "7":
        print("babay")

    else:
        BersihkanLayar(
            "Pilihan menu anda tidak dikenali, tekan enter untuk melanjutkan"
        )
        print("WELOCOME TO, \n~~~~Dayeuhkolot Tropicana Hotel & Resort~~~~")
