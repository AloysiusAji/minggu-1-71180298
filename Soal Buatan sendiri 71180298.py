#Aloysius Gonzaga Ardhian Krisna Aji
#Universitas Kristen Duta Wacana
#71180298

#Sumber Modul

'''Martin ingin mendaftar magang di salah satu perusahaan swasta di jepang selama 2 bulan.
Martin diminta untuk menyebutkan gaji perjam yang dia inginkan, Total pajak yang harus martin
bayarkan dari penghasilannya selama bekerja adalah 15%. Setelah membayar pajak (Pendapatan bersih),
martin ingin menghabiskan 10% dari pendapatan bersihnya untuk membeli Kit Gunpla yang telah 
ia impikan sejak lama dan 30% untuk diberikan kepada orang tua. 
Setelah membeli gunpla dan menyisihkan uangnya untuk orang tua,
Martin berencana menggunakan 25% dari sisa uangnya untuk disedekahkan. 
30% nya akan diserahkan kepada gereja, dan sisanya akan
diserahkan ke panti asuhan.'''

gajiperjam = int(input("1. Gaji perjam yang diinginkan martin: "))
jumlahjamkerja = int(input("2. Jumlah jam kerja yang akan dilakukan dalam 1 minggu:"))

pendapatannopajak = gajiperjam * jumlahjamkerja * 8
pajak = pendapatannopajak * 15 / 100
pendapatansetelahpajak = pendapatannopajak - pajak
beligunpla = pendapatansetelahpajak * 10 / 100
buatortu = pendapatansetelahpajak * 30 / 100
uangsisa = pendapatansetelahpajak - beligunpla - buatortu
uangsedekah = uangsisa * 25 / 100
uanggereja = uangsedekah * 30 / 100
uangpanti = uangsedekah - uanggereja

print("=====Output=====")

print("1. Pendapatan Martin sebelum melakukan pembayaran pajak: ",pendapatannopajak)
print("2. Pendapatan Martin setelah melakukan pembayaran pajak: ",pendapatansetelahpajak)
print("3. Jumlah uang yang akan Martin habiskan untuk membeli Kit Gunpla: ",beligunpla)
print("4. Jumlah uang yang akan Martin berikan kepada orang tua: ",buatortu)
print("5. Jumlah uang yang akan Martin sedekahkan",uangsedekah)
print("6. Jumlah uang yang akan diterima gereja: ",uanggereja)
print("7. Jumlah uang yang akan diterima panti asuhan: ",uangpanti)