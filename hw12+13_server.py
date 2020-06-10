import socket
import threading
import time
from JIM import MessageBuilder
import log_config

enable_tracing = True
if enable_tracing:
   debug_log = open("chat_log.txt", "w", encoding='utf-8')


def log(func):
   if enable_tracing:
       def callf(*args, **kwargs):
           debug_log.write("Вызов %s: %s, %s\n" % (func.__name__, args, kwargs))
           r = func(*args, **kwargs)
           debug_log.write("%s вернула %s\n" % (func.__name__, r))
           return r

       return callf

   else:
       return func



class Server:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clients = []
    

    def __init__(self, host='localhost', port=8008):
        self.s.bind((host, port))
        log_config.My_log()


    @staticmethod
    def j_message(msg):
        msg = ascii(msg)
        print(msg)
        msg_j = MessageBuilder.encode_to_json(msg)

        return msg_j


    @staticmethod
    def send_response(client, code, alert=None):
        gen_response = MessageBuilder.create_response_message(code, alert)
        gen_response_json = gen_response.encode_to_json()
        client.send(gen_response_json.encode('ascii'))
    @log
    def run_server(self):
        quit_server = False
        
        while not quit_server:
            try:
                self.s.listen(1)
                client, addr = self.s.accept()
                print('Получен запрос на соединение от %s' % str(addr))
                self.clients.append(client)
                for client in self.clients:
                    data = client.recvfrom(1024)
                    jd_message = self.j_message(data)
                    try:
                        if jd_message.action == "presence" and (client in self.clients):
                            self.send_response(client.name, 200, "{} is currently present."
                                               .format(jd_message.client.name))
                    except:
                        self.clients.remove(client)
                        log_config.My_log()
            except Exception as ex:
                log_config.My_log()


if __name__ == '__main__':
    server = Server()
    server.run_server()


