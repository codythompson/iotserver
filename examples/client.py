# https://github.com/anecdata/Socket/blob/main/examples/udp_server_CPython.py
import socket


HOST = ""
PORT = 43211
TIMEOUT = 2
MAXBUF = 256


print("Create UDP Server Socket")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(TIMEOUT)

s.bind((HOST, PORT))

buf = 
s.sendto()
while True:
    size, addr = s.recvfrom_into(buf)
    print("Received", buf[:size], size, "bytes from", addr)

    size = s.sendto(buf[:size], addr)
    print("Sent", buf[:size], size, "bytes to", addr)