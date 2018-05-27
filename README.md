# Консольный чат

Данная программа представляет собой консольный чат с поддержкой нескольких клиентов. Проект содержит два файла: server.py (для запуска сервера) и client.py (для подключения клиента к серверу). Сервер запускается на локальном хосте и ожидает подключения клиента для обмена данными по продоколу TCP/IP.
На сервере логируются все сообщения клиентов вместе с их адресами, также отображается вход в чат и выход из чата клинтов. Клиенты получают отчеты об отправке своих сообщений, а так же сообщения других клиентов.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
Запуск на Linux:

Сначала необходимо запустить сервер (файл server.py) и ввести хост(необязательно) и порт для подключения:

```bash
stanislavkostrov$ python3 /Users/stanislavkostrov/PycharmProjects/new_chat/server.py 
HOST: 
PORT: 5000
Chat server started on port 5000
192.168.0.101
```
Далее в других консольных окнах активируем двух клиентов и в качестве аргументов при запуске передаем так же хост и порт для соединения с сервером:

```bash
stanislavkostrov$ python3 /Users/stanislavkostrov/PycharmProjects/new_chat/client.py 192.168.0.101 5000
Enter your name to enter the chat > Stanislav
Connected... Start sending messages
```
```bash
stanislavkostrov$ python3 /Users/stanislavkostrov/PycharmProjects/new_chat/client.py 192.168.0.101 5000
Enter your name to enter the chat > Alexei
Connected... Start sending messages
```
Далее можно обмениваться сообщениями:

```bash
stanislavkostrov$ python3 /Users/stanislavkostrov/PycharmProjects/new_chat/client.py 192.168.0.101 5000
Enter your name to enter the chat > Alexei
Connected... Start sending messages
Stanislav :: Hello!
Hi!
OK . .

Stanislav :: Hello,world!!!
Hello, Python!
OK . .

```

```bash
stanislavkostrov$ python3 /Users/stanislavkostrov/PycharmProjects/new_chat/client.py 192.168.0.101 5000
Enter your name to enter the chat > Stanislav
Connected... Start sending messages
Hello!
OK . .

Alexei :: Hi!
Hello,world!!!
OK . .

Alexei :: Hello, Python!

```

Сервер логирует сообщения клиентов:

```bash
stanislavkostrov$ python3 /Users/stanislavkostrov/PycharmProjects/new_chat/server.py 
HOST: 
PORT: 5000
Chat server started on port 5000
192.168.0.101
Stanislav is now connected
Alexei is now connected
[Stanislav] :: Hello!
[Alexei] :: Hi!
[Stanislav] :: Hello,world!!!
[Alexei] :: Hello, Python!
```
Запуск на других операционных системах происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного тестового задания для RAIDIX (ГК Digital Design)

