import socket
import netifaces
import plac


class Comm:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def disconnect(self):
        self.sock.close()

    def send(self, msg):
        total_sent = 0
        msg_len = len(msg)
        while total_sent < msg_len:
            sent = self.sock.send(msg[total_sent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_sent = total_sent + sent

    def receive(self):
        chunks = []
        bytes_recd = 0
        msg_len = 512
        while bytes_recd < msg_len:
            chunk = self.sock.recv(min(msg_len - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd += len(chunk)
        return ''.join(chunks)

    def listen(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen()

        while True:
            connection, address = self.sock.accept()
            buf = connection.recv(64)
            if len(buf) > 0:
                print(buf)
                break


def ips():
    for interface in netifaces.interfaces():
        if netifaces.AF_INET in netifaces.ifaddresses(interface):
            yield from netifaces.ifaddresses(interface)[netifaces.AF_INET]


def main():
    print('interfaces:', list(ips()))
