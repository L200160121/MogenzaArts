from bank import *
from os import system
from user import akun
import time


def login():
    system('cls')
    rekening = input('Masukkan nomor rekening anda: ')
    nama = input('Masukkan nama pemilik rekening ini: ')

    if rekening in akun and akun[rekening][0] == nama:
        print('Anda berhasil login')
    else:
        print('Login gagal silahkan cek kembali nomor rekening anda dan nama pemilik rekening')
        login()
    acc = Nasabah(rekening)
    acc.set_saldo(akun[rekening][1])

    print('''Plihan:
    1. Setoran
    2. Tarik Tunai
    3. Transfer Uang
    4. Cek Saldo
    Q. Logout''')

    def menu():
        pilih = (input('Masukkan pilihan anda: '))
        if pilih == '1':
            setor = int(input('Masukkan jumlah yang ingin anda setorkan: '))
            setor = abs(setor)
            akun[rekening][1] = acc.deposit(setor)
            print('Saldo anda adalah Rp', akun[rekening][1])
            menu()
        elif pilih == '2':
            tarik = int(input('Masukkan jumlah yang ingin anda tarik: '))
            tarik = abs(tarik)
            akun[rekening][1] = acc.ambil(tarik)
            print('Saldo anda adalah Rp', akun[rekening][1])
            menu()
        elif pilih == '3':
            def trf():
                jml = int(input('Masukkan jumlah yang ingin anda transfer: '))
                tujuan = input('Masukkan nomor rekening tujuan: ') or ''
                jml = abs(jml)
                print('Anda akan mengirimkan dana sejumlah {} kepada {}' \
                      .format(str(jml), akun[tujuan][0]))
                auto = input('Apakah nomor yang anda masukkan benar (y/n): ')
                if auto in ['Y', 'y']:
                    if tujuan in akun and jml < acc.saldo:
                        print('Sisa saldo anda sebelum transfer adalah Rp ', akun[rekening][1])
                        akun[rekening][1] = transfer(rekening, tujuan, jml)
                    else:
                        print('Tujuan transfer salah atau belum terdaftar, silihkan coba kembali')
                        trf()
                elif auto in ['N', 'n']:
                    print('Transaksi anda dibatalkan')
                    time.sleep(3)
                    login()
                else:
                    print('Opsi yang anda masukkan salah')
                    time.sleep(3)
                    login()

            trf()
            menu()
        elif pilih == '4':
            print('Sisa saldo anda adalah Rp ', akun[rekening][1])
            menu()
        elif pilih == 'Q' or pilih == 'q':
            login()
        else:
            menu()

    menu()
login()
