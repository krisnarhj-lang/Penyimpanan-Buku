import os

# Nama file tempat menyimpan data buku
# Saya pakai variabel supaya mudah diingat dan diubah kalau perlu
NAMA_FILE = "data.txt"

# Fungsi 1: Untuk membaca data dari file saat program pertama kali jalan
def muat_data():
    buku_list = []
    # Cek dulu, apakah file data.txt sudah ada?
    if os.path.exists(NAMA_FILE):
        try:
            with open(NAMA_FILE, 'r') as file:
                # Baca file per baris
                for baris in file:
                    # Pecah data berdasarkan tanda pemisah '|'
                    data = baris.strip().split('|')
                    
                    # Pastikan format datanya benar (ada judul, penulis, isi)
                    if len(data) == 3:
                        # Masukkan ke dalam bentuk dictionary
                        buku_list.append({
                            'judul': data[0],
                            'penulis': data[1],
                            'isi': data[2]
                        })
        except Exception as e:
            print(f"Maaf, terjadi error saat membaca file: {e}")
            
    return buku_list

# Fungsi 2: Untuk menyimpan data ke file (setiap ada perubahan)
def simpan_data(buku_list):
    try:
        with open(NAMA_FILE, 'w') as file:
            for buku in buku_list:
                # Format penulisan: Judul|Penulis|Isi
                file.write(f"{buku['judul']}|{buku['penulis']}|{buku['isi']}\n")
    except Exception as e:
        print(f"Maaf, gagal menyimpan data: {e}")

# Fungsi 3: Menampilkan daftar semua buku
def tampilkan_buku(buku_list):
    print("\n" + "="*40)
    print("      DAFTAR BUKU TERSEDIA")
    print("="*40)
    
    # Kalau list kosong, kasih tau user
    if not buku_list:
        print("Belum ada buku tersedia. Silakan tambah buku baru.")
    else:
        # Looping untuk menampilkan setiap buku
        for i, buku in enumerate(buku_list):
            print(f"{i+1}. Judul: {buku['judul']}")
            print(f"   Penulis: {buku['penulis']}")
            print("-" * 40)

# Fungsi 4: Menambah buku baru (Input dari user)
def tambah_buku(buku_list):
    print("\n--- TAMBAH BUKU BARU ---")
    judul = input("Masukkan Judul Buku : ")
    penulis = input("Masukkan Nama Penulis: ")
    
    # Input isi buku dibuat singkat karena ini CLI
    print("Masukkan Isi/Sinopsis Buku (Singkat):")
    isi = input(">> ")
    
    # Validasi sederhana, jangan kosong
    if judul and penulis and isi:
        buku_baru = {
            'judul': judul,
            'penulis': penulis,
            'isi': isi
        }
        # Tambahkan ke list, lalu simpan ke file
        buku_list.append(buku_baru)
        simpan_data(buku_list)
        print("\n[SUCCESS] Buku berhasil ditambahkan!")
    else:
        print("\n[ERROR] Judul, Penulis, dan Isi tidak boleh kosong.")

# Fungsi 5: Membaca isi buku yang dipilih
def baca_buku(buku_list):
    # Tampilkan dulu list bukunya
    tampilkan_buku(buku_list)
    
    if not buku_list:
        return # Langsung kembali kalau tidak ada buku

    try:
        pilihan = int(input("\nPilih nomor buku yang ingin dibaca: "))
        # Cek apakah nomor yang dipilih ada di list
        if 1 <= pilihan <= len(buku_list):
            # List index dimulai dari 0, jadi kurangi 1
            buku = buku_list[pilihan - 1]
            
            print("\n" + "="*40)
            print(f"JUDUL: {buku['judul'].upper()}")
            print(f"PENULIS: {buku['penulis']}")
            print("="*40)
            print(f"\n{buku['isi']}\n")
            print("="*40)
            input("Tekan Enter untuk kembali ke menu...")
        else:
            print("[ERROR] Nomor buku tidak ditemukan.")
            
    except ValueError:
        # Kalau user input huruf, tangkap errornya
        print("[ERROR] Input harus berupa angka!")

# Fungsi 6: Menghapus data buku
def hapus_buku(buku_list):
    tampilkan_buku(buku_list)
    if not buku_list:
        return

    try:
        pilihan = int(input("\nPilih nomor buku yang ingin dihapus: "))
        if 1 <= pilihan <= len(buku_list):
            # Ambil data buku yang mau dihapus untuk pesan konfirmasi
            buku_dihapus = buku_list.pop(pilihan - 1)
            
            # Update file data.txt
            simpan_data(buku_list)
            print(f"\n[SUCCESS] Buku '{buku_dihapus['judul']}' telah dihapus.")
        else:
            print("[ERROR] Nomor buku tidak ditemukan.")
    except ValueError:
        print("[ERROR] Input harus berupa angka!")

# Program Utama (Fungsi Main)
def main():
    # Load data pertama kali
    daftar_buku = muat_data()

    # Loop utama aplikasi
    while True:
        # Bersihkan layar biar rapi (hanya jalan di terminal/command prompt)
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        print("========================================")
        print("   APLIKASI MEMBACA BUKU ONLINE (CLI)   ")
        print("========================================")
        print("1. Lihat Daftar Buku")
        print("2. Tambah Buku Baru")
        print("3. Baca Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        print("========================================")
        
        try:
            menu = input("Pilih menu (1-5): ")
            
            if menu == '1':
                tampilkan_buku(daftar_buku)
                input("\nTekan Enter untuk kembali...")
            elif menu == '2':
                tambah_buku(daftar_buku)
                input("\nTekak Enter untuk kembali...")
            elif menu == '3':
                baca_buku(daftar_buku)
            elif menu == '4':
                hapus_buku(daftar_buku)
                input("\nTekan Enter untuk kembali...")
            elif menu == '5':
                print("\nTerima kasih telah menggunakan aplikasi. Sampai jumpa!")
                break # Stop loop dan keluar program
            else:
                print("[ERROR] Pilihan tidak tersedia. Pilih 1-5.")
                input("Tekan Enter untuk coba lagi...")
                
        except Exception as e:
            print(f"Terjadi kesalahan sistem: {e}")
            input("Tekan Enter untuk melanjutkan...")

# Fungsi utamanya jalan kalau file ini dieksekusi langsung
if __name__ == "__main__":
    main() 