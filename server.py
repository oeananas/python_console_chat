import socket
import threading
import sys


# функция, регистрирующая клиента, принимающая его данные и добавляющая его в список
def accept_client():
    while True:
        # accept
        client_sock, client_add = server_socket.accept()
        name = client_sock.recv(1024)
        clients.append((name, client_sock))
        print('{} is now connected'.format(name.decode('utf-8')))
        # реализация многопоточного ожидания сообщений от клиентов
        thread_client = threading.Thread(target=broadcast_user, args=(name, client_sock))
        thread_client.start()


# функция, принимающая сообщения от клиентов и выводящаяя на экран логи
def broadcast_user(name, sock):
    while True:
        try:
            data = sock.recv(1024)
            if data:
                print("[{}] :: {}".format(name.decode('utf-8'), data.decode('utf-8')))
                b_usr(sock, name, data)
        except socket.error:
            print("\n[ Server Stopped ]")
            server_socket.send("\n[ Server Stopped ]".encode("utf-8"))
            sys.exit()


# функция, отправляющая сообщение одного клиента всем остальным
def b_usr(cs_sock, name, msg):
    for client in clients:
        if client[1] != cs_sock:
            client[1].send(name)
            client[1].send(msg)


if __name__ == '__main__':
    # список необходимых параметров для создания сокета
    RECV_BUFFER = 1024
    HOST = input('HOST: ')
    PORT = int(input('PORT: '))

    # список, где будут храниться данные о всех подключенных клиентах
    clients = []

    # создание сокета tcp/ip
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    # сервер запустился
    print("Chat server started on port " + str(PORT))
    print(socket.gethostbyname(socket.gethostname()))

# реализация многопоточного ожидания нового подключения
thread_ac = threading.Thread(target=accept_client)
thread_ac.start()
