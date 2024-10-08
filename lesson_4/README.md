## LESSON 4

<h3>Модель OSI: Семь уровней</h3>

1. <h4 style="color:blue"> Физический уровень (Physical Layer) </h4>

    - Функция: Определяет физические и электрические характеристики соединения.
    - Примеры: Кабели, разъемы, электрические сигналы, оптоволоконные линии.
    - Протоколы/Технологии: Ethernet (физические аспекты), USB, DSL.

2. <h4 style="color:blue"> Канальный уровень (Data Link Layer) </h4>

    - Функция: Обеспечивает передачу данных между узлами в одной сети, устраняет ошибки, контролирует доступ к среде передачи.
    - Примеры: MAC-адреса, коммутаторы (Switches).
    - Протоколы: Ethernet, Wi-Fi, PPP (Point-to-Point Protocol).

3. <h4 style="color:blue"> Сетевой уровень (Network Layer) </h4>

    - Функция: Маршрутизация пакетов данных между разными сетями, определение пути передачи данных.
    - Примеры: IP-адреса, маршрутизаторы (Routers).
    - Протоколы: IP (Internet Protocol), ICMP (Internet Control Message Protocol).

4. <h4 style="color:blue"> Транспортный уровень (Transport Layer) </h4>

    - Функция: Обеспечивает надежную передачу данных, управление сессиями передачи, контроль ошибок.
    - Примеры: Порты TCP/UDP.
    - Протоколы: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).

5. <h4 style="color:blue"> Сеансовый уровень (Session Layer) </h4>

    - Функция: Управляет установкой, поддержанием и завершением сеансов связи между приложениями.
    - Примеры: Сеансы данных, управление диалогами.
    - Протоколы: PPTP (Point-to-Point Tunneling Protocol), RPC (Remote Procedure Call).

6. <h4 style="color:blue"> Представительский уровень (Presentation Layer) </h4>

    - Функция: Обеспечивает преобразование данных между форматами, шифрование и дешифрование, сжатие данных.
    - Примеры: Форматы данных, шифрование SSL/TLS.
    - Протоколы: JPEG, GIF, SSL/TLS.

7. <h4 style="color:blue"> Прикладной уровень (Application Layer) </h4>

    - Функция: Предоставляет интерфейс и услуги для приложений, обеспечивая доступ к сетевым ресурсам.
    - Примеры: Веб-браузеры, почтовые клиенты.
    - Протоколы: HTTP, FTP, SMTP, DNS.
--------------
<h4>(OSI model)</h4>

- А (Application) — Прикладной
- П (Presentation) — Представительский
- С (Session) — Сеансовый
- Т (Transport) — Транспортный
- С (Network) — Сетевой
- К (Data Link) — Канальный
- Ф (Physical) — Физический

------------

**Атаки OSI**

<h4 style="color:red"> 1. Физический уровень (Physical Layer) </h4>
Атаки:

    - Перехват данных (Wiretapping): Физическое подключение к кабелю для прослушивания передаваемых данных.
    - Помехи (Interference): Использование электромагнитных помех для нарушения работы сети.
    - Физическое повреждение (Physical Damage): Нарушение работы сети путем повреждения оборудования или кабелей.
>
<h4 style="color:red">2. Канальный уровень (Data Link Layer)</h4>
Атаки:

    - MAC-спуфинг (MAC Spoofing): Подмена MAC-адреса для получения несанкционированного доступа к сети.
    - Атака "Человек посередине" (Man-in-the-Middle, MITM): Перехват и изменение трафика между двумя устройствами.
    - Атака "Петля" (Loop Attack): Создание петли в сети, что может привести к перегрузке сети и отказу в обслуживании.
>
<h4 style="color:red">3. Сетевой уровень (Network Layer)</h4>
Атаки:

    - IP-спуфинг (IP Spoofing): Подмена IP-адреса для маскировки источника атаки.
    - DDoS (Distributed Denial of Service): Перегрузка сети огромным количеством трафика, чтобы вызвать отказ в обслуживании.
    - Маршрутизационное отравление (Routing Table Poisoning): Внесение ложных записей в таблицы маршрутизации, что приводит к перенаправлению трафика через узлы злоумышленника.
>
<h4 style="color:red">4. Транспортный уровень (Transport Layer)</h4>
Атаки:

    - Сканирование портов (Port Scanning): Изучение открытых портов на устройстве для выявления уязвимостей.
    - Атака SYN Flood: Перегрузка сервера большим количеством недозавершенных запросов SYN, что приводит к отказу в обслуживании.
    - TCP-сессии перехват (TCP Session Hijacking): Захват активной TCP-сессии для перехвата данных или выполнения команд от имени пользователя.
>
<h4 style="color:red">5. Сеансовый уровень (Session Layer)</h4>
Атаки:

    - Угон сессии (Session Hijacking): Перехват активной сессии между клиентом и сервером для получения несанкционированного доступа.
    - Повторная атака (Replay Attack): Повторное воспроизведение ранее перехваченных сообщений для выполнения несанкционированных действий.
>
<h4 style="color:red">6. Представительский уровень (Presentation Layer)</h4>
Атаки:

    - Эксплойты уязвимостей форматов данных (Data Format Exploits): Использование уязвимостей в форматах данных (например, изображений или видео) для выполнения вредоносного кода.
    - Атака на шифрование (Cryptographic Attack): Попытки взлома или обхода методов шифрования, например, атаки на SSL/TLS.
>
<h4 style="color:red">7. Прикладной уровень (Application Layer)</h4>
Атаки:

    - SQL-инъекция (SQL Injection): Внедрение вредоносного SQL-кода через веб-формы для выполнения нежелательных действий с базой данных.
    - XSS (Cross-Site Scripting): Внедрение вредоносного кода в веб-страницы для выполнения его в браузерах пользователей.
    - Фишинг (Phishing): Мошенничество, направленное на получение конфиденциальной информации (например, паролей) путем обмана пользователей.

-------

1.        /26 
    - 192.168.100.0 - 192.168.100.63
    - 192.168.100.64 - 192.168.100.127
>

2.        /27
    - 192.168.100.0 - 192.168.100.31
    - 192.168.100.32 - 192.168.100.63
    - 192.168.100.64 - 192.168.100.95
    - 192.168.100.96 - 192.168.100.127
>
3.        /28
    - 192.168.100.0 - 192.168.100.15
    - 192.168.100.16 - 192.168.100.31
    - 192.168.100.32 - 192.168.100.47
    - 192.168.100.48 - 192.168.100.63
    - 192.168.100.64 - 192.168.100.79
    - 192.168.100.80 - 192.168.100.95
    - 192.168.100.96 - 192.168.100.111
    - 192.168.100.112 - 192.168.100.127
>
4.        /29 
    - 192.168.100.0 - 192.168.100.7
    - 192.168.100.8 - 192.168.100.15
    - 192.168.100.16 - 192.168.100.23
    - 192.168.100.24 - 192.168.100.31
    - 192.168.100.32 - 192.168.100.39
    - 192.168.100.40 - 192.168.100.47
    - 192.168.100.48 - 192.168.100.55
    - 192.168.100.56 - 192.168.100.63
    - 192.168.100.64 - 192.168.100.71
    - 192.168.100.72 - 192.168.100.79
    - 192.168.100.80 - 192.168.100.87
    - 192.168.100.88 - 192.168.100.95
    - 192.168.100.96 - 192.168.100.103
    - 192.168.100.104 - 192.168.100.111
    - 192.168.100.112 - 192.168.100.119
    - 192.168.100.120 - 192.168.100.127
>
5.        /30
    - 192.169.100.0/30

--------
**IPv4 to IPv6**

- 192.168.100.1 = ::ffff:с0a8.64.1
- 172.16.0.1 = ::ffff:AC.10.0.1
- 10.10.10.10 = ::ffff:0a0a:0a0a (::ffff:10.10.10.10)

--------

