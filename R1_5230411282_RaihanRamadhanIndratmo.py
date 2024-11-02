class Pegawai:
    def __init__(self, id_pegawai, nama, alamat):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.alamat = alamat

    def tampil_info(self):
        print(f"ID Pegawai: {self.id_pegawai}")
        print(f"Nama: {self.nama}")
        print(f"Alamat: {self.alamat}")


class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = 0
        self.stok = 0

    def tampil_info(self):
        print(f"Kode Produk: {self.kode_produk}")
        print(f"Nama Produk: {self.nama_produk}")
        print(f"Jenis Produk: {self.jenis_produk}")
        print(f"Harga: Rp {self.harga:,}")
        print(f"Stok: {self.stok}")


class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga, stok):
        super().__init__(kode_produk, nama_snack, "Snack")
        self.harga = harga
        self.stok = stok

    def tampil_info(self):
        super().tampil_info()
        print("Kategori: Snack")


class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga, stok):
        super().__init__(kode_produk, nama_makanan, "Makanan")
        self.harga = harga
        self.stok = stok

    def tampil_info(self):
        super().tampil_info()
        print("Kategori: Makanan")


class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga, stok):
        super().__init__(kode_produk, nama_minuman, "Minuman")
        self.harga = harga
        self.stok = stok

    def tampil_info(self):
        super().tampil_info()
        print("Kategori: Minuman")


class Transaksi:
    def __init__(self, no_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = []
        self.total_harga = 0

    def tambah_item(self, produk, jumlah):
        if produk.stok >= jumlah:
            self.detail_transaksi.append({
                'produk': produk,
                'jumlah': jumlah,
                'subtotal': produk.harga * jumlah
            })
            self.total_harga += produk.harga * jumlah
            produk.stok -= jumlah
            return True
        return False

    def tampil_struk(self):
        print("\n===== STRUK TRANSAKSI =====")
        print(f"No Transaksi: {self.no_transaksi}")
        print("\nDetail Pembelian:")
        print("-" * 50)
        for item in self.detail_transaksi:
            print(f"Produk: {item['produk'].nama_produk}")
            print(f"Jumlah: {item['jumlah']}")
            print(f"Harga Satuan: Rp {item['produk'].harga:,}")
            print(f"Subtotal: Rp {item['subtotal']:,}")
            print("-" * 50)
        print(f"\nTotal Harga: Rp {self.total_harga:,}")
        print("========================")


class SistemManajemen:
    def __init__(self):
        self.daftar_pegawai = []
        self.daftar_produk = []
        self.daftar_transaksi = []
        self.counter_transaksi = 1

    def menu_pegawai(self):
        while True:
            print("\n=== MENU MANAJEMEN PEGAWAI ===")
            print("1. Tambah Pegawai")
            print("2. Tampil Daftar Pegawai")
            print("3. Pecat Pegawai")
            print("4. Kembali ke Menu Utama")
            
            pilihan = input("\nPilih menu (1-4): ")
            
            if pilihan == "1":
                id_pegawai = input("Masukkan ID Pegawai: ")
                nama = input("Masukkan Nama Pegawai: ")
                alamat = input("Masukkan Alamat: ")
                self.tambah_pegawai(id_pegawai, nama, alamat)
            
            elif pilihan == "2":
                self.tampil_daftar_pegawai()
            
            elif pilihan == "3":
                self.tampil_daftar_pegawai()
                id_pegawai = input("Masukkan ID Pegawai yang akan dipecat: ")
                self.pecat_pegawai(id_pegawai)
            
            elif pilihan == "4":
                break
            
            else:
                print("Pilihan tidak valid")

    def menu_produk(self):
        while True:
            print("\n=== MENU MANAJEMEN PRODUK ===")
            print("1. Tambah Produk")
            print("2. Tampil Daftar Produk")
            print("3. Kembali ke Menu Utama")
            
            pilihan = input("\nPilih menu (1-3): ")
            
            if pilihan == "1":
                print("\nJenis Produk:")
                print("1. Snack")
                print("2. Makanan")
                print("3. Minuman")
                jenis = input("Pilih jenis produk (1-3): ")

                jenis_map = {"1": "snack", "2": "makanan", "3": "minuman"}
                if jenis in jenis_map:
                    kode = input("Masukkan Kode Produk: ")
                    nama = input("Masukkan Nama Produk: ")
                    try:
                        harga = int(input("Masukkan Harga: "))
                        stok = int(input("Masukkan Jumlah Stok: "))
                        self.tambah_produk(jenis_map[jenis], kode, nama, harga, stok)
                    except ValueError:
                        print("Harga dan stok harus berupa angka")
                else:
                    print("Pilihan tidak valid")
            
            elif pilihan == "2":
                self.tampil_daftar_produk()
            
            elif pilihan == "3":
                break
            
            else:
                print("Pilihan tidak valid")

    def menu_transaksi(self):
        while True:
            print("\n=== MENU TRANSAKSI ===")
            print("1. Buat Transaksi Baru")
            print("2. Kembali ke Menu Utama")
            
            pilihan = input("\nPilih menu (1-2): ")
            
            if pilihan == "1":
                transaksi = self.buat_transaksi()
                while True:
                    self.tampil_daftar_produk()
                    kode_produk = input("\nMasukkan kode produk (atau 'selesai' untuk mengakhiri): ")

                    if kode_produk.lower() == 'selesai':
                        break

                    produk = self.cari_produk(kode_produk)
                    if produk:
                        try:
                            jumlah = int(input("Masukkan jumlah: "))
                            if jumlah <= 0:
                                print("Jumlah harus lebih dari 0")
                                continue

                            if produk.stok < jumlah:
                                print(f"Stok tidak mencukupi. Stok tersedia: {produk.stok}")
                                continue

                            if transaksi.tambah_item(produk, jumlah):
                                print("Produk berhasil ditambahkan ke transaksi")
                            else:
                                print("Gagal menambahkan produk")
                        except ValueError:
                            print("Jumlah harus berupa angka")
                    else:
                        print("Produk tidak ditemukan")

                transaksi.tampil_struk()
            
            elif pilihan == "2":
                break
            
            else:
                print("Pilihan tidak valid")

    # Method lainnya tetap sama
    def tambah_pegawai(self, id_pegawai, nama, alamat):
        pegawai = Pegawai(id_pegawai, nama, alamat)
        self.daftar_pegawai.append(pegawai)
        print(f"Pegawai {nama} berhasil ditambahkan")

    def tampil_daftar_pegawai(self):
        print("\n=== DAFTAR PEGAWAI ===")
        if not self.daftar_pegawai:
            print("Belum ada pegawai terdaftar")
            return
        for pegawai in self.daftar_pegawai:
            pegawai.tampil_info()
            print()

    def pecat_pegawai(self, id_pegawai):
        for pegawai in self.daftar_pegawai:
            if pegawai.id_pegawai == id_pegawai:
                self.daftar_pegawai.remove(pegawai)
                print(f"Pegawai dengan ID {id_pegawai} berhasil dipecat")
                return
        print(f"Pegawai dengan ID {id_pegawai} tidak ditemukan")

    def tambah_produk(self, jenis, kode_produk, nama, harga, stok):
        if jenis.lower() == "snack":
            produk = Snack(kode_produk, nama, harga, stok)
        elif jenis.lower() == "makanan":
            produk = Makanan(kode_produk, nama, harga, stok)
        elif jenis.lower() == "minuman":
            produk = Minuman(kode_produk, nama, harga, stok)
        else:
            print("Jenis produk tidak valid")
            return

        self.daftar_produk.append(produk)
        print(f"{jenis.capitalize()} {nama} berhasil ditambahkan")

    def buat_transaksi(self):
        transaksi = Transaksi(f"TRX{self.counter_transaksi:03d}")
        self.counter_transaksi += 1
        self.daftar_transaksi.append(transaksi)
        return transaksi

    def tampil_daftar_produk(self):
        print("\n=== DAFTAR PRODUK ===")
        if not self.daftar_produk:
            print("Belum ada produk terdaftar")
            return
        for produk in self.daftar_produk:
            produk.tampil_info()
            print()

    def cari_produk(self, kode_produk):
        for produk in self.daftar_produk:
            if produk.kode_produk == kode_produk:
                return produk
        return None


def main():
    sistem = SistemManajemen()

    # Menambahkan beberapa data awal
    sistem.tambah_pegawai("P001", "Joko Sigma Sejati", "Jakarta")
    sistem.tambah_produk("snack", "SNK-001", "Potato Chips", 8000, 50)
    sistem.tambah_produk("makanan", "MKN-001", "Nasi Goreng", 15000, 30)
    sistem.tambah_produk("minuman", "MNM-001", "Es Teh", 5000, 100)

    while True:
        print("\n=== SISTEM MANAJEMEN PRODUK DAN TRANSAKSI ===")
        print("1. Manajemen Pegawai")
        print("2. Manajemen Produk")
        print("3. Manajemen Transaksi")
        print("4. Keluar")

        pilihan = input("\nPilih menu (1-4): ")

        if pilihan == "1":
            sistem.menu_pegawai()
        elif pilihan == "2":
            sistem.menu_produk()
        elif pilihan == "3":
            sistem.menu_transaksi()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem ini")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()