#!/usr/share/python
import socket, sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))

s.send(sys.argv[1]+"\r\n")
resposta = s.recv(1024).split()
resp = resposta[19]

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((resp,43))

s1.send(sys.argv[1]+"\r\n")

asd = s1.recv(1024)
print(asd)

