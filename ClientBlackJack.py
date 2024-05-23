import socket

ip = input("Ip Adresse: ")
#Socket mit ipv4 und tcp
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,50000))
# Hallo
try:
    while True:
        nachricht = input ("Nachricht: ")
        s.send(nachricht.encode())
        antwort = s.recv(1024)
        print(f"Nachricht von {ip}: {antwort.decode()}")
finally:
    s.close()
