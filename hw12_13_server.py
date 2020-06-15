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
       def callf(*args):
           debug_log.write(f"Вызов {func.__name__}: {args}\n")
           r = func(*args)
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
    @log
    def j_message(msg):

        print(msg)
        msg_j = MessageBuilder.encode_to_json(msg)
        return msg_j

    log_config.My_log()



    @staticmethod
    @log
    def send_response(client, code, alert=None):
        gen_response = MessageBuilder.create_response_message(code, alert)
        gen_response_json = gen_response.encode_to_json()
        client.send(gen_response_json.encode('ascii'))
        log_config.My_log()
    @log
    def run_server(self):
        quit_server = False
        
        while not quit_server:
            try:
                self.s.listen(99)
                client, addr = self.s.accept()
                print('Получен запрос на соединение от %s' % str(addr))
                self.clients.append(client)
                for client in self.clients:
                    data = client.recv(1024).decode('ascii')
                    jd_message = self.j_message(data)
                    try:
                        if jd_message[0] == "presence" and (client in self.clients):
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


