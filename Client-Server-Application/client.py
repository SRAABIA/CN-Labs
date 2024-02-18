import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 3345

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.connect((ip,port))

    string = input("Enter: ")
    server.send(bytes(string,'utf-8'))
    msg = server.recv(1024)
    msg = msg.decode('utf-8')
    print(f"Server: {msg}")
