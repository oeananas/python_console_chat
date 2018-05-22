import socket
import threading
import time

shutdown = False
join = False


def receiving(sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except OSError:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.0.101", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

name = input("Name: ")

rT = threading.Thread(target=receiving, args=(s,))
rT.start()

while not shutdown:
    if not join:
        s.sendto((name + " >> join chat").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()

            if message != "":
                s.sendto((name + " :: " + message).encode("utf-8"), server)
            elif message == "exit":
                s.sendto((name + " << left chat").encode("utf-8"), server)
            time.sleep(0.2)
        except OSError:
            s.sendto((name + " << left chat").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
