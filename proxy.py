from socket import *
import sys
import os
import multiprocessing

def function(tcpCliSock, addr, message):
    # Extract the filename from the given message
    # print(message.split()[1])

    # filename = message.split()[1].partition("/")[2]
    if "Referer" in message:
        tcpCliSock.close()
        return
    # print(message)

    try:
        filename = message.split()[1].replace("/", "")
    except Exception:
        print("Cannot extract request.")
        tcpCliSock.close()
        return
    # print(filename)
    fileExist = "false"
    filetouse = "./cache/" + filename
    # print(filetouse)
    try:
        print("Checking to see if file exists...")
        f = open(filetouse, "rb")
        outputdata = f.readlines()
        fileExist = "true"
        
        buf = b''
        for i in range(len(outputdata)):
            buf = buf + (outputdata[i])

        tcpCliSock.sendall(buf)
        print('Read from cache!')
        
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":

            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)

            hostn = filename.replace("www.","",1)
            if "Referer" not in message:
                try:
                    # Client connection to get missing html object
                    
                    request = "GET / HTTP/1.1\nHost: "+filename+"\n\n"
                    request = request.encode()
                    
                    c.connect((filename, 80))  
                    print("Request to " + filename + " made.")
                    c.sendall(request)  
                    
                    buffer = recvall(c)
                    print("Response from " + filename + " recieved:")
                    print(buffer)
                    print('\n')
                    status_code = int(buffer.decode().split()[1])

                    tcpCliSock.sendall(buffer)
                    if (status_code == 200):
                        tmpFile = open("./cache/" + filename,"wb")
                        tmpFile.write(buffer)
                        tmpFile.close()
                    else:
                        http_error_handle(status_code, tcpCliSock)
                except error as e :  
                    print(e)
                    print("Illegal request")
                    request = "HTTP/1.1 400 Bad Request \r\n\r\n"
                    tcpCliSock.sendall(request.encode())
            else:
                print("Attempt to redirect made.")
        else:
            # HTTP response message for file not found
            # Fill in start.
            # Fill in end.
            tcpCliSock.send("HTTP/1.0 404 sendErrorErrorError\r\n")
            tcpCliSock.send("Content-Type:text/html\r\n")
            tcpCliSock.send("\r\n")
            # Close the client and the server sockets
            c.close()
            
    tcpCliSock.close()

#recieve all function
def recvall(sock):
    buf = b''
    while True:
        line = sock.recv(512)
        buf += line
        if len(line) < 512:
            break
    return buf

#error handling function, haven't tested
def http_error_handle(status, sock):
    if (status == 301):
        request = "HTTP/1.1 301 Moved Permanently \r\n\r\n"
        request = request.encode()
        sock.sendall(request) 
    elif(status == 302):
        request = "HTTP/1.1 302 Found \r\n\r\n"
        request = request.encode()
        sock.sendall(request) 
    elif(status == 400):
        request = "HTTP/1.1 Bad Request \r\n\r\n"
        request = request.encode()
        sock.sendall(request) 
    elif(status == 404):
        request = "HTTP/1.1 404 Not Found \r\n\r\n"
        request = request.encode()
        sock.sendall(request) 
    elif(status == 500):
        request = "HTTP/1.1 500 Internal Server Error \r\n\r\n"
        request = request.encode()
        sock.sendall(request) 
    else:
        request = "HTTP/1.1 Bad Request \r\n\r\n"
        request = request.encode()
        sock.sendall(request) 


def create_cache_folder():
    if not (os.path.exists("./cache")):
        os.mkdir("./cache")
        print("Created cache folder!")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('Usage : python proxy.py server_port\n')
        sys.exit(2)
    
    port = int(sys.argv[1]) 
    
    create_cache_folder();    
    
    # Create a server socket, bind it to a port and start listening
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(('',port))
    tcpSerSock.listen(5)
    while 1:
        print('Ready to serve...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:', addr)

        message = recvall(tcpCliSock)
        message = message.decode()
        # print(message)
        p = multiprocessing.Process(target=function, args=(tcpCliSock,addr,message))
        p.daemon = True
        p.start()




