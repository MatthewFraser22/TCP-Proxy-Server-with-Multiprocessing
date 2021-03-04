
#imported library
from socket import *
import sys

#the server address to connect to 
serverName = 'www.whynohttps.com'

#binds a port number
serverPort = 80

print('Client running...')
#A TCP socket created SOCK_STREAM = TCP, AF_NET uses IPV4
clientSocket = socket(AF_INET,SOCK_STREAM)
#connects to the server address and port number
clientSocket.connect((serverName,serverPort))
#send sentence
sentence = 'GET / HTTP/1.1\r\nHost:%s\r\n\r\n' % serverName
##SEND THE SENTENCE TO THE SERVER changes the string to bytes
clientSocket.send(sentence.encode())
modSentence = clientSocket.recv(1024)
#prints the sentence 
print('From server:',modSentence.decode())
clientSocket.close()
