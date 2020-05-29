import socket
import threading
import time
from JIM import MessageBuilder


class Server:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, host='localhost', port=9090):
        self.s.bind((host, port))
        print("Server started")

    def run_server(self):
        quit_server = False
        clients = []

        while not quit_server:
            try:
                client, addr = self.s.accept()
            except Exception as ex:
                pass
            else:
                print('Получен запрос на соединение от %s' % str(addr))
                self.clients.append(client)
            finally:
                for client in clients:
                    data = client.recvfrom(1024)
                    jd_message = self.j_message(data)
                    try:
                        if jd_message.action == "presence" and (client in clients):
                            self.send_response(client, 200, "{} is currently present.".format(jd_message.user.name))
                    except:
                        self.clients.remove(client)

    @staticmethod
    def j_message(msg):
        msg = msg.decode('ascii')
        print(msg)
        jd_message = MessageBuilder.get_object_of_json(msg)
        return jd_message

    @staticmethod
    def send_response(client, code, alert=None):
        gen_response = MessageBuilder.create_response_message(code, alert)
        gen_response_json = gen_response.encode_to_json()
        client.send(gen_response_json.encode('ascii'))


if __name__ == '__main__':
    server = Server()
    server.run_server()
