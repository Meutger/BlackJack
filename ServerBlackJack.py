import socket
#Socket mit ipv4 und tcp
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("",50000))
#TCP listen for connections
s.listen(1)

try:
    while True:
        #warte darauf, dass Server Anfrage akzeptiert
        komm,addr=s.accept()
        while True:
            
            data=komm.recv(1024)
        
            if not data:
                komm.close()
                break
            print(f"Nachricht von {addr}: {data.decode()}")

            nachricht=f"Empfangsbestätigung {addr}: {len(data)}"
            komm.send(nachricht.encode())
finally:
    s.close()
        


