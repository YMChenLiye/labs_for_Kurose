from socket import *



mailserver = 'smtp.163.com'
fromaddress = "c441994447@163.com"
toaddress = "441994447@qq.com"

username="YzQ0MTk5NDQ0N0AxNjMuY29t"
password="OTUwOTEw"

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,25))

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not receive from server.'

heloCommand = 'HELO Cly\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

clientSocket.sendall('AUTH LOGIN\r\n')
recv = clientSocket.recv(1024)
print recv
if (recv[:3] != '334'):
    print '334 reply not received from server'
clientSocket.sendall(username+'\r\n')
recv = clientSocket.recv(1024)
print recv
if(recv[:3] != '334'):
    print '334 reply not received from server'
clientSocket.sendall(password+'\r\n')
recv = clientSocket.recv(1024)
print recv
if(recv[:3] != '235'):
    print '235 reply not received from server'

clientSocket.sendall('MAIL FROM:<'+fromaddress+'>\r\n')
recv = clientSocket.recv(1024)
print recv
if(recv[:3] != '250'):
    print '250 reply not received from server'

clientSocket.sendall('RCPT TO:<'+toaddress+'>\r\n')
recv = clientSocket.recv(1024)
print recv
if(recv[:3] != '250'):
    print '250 reply not received from server'

clientSocket.send('DATA\r\n')
recv = clientSocket.recv(1024)
print recv
if(recv[:3] != '354'):
    print '354 reply not received from server'


msg ='from:'+fromaddress+'\r\n'
msg+='subject:'+'I love computer networks'+'\r\n'
msg+='.\r\n'

clientSocket.send(msg)

recv = clientSocket.recv(1024)
print recv
if(recv[:3] != '250'):
    print '250 reply not received from server'

clientSocket.sendall('QUIT\r\n')

clientSocket.close()


