'''
Important Socket Vocabulary:

Domain: The family of protocols used as the transport mechanism (e.g., AF_INET for IPv4).
Type: The type of communication between endpoints (e.g., SOCK_STREAM for connection-oriented protocols like TCP).
Protocol: Typically zero, used to identify a variant of a protocol within a domain and type.
'''
import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 3345

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((ip,port))

    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Connection Established : IP: {address[0]} PORT: {address[1]}")

        msg = client.recv(1024)
        msg = msg.decode('utf-8')
        msg = msg.upper()
        # print(f"Client: {msg}")
        client.send(bytes(msg,'utf-8'))
        client.close()