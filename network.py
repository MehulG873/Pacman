# Modified from previous code
# Github Link:https://github.com/kgabc/Explore-Conquest
# The Purpose of this file is to assist game.py in creating a connection with a server


import socket
import json
import pickle
import ast
import time


class network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.66"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.otherDir = self.connect()

    def getOtherDir(self):
        return self.otherDir

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass
        return self.receive()

    def send(self, data):
        try:
            print(data)
            self.client.send(data.encode())
            print("sent")
        except socket.error as e:
            print(e)
        return self.receive()

    def receive(self):
        data = self.client.recv(256).decode()
        print(data)
        return data
