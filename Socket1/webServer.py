#import socket module
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)

#prepare a sever socket

serverPort = 6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)


while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket,addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\n\n')
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\n\n')
        connectionSocket.close()

serverSocket.close()

