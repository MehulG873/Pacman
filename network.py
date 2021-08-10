import socket
import json
import pickle
import ast
import time

#####Previous Code
class network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.66"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.app = self.connect()

    def getApp(self):
        return self.app
    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass
        return self.receive()

    def send(self, data):
        try:
            print(data)
            self.client.send(pickle.dumps(data))
            print("sent")
        except socket.error as e:
            print(e)
        return self.receive()
    def receive(self):
        length = int(self.client.recv(12).decode())
        time.sleep(0.1)
        data = b""
        while len(data) < length - 2048:
            x = self.client.recv(2048)
            data += x
        data += (self.client.recv(length - len(data)))
        sendable = pickle.loads(data)
        print("received")
        return sendable

