# Консольный чат

Данная программа представляет собой консольный чат с поддержкой нескольких клиентов. Проект содержит два файла: server.py (для запуска сервера) и client.py (для подключения клиента к серверу). Сервер запускается на локальном хосте и ожидает подключения клиента для обмена данными по продоколу TCP/IP.
На сервере логируются все сообщения клиентов вместе с их адресами, также отображается вход в чат и выход из чата клинтов. Клиенты получают отчеты об отправке своих сообщений, а так же сообщения других клиентов.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
Запуск на Linux:

Сначала необходимо запустить сервер (файл server.py):

```bash
stanislavkostrov$ python3 server.py
[ Server Started ]
```
Далее в других консольных окнах активируем двух клиентов:

```bash
stanislavkostrov$ python3 client.py
Name: Stanislav
[>> send to server]
```
```bash
stanislavkostrov$ python3 client.py
Name: Alexei
[>> send to server]
```
Далее можно обмениваться сообщениями:

```bash
stanislavkostrov$ python3 client.py
Name: Stanislav
[>> send to server]
Alexei >> join chat
Hello!
[>> send to server]
Alexei :: Hi!
Alexei :: Hello, world!
Hello, Python!
[>> send to server]
```

```bash
stanislavkostrov$ python3 client.py
Name: Alexei
[>> send to server]
Stanislav :: Hello!
Hi!
[>> send to server]
Hello, world!
[>> send to server]
Stanislav :: Hello, Python!
```

Сервер логирует сообщения клиентов:

```bash
python3 server.py
[ Server Started ]
[192.168.0.101]=[57267] / Stanislav >> join chat
[192.168.0.101]=[65215] / Alexei >> join chat
[192.168.0.101]=[57267] / Stanislav :: Hello!
[192.168.0.101]=[65215] / Alexei :: Hi!
[192.168.0.101]=[65215] / Alexei :: Hello, world!
[192.168.0.101]=[57267] / Stanislav :: Hello, Python!
```
Запуск на других операционных системах происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного тестового задания для RAIDIX (ГК Digital Design)

