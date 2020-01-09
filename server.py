import socket
from _thread import *
import sys

server = "10.0.0.52"
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    err(e)

s.listen(2)
print("Waiting for connection\n")


def threaded_client(conn):
    conn.send(str.encode("Conned"))

    reply = ""    
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("dis\n")
                break
            else:
                print("rec ", reply)


            conn.sendall(str.encode(reply))
        except:
            break
    print("Conn closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Conn to ", addr)

    start_new_thread(threaded_client, (conn,))
