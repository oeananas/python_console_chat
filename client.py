mport socket
import sys
import threading


# функция отправки сообщений пользователю и подтверждения отправки
def send():
    try:
        while True:
            msg = input()
            if msg == 'exit':
                s.send((name + ' disconnected...').encode('utf-8'))
                exit()
            elif msg:
                s.send(msg.encode('utf-8'))
                print('OK . .\n')
            else:
                pass
    except socket.error:
        pass


# функция, принимающая сообщения от других пользователей
def receive():
    try:
        while True:
            name = s.recv(1024)
            data = s.recv(1024)
            if data:
                print(str(name.decode('utf-8')) + ' :: ' + str(data.decode('utf-8')))
            else:
                pass
    except socket.error:
        pass


if __name__ == '__main__':

    # проверка при запуске скрипта на введенные аргументы
    if len(sys.argv) < 3:
        exit('You need to enter 2 arguments: python3 client.py hostname port')

    # переменным присваиваются соответствующие значения аргументов
    host = sys.argv[1]
    port = int(sys.argv[2])

    # создание сокета
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # соединение по указанному хосту и порту
    try:
        s.connect((host, port))
    except socket.error:
        print('connection failed')
        sys.exit()

    name = input('Enter your name to enter the chat > ')
    s.send(name.encode('utf-8'))

    print('Connected... Start sending messages')

    # реализация многопоточного принятия и отправки данных чере сокет
    thread_send = threading.Thread(target=send)
    thread_send.start()

    thread_receive = threading.Thread(target=receive)
    thread_receive.start()
