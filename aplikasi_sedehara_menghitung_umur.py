#belajar membuat date and time
import datetime as cavin
print("-----mengecek hari umur kita sudah berapa tahun-----")
print(5*"-" + "masukkan data dengan angka bukan nomor" + 5*"-" )
inputhari = int(input("Masukkan data hari:\t"))
inputbulan = int(input("Masukkan data bulan:\t"))
inputtahun = int(input("Masukkan data tahun:\t"))

hari_bulan_tahun = cavin.date(inputtahun, inputbulan, inputhari)
print("tanggal kamu lahir adalah:", hari_bulan_tahun)
print(f"Kamu lahir di hari {hari_bulan_tahun:%A}")

hari_ini = cavin.date.today()
hari_lahir = hari_bulan_tahun
umur_kalian_adalah = hari_ini - hari_lahir
umur_bulan = (umur_kalian_adalah.days % 365) // 30
umur_tahun = umur_kalian_adalah//365
print(f"UMUR KAMU SEKARANG ADALAH {umur_tahun.days} TAHUN,{umur_bulan} BULAN ")

