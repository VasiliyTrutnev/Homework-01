import socket
import threading
import time
from JIM import MessageBuilder
import log_config
from hw12_server import log






class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, server_host='localhost', port=8008):
        self.s.connect((server_host, port))
        self.name = None

    @log
    def run_client(self):
        while True:
            self.sending("presence")
            response = self.s.recvfrom(1024)
            response, alert = self.receiving(response)
            log_config.My_log()

    @log
    def receive_data(self):
        data = None
        while data is None:
            data = self.s.recvfrom(1024)
            log_config.My_log()

    @log
    def receiving(self, response):
        response = response.decode('ascii')
        print(response)
        rec_response = MessageBuilder.get_object_of_json(response)
        print(rec_response.response)
        print(rec_response.alert)
        log_config.My_log()
        return rec_response.response, rec_response.alert

    @log
    def sending(self, type="presence"):
        if self.name is None:
            self.name = input("Your name: ")
        make_message = MessageBuilder.create_presence_message(self.name)
        make_message_json = make_message.encode_to_json(self)
        self.s.send(make_message_json.encode('ascii'))

    def quit(self):
        self.s.close()


if __name__ == '__main__':
    client = Client()
    client.run_client()
    name = client.name

    recv_thread1 = threading.Thread(target=client.run_client(), args=name)
    recv_thread2 = threading.Thread(target=client.receive_data(), args=name)
    send_thread = threading.Thread(target=client.sending())
    recv_thread1.start()
    recv_thread2.start()
    send_thread.start()
    recv_thread1.join()
    recv_thread2.join()
    send_thread.join()
