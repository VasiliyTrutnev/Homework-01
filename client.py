import io
import socket
import threading
import time

shutdown = False
join = False


def receiving(client_name, sock):
    global shutdown
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except Exception as ex:
            print(f"Что-то пошло не так: {ex}")
            shutdown = True


def sending(client_name, sock):
    global shutdown, join
    while not shutdown:
        if not join:
            sock.sendto(f"[{client_name}] => join chat ".encode("utf-8"), server)
            join = True
        else:
            try:
                message = input("[You] :: ")

                if message:
                    sock.sendto(f"[{client_name}] :: {message}".encode("utf-8"), server)
                time.sleep(0.2)
            except Exception as ex:
                print(f"Что-то пошло не так: {ex}")
                shutdown = True


if __name__ == '__main__':
    name = input("Name: ")

    server = ('localhost', 9090)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('localhost', 0))

    recv_thread = threading.Thread(target=receiving, args=(name, s))
    recv_thread.start()
    sending(name, s)
    recv_thread.join()
