import socket
import threading
import time
from JIM import MessageBuilder

host = 'localhost'
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
quit_server = False
print("Server started")


def j_message(msg):
    msg = msg.decode('ascii')
    print(msg)
    jd_message = MessageBuilder.get_object_of_json(msg)
    return jd_message


def send_response(client, code, alert=None):
    gen_response = MessageBuilder.create_response_message(code, alert)
    gen_response_json = gen_response.encode_to_json()
    client.send(gen_response_json.encode('ascii'))


while not quit_server:
    try:
        client, addr = s.accept()
    except Exception as ex:
        print(ex)
    else:
        print('Получен запрос на соединение от %s' % str(addr))
        clients.append(client)
    finally:
        for client in clients:
            data = client.recvfrom(1024)
            jd_message = j_message(data)
            try:
                if jd_message.action == "presence" and (client in clients):
                    send_response(client, 200, "{} is currently present.".format(jd_message.user.name))
            except:
                clients.remove(client)

s.close()
