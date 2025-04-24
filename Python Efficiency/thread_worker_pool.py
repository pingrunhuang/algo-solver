from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


def echo_client_1(q:Queue):
    client_sock, client_addr = q.get()
    print(f"got connection from: {client_addr}")
    while True:
        
        msg = client_sock.recv(65536)
        if not msg:
            break
        client_sock.sendall(msg)
    print("client closed connection")
    client_sock.close()


def echo_server_1(addr, nworkers):
    print(f"Echo server running at {addr}")
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client_1,args=(q,), daemon=True)
        t.start()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    
    while True:
        try:
            client_sock, client_addr = sock.accept()
            q.put((client_sock, client_addr))
        except KeyboardInterrupt:
            break


def echo_client_2(client_sock:socket, client_addr):
    print(f"Getting connection form {client_addr}")
    while True:
        msg = client_sock.recv(65536)
        if not msg:
            break
        client_sock.sendall(msg)
    print("client closed connection")
    client_sock.close()

def echo_server_2(addr, nworkers):
    print(f"Echo server running at {addr}")
    pool = ThreadPoolExecutor(nworkers)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client_2, client_sock, client_addr)


if __name__=="__main__":
    echo_server_2(("", 15000), 128)