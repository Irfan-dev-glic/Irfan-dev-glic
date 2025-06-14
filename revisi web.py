class Pengguna:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Akun:
    def __init__(self, nomor_akun, pemegang_akun):
        self.nomor_akun = nomor_akun
        self.pemegang_akun = pemegang_akun
        self.saldo = 1000.0  # saldo awal, misalnya 1000

class Transaksi:
    def __init__(self, tanggal, jenis, jumlah):
        self.tanggal = tanggal
        self.jenis = jenis
        self.jumlah = jumlah

class SistemAdministrasiBank:
    def __init__(self):
        self.pengguna = {}
        self.akun = {}
        self.transaksi = []

    def tambah_pengguna(self, username, password):
        self.pengguna[username] = Pengguna(username, password)

    def tambah_akun(self, nomor_akun, pemegang_akun):
        self.akun[nomor_akun] = Akun(nomor_akun, pemegang_akun)

    def lakukan_transaksi(self, tanggal, jenis, jumlah):
        self.transaksi.append(Transaksi(tanggal, jenis, jumlah))

    def cetak_laporan(self):
        print("Laporan Transaksi:")
        for transaksi in self.transaksi:
            print(f"Tanggal: {transaksi.tanggal}, Jenis: {transaksi.jenis}, Jumlah: {transaksi.jumlah}")

    def jumlah_laporan(self):
        total = sum(transaksi.jumlah for transaksi in self.transaksi)
        print(f"Total jumlah transaksi bulan ini: {total}")

# Contoh penggunaan
sistem = SistemAdministrasiBank()
sistem.tambah_pengguna("admin", "password")
sistem.tambah_akun("12345", "John Doe")
sistem.lakukan_transaksi("2023-02-20", "Transfer", 100000)
sistem.lakukan_transaksi("2023-02-21", "Belanja", 250000)

sistem.cetak_laporan()
sistem.jumlah_laporan()
