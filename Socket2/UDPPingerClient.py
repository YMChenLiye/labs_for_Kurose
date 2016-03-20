from socket import *
import time

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

clientSocket.settimeout(1)

loop = 1
while loop < 10:
    message = 'ping '+str(loop)
    clientSocket.sendto(message,(serverName,serverPort))
    time1 = time.time()
    try:
        reveived,serverAddress = clientSocket.recvfrom(1024)
        time2 = time.time()
        print time2-time1,"success"

    except timeout:
        print('timeout')

    loop = loop + 1
