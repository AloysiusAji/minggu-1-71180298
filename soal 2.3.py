#Aloysius Gonzaga Ardhian Krisna Aji
#Universitas Kristen Duta Wacana
#71180298

'''Budi tertarik untuk melamar pekerjaan pada liburan semester yang akan berlangsung
selama 5 minggu. Gaji yang diberikan adalah gaji per jam. Total pajak yang harus budi
bayarkan dari penghasilannya selama bekerja adalah 14%. Setelah membayar pajak, budi
menghabiskan 10% dari pendapatan bersihnya untuk membeli baju dan aksesoris yang akan
digunakan pada semester baru, dan 1% untuk membeli alat tulis. Setelah membeli baju, aksesoris
dan alat tulis, Budi menggunakan 25% dari sisa uangnya untuk disedekahkan. Setiap
Rp.1000 yang Budi sedekahkan 30% nya akan diserahkan kepada anak yatim, dan sisanya akan
diserahkan ke kaum dhuafa.'''


print("=====Input=====")

gajiperjam = int(input("1. Gaji perjam yang anda inginkan: "))
jumlahjamkerja = int(input("2. Jumlah jam kerja yang akan dilakukan dalam 1 minggu:"))

pendapatannopajak = gajiperjam * jumlahjamkerja * 5
pajak = pendapatannopajak * 14 / 100
pendapatansetelahpajak = pendapatannopajak - pajak
beliaksesoris = pendapatansetelahpajak * 10 / 100
belialattulis = pendapatansetelahpajak * 1 / 100
uangsisa = pendapatansetelahpajak - beliaksesoris - belialattulis
uangsedekah = uangsisa * 25 / 100
uangyatim = uangsedekah * 30 / 100
uangdhuafa = uangsedekah - uangyatim

print("=====Output=====")

print("1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: ",pendapatannopajak)
print("2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: ",pendapatansetelahpajak)
print("3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: ",beliaksesoris)
print("4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis",belialattulis)
print("5. Jumlah uang yang akan Budi sedekahkan",uangsedekah)
print("6. Jumlah uang yang akan diterima anak yatim: ",uangyatim)
print("7. Jumlah uang yang akan diterima kaum dhuafa: ",uangdhuafa)