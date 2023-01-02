pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
         Moys Bar
      List Menu Makanan 
 
==============================
    A. Mie Aceh Ganja : Rp 120.000
    B. Anggur Merah : Rp 55.000
    C. Ubi Unggu : Rp 80.000
    D. Puding Kecubung : Rp 30.000
    ==============================
   """"")
    pesan=str(input("masukkan list abjad menu makanan ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "Mie Aceh Ganja"
        harga=(120000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "b":
        listnama= "Anggur Merah"
        harga = (55000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "c":
        listnama= "Ubi Unggu"
        harga=int(80000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "d":
        listnama= "Puding Kecubung"
        harga=int(30000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("Moys Bar")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")