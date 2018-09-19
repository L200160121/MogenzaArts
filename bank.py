from user import akun


class Nasabah(object):
    def __init__(self, num):
        """record akun rekening"""
        self.num = num

    def set_saldo(self, saldo = 0):
        """Set saldo akun"""
        self.saldo = saldo
        return self.saldo

    def ambil(self, jumlah):
        '''Mengambil uang'''
        if jumlah > self.saldo:
            raise RuntimeError('Jumlah lebih besar daripada saldo yang tersedia')
        self.saldo -= jumlah
        return self.saldo

    def deposit(self, jumlah):
        '''Memasukkan uang pada tabungan'''
        self.saldo += jumlah
        return self.saldo

    def cek_saldo(self):
        '''Cek saldo'''
        return self.saldo

    def __str__(self):
        return str(self.num)


def transfer(akun_pertama, akun_lain, jumlah):
    '''Transfer uang'''
    akun[akun_pertama][1] -= jumlah
    akun[akun_lain][1] += jumlah
    return (akun[akun_pertama][1])
