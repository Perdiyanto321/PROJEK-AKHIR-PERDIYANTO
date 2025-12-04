daftar_sopir = {
    "Budi": ["Mobil", "B 1234 CD", "tersedia"],
    "Andi": ["Motor", "D 4321 AB", "tersedia"],
    "Joko": ["Mobil", "F 9999 ZZ", "sibuk"]
}

pesanan = {

}

struk = {

}

akun = {
    "username": "admin",
    "password": "admin123"

}

def tampilkan_sopir():
    print("\n=== DAFTAR SOPIR ===")
    if not daftar_sopir:
        print("Tidak ada sopir.")
        return
    
    for nama, data in daftar_sopir.items():
        print(f"- {nama}: {data[0]} ({data[1]}) - {data[2]}")

def tambah_sopir():
    print("\n=== TAMBAH SOPIR ===")
    while True:
        while True:
            while True:
                nama = input("Nama sopir: ").strip()

                if any(char.isdigit() for char in nama):
                    print("Tidak bisa mengandung angka")
                else:
                    break
        
            if not nama:
                print("Nama sopir tidak boleh kosong. Coba lagi.")
                continue
        
            sopir = []

            for i in daftar_sopir.keys():
                sopir.append(i.lower())

            if nama.lower() in sopir:
                print("Nama sopir sudah ada!")
                return
            else:
                break
    
        while True:
            jenis = input("Jenis kendaraan (Mobil/Motor): ").strip().lower()
            if jenis not in ["mobil", "motor"]:
                print("Jenis kendaraan harus 'Mobil' atau 'Motor'. Coba lagi.")
                continue
            break
        
        while True:
            plat = input("Plat nomor: ").strip().upper()

            if len(plat.strip()) > 9:
                print("panjang plat nomer tidak boleh lebih dari 7")
                            
            if not plat:
                print("Plat nomor tidak boleh kosong. Coba lagi.")
                continue
            
            else:
                break
    
        daftar_sopir[nama.title()] = [jenis.capitalize(), plat, "tersedia"]
        print("Sopir berhasil ditambahkan!")
        break

def update_sopir():
    tampilkan_sopir()
    while True:
        nama = input("Masukkan nama sopir yang ingin diubah: ").strip()

        sopir = []
        for i in daftar_sopir.keys():
            sopir.append(i.lower())
        
        if nama.lower() not in sopir:
            print("Sopir tidak ditemukan!")
            return
        break
    
    print("\n1. Ubah nama")
    print("2. Ubah jenis kendaraan")
    print("3. Ubah plat")
    print("4. Ubah status")
    
    while True:
        while True:
            pilihan = input("Pilih nomor menu: ").strip()
            if pilihan not in ["1", "2", "3", "4"]:
                print("Pilihan tidak valid! Pilih 1-4.")
                continue
            else:
                break
    
        if pilihan == "1":
            while True:
                nama_baru = input("Nama baru: ").strip()
                if not nama_baru:
                    print("Nama baru tidak boleh kosong. Coba lagi.")
                    continue
                
                sopir = []
                for i in daftar_sopir.keys():
                    sopir.append(i.lower())

                if nama_baru.lower() in sopir:
                    print("Nama sopir sudah ada!")
                    continue
                
                else:
                    break
            daftar_sopir[nama_baru.title()] = daftar_sopir.pop(nama.title())
            print("Nama sopir berhasil diubah!")
            break
        
        elif pilihan == "2":
            while True:
                jenis_baru = input("Jenis kendaraan baru (Mobil/Motor): ").strip()
                if jenis_baru.lower() not in ["mobil", "motor"]:
                    print("Jenis kendaraan harus 'Mobil' atau 'Motor'. Coba lagi.")
                    continue
                break
            daftar_sopir[nama.title()][0] = jenis_baru.capitalize()
            print("Jenis kendaraan berhasil diubah!")
            break   
        
        elif pilihan == "3":
            while True:
                plat_baru = input("Plat baru: ").strip().upper()
                if not plat_baru:
                    print("Plat baru tidak boleh kosong. Coba lagi.")
                    continue

                data = []
                for i in daftar_sopir.values():
                    data.append(i[1])   
                if plat_baru.upper() in data:
                    print("Plat nomor sudah ada ")
                    continue
                else:
                    break
                    
            daftar_sopir[nama.title()][1] = plat_baru
            print("Plat berhasil diubah!")
            break
        
        elif pilihan == "4":
            while True:
                status_baru = input("Status baru (tersedia/sibuk): ").strip().lower()
                if status_baru not in ["tersedia", "sibuk"]:
                    print("Status harus 'tersedia' atau 'sibuk'. Coba lagi.")
                    continue
                break
            daftar_sopir[nama.title()][2] = status_baru
            print("Status berhasil diubah!")
            break

def hapus_sopir():
    tampilkan_sopir()
    while True:
        sopir = []
        for i in daftar_sopir.keys():
            sopir.append(i.lower())

        nama = input("Masukkan nama sopir yang ingin dihapus: ").strip()
        if nama.lower() not in sopir:
            print("Sopir tidak ditemukan!")
        
        else:
            break
    
    del daftar_sopir[nama.title()]
    print("Sopir berhasil dihapus!")

def pesan_transport():
    print("\n=== PEMESANAN TRANSPORTASI ===")
    
    sopir_tersedia = [nama for nama, data in daftar_sopir.items() if data[2].lower() == "tersedia"]
 
    if not sopir_tersedia:
        print("Tidak ada sopir tersedia!")
        return
    
    print("Sopir tersedia:")
    for i, nama in enumerate(sopir_tersedia, 1):
        kendaraan, plat, _ = daftar_sopir[nama]
        print(f"{i}. {nama} - {kendaraan} ({plat})")
    
    while True:
        try:
            idx = int(input("Pilih sopir (nomor): ")) - 1
            if not (0 <= idx < len(sopir_tersedia)):
                print("Pilihan tidak valid! Masukkan nomor yang benar.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")
            continue
    
    nama = sopir_tersedia[idx]
    kendaraan, plat, _ = daftar_sopir[nama]
    
    daftar_sopir[nama][2] = "sibuk"
    
    print(f"Transport dengan sopir {nama} berhasil dipesan!")
    
    while True:
        try:
            jarak = float(input("Masukkan jarak (km): "))
            if jarak <= 0:
                print("Jarak harus lebih dari 0. Coba lagi.")
                continue
            break
        except ValueError:
            print("Jarak harus berupa angka. Coba lagi.")
            continue

    nama_pemesan = input("masukan nama anda ")
    
    if kendaraan.lower() == "mobil":
        harga = jarak * 10000
    else:
        harga = jarak * 5000
    
    print(f"nama pemesan {nama}")
    print(f"Harga: Rp{harga:,.0f}")
    
    pesanan[nama] = {
        "kendaraan": kendaraan,
        "plat": plat,
        "jarak": jarak,
        "harga": harga,
        "nama pemesan": nama_pemesan
    }

    struk[nama] = {
        "kendaraan": kendaraan,
        "plat": plat,
        "jarak": jarak,
        "harga": harga,
        "nama pemesan": nama_pemesan
    }
    
    print("Pesanan berhasil disimpan!")

def tampilkan_pesanan():
    print("\n=== DAFTAR PESANAN ===")
    if not pesanan:
        print("Belum ada pesanan.")
        return
    
    for nama, data in pesanan.items():
        print(f"- {nama}: nama pemesan {data['nama pemesan']} {data['kendaraan']} ({data['plat']}), Jarak: {data['jarak']} km, Harga: Rp{data['harga']:,.0f}")

def update_pesanan_admin():
    tampilkan_pesanan()
    if not pesanan:
        return
    
    while True:
        sopir = []
        for i in pesanan.keys():
            sopir.append(i.lower())

        nama = input("\nMasukkan nama sopir yang ingin diubah pesanannya: ").strip()
        if nama.lower() not in sopir:
            print("Pesanan tidak ditemukan!")
            return
        break
    
    print("\n1. Ubah jarak")
    print("2. Ubah harga")
    
    while True:
        pilihan = input("Pilih nomor menu: ").strip()
        if pilihan not in ["1", "2"]:
            print("Pilihan tidak valid! Pilih 1 atau 2.")
            continue
        break
    
    if pilihan == "1":
        while True:
            try:
                jarak_baru = float(input("Jarak baru (km): "))
                if jarak_baru <= 0:
                    print("Jarak harus lebih dari 0. Coba lagi.")
                    continue
                break
            except ValueError:
                print("Jarak harus berupa angka. Coba lagi.")
                continue
        
        pesanan[nama.title()]["jarak"] = jarak_baru
        
        if pesanan[nama.title()]["kendaraan"].lower() == "mobil":
            pesanan[nama.title()]["harga"] = jarak_baru * 10000
        else:
            pesanan[nama.title()]["harga"] = jarak_baru * 5000
        
        print("Jarak & harga berhasil diperbarui.")
    
    elif pilihan == "2":
        while True:
            try:
                harga_baru = float(input("Harga baru: "))
                if harga_baru < 0:
                    print("Harga tidak boleh negatif. Coba lagi.")
                    continue
                break
            except ValueError:
                print("Harga harus berupa angka. Coba lagi.")
                continue
        
        pesanan[nama.title()]["harga"] = harga_baru
        print("Harga berhasil diubah.")

def update_pesanan_user():
    tampilkan_pesanan()
    if not pesanan:
        return
    
    while True:
        sopir = []
        for i in pesanan.keys():
            sopir.append(i.lower())

        nama = input("\nMasukkan nama sopir yang ingin diubah pesanannya: ").strip()
        if nama.lower() not in sopir:
            print("Pesanan tidak ditemukan!")
            return
        break
    
    print("\n1. Ubah jarak")
    
    while True:
        pilihan = input("Pilih nomor menu: ").strip()
        if pilihan not in ["1", "2"]:
            print("Pilihan tidak valid! Pilih 1 atau 2.")
            continue
        break
    
    if pilihan == "1":
        while True:
            try:
                jarak_baru = float(input("Jarak baru (km): "))
                if jarak_baru <= 0:
                    print("Jarak harus lebih dari 0. Coba lagi.")
                    continue
                break
            except ValueError:
                print("Jarak harus berupa angka. Coba lagi.")
                continue
        
        pesanan[nama.title()]["jarak"] = jarak_baru
        
        if pesanan[nama.title()]["kendaraan"].lower() == "mobil":
            pesanan[nama.title()]["harga"] = jarak_baru * 10000
        else:
            pesanan[nama.title()]["harga"] = jarak_baru * 5000
        
        print("Jarak & harga berhasil diperbarui.")

def selesaikan_pesanan():
    tampilkan_pesanan()
    if not pesanan:
        return
    
    while True:
        sopir = []
        for i in pesanan.keys():
            sopir.append(i.lower())

        nama = input("\nMasukkan nama sopir yang pesanannya ingin diselesaikan: ").strip()
        if nama.lower() not in sopir:
            print("Pesanan tidak ditemukan!")
            return
        break
    
    daftar_sopir[nama.title()][2] = "tersedia"
    
    del pesanan[nama.title()]
    
    print("Pesanan berhasil diselesaikan! Status sopir diubah ke tersedia.")

def tampilkan_struk():
    for key, item in struk.items():
        print("========= STRUK PESANAN ==========")
        print(f"Nama Sopir: {key} ")
        print(f"Kendaraan: {item["kendaraan"]}")
        print(f"Plat: {item["plat"]}")
        print(f"Jrak: {item["jarak"]}")
        print(f"Nama pemesan: {item["nama pemesan"]}")
        print(f"Harga: {item["harga"]}")

def cari_sopir_kendaraan():
    while True:
        jenis = input("\nCari jenis kendaraan (Mobil/Motor): ").strip().lower()
        if jenis not in ["mobil", "motor"]:
            print("Jenis kendaraan harus 'Mobil' atau 'Motor'. Coba lagi.")
            continue
        break
    
    print(f"\nHasil pencarian untuk {jenis.capitalize()}:")
    
    found = False
    for nama, data in daftar_sopir.items():
        if data[0].lower() == jenis:
            print(f"- {nama}: {data[0]} ({data[1]}) - {data[2]}")
            found = True
    
    if not found:
        print("Tidak ada sopir dengan jenis kendaraan tersebut.")

def statistik_kendaraan():
    print("\n=== JUMLAH SOPIR PER KENDARAAN ===")
    
    stat = {}
    for _, data in daftar_sopir.items():
        jenis = data[0]
        stat[jenis] = stat.get(jenis, 0) + 1

    if not stat:
        print("Tidak ada data sopir.")
        return
    
    for jenis, total in stat.items():
        print(f"{jenis}: {total} sopir")

def buat_akun():
    print("======= BUAT AKUN ADMIN =======")
    user = input("Masukan username baru ")
    pwd = input("Masukan password baru ")
    akun["username"] = user
    akun["password"] = pwd

while True:
    masukan = input("Login sebagai admin / user: ").strip().lower()
    if masukan in ["admin", "user"]:
        break
    print("Login harus 'admin' atau 'user'. Coba lagi.")

if masukan == "admin":
    while True:
        while True:
            pilihan = input("login / buat akun baru ").lower()
            if pilihan in ["login", "buat akun baru"]:
                break
            print("Pilihan hanya (login / buat akun baru)")
            
        if pilihan == "buat akun baru":
            buat_akun()
            while True:
                print("====== MASUKKAN USERNAME DAN PASSWORD ======")
                username = input("masukkan username: ").strip()
                password = input("masukkan password: ").strip()

                if username == akun["username"] and password == akun["password"]:
                    print("Login berhasil!")
                    break
                else:
                    print("Username atau password salah. Coba lagi.")
            break

        if pilihan == "login":
            if not akun:
                print("Anda masih belum memiliki akun silahkan membuat terlebih dahulu")
                buat_akun()
                print("====== MASUKKAN USERNAME DAN PASSWORD ======")
            while True:
                username = input("masukkan username: ").strip()
                password = input("masukkan password: ").strip()

                if username == akun["username"] and password == akun["password"]:
                    print("Login berhasil!")
                    break
                else:
                    print("Username atau password salah. Coba lagi.")
            break
            
  
    while True:
        print("\n========= MENU UTAMA ADMIN =========")
        print("1. Tampilkan sopir")
        print("2. Tambah sopir")
        print("3. Update sopir")
        print("4. Hapus sopir")
        print("5. Pesan transport")
        print("6. Cari sopir berdasarkan kendaraan")
        print("7. Statistik kendaraan")
        print("8. Tampilkan pesanan")
        print("9. Update pesanan")
        print("10. Selesaikan pesanan")
        print("11. keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_sopir()
        elif pilihan == "2":
            tambah_sopir()
        elif pilihan == "3":
            update_sopir()
        elif pilihan == "4":
            hapus_sopir()
        elif pilihan == "5":
            pesan_transport()
        elif pilihan == "6":
            cari_sopir_kendaraan()
        elif pilihan == "7":
            statistik_kendaraan()
        elif pilihan == "8":
            tampilkan_pesanan()
        elif pilihan == "9":
            update_pesanan_admin()
        elif pilihan == "10":
            selesaikan_pesanan()
        elif pilihan == "11":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Pilih 1-11.")

elif masukan == "user":
    while True:
        print("\n========= MENU UTAMA USER =========")
        print("1. Tampilkan sopir")
        print("2. Pesan transport")
        print("3. Cari sopir berdasarkan kendaraan")
        print("4. Statistik kendaraan")
        print("5. Tampilkan pesanan")
        print("6. Update pesanan")
        print("7. Selesaikan pesanan")
        print("8. Tampilkan Struk")
        print("9. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_sopir()
        elif pilihan == "2":
            pesan_transport()
        elif pilihan == "3":
            cari_sopir_kendaraan()
        elif pilihan == "4":
            statistik_kendaraan()
        elif pilihan == "5":
            tampilkan_pesanan()
        elif pilihan == "6":
            update_pesanan_user()
        elif pilihan == "7":
            selesaikan_pesanan()
        elif pilihan == "8":
            tampilkan_struk()
        elif pilihan == "9":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid! Pilih 1-9.")