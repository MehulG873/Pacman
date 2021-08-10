import socket
from _thread import *
import random
import pickle
import json
import math
import sys
import time
import ast
from cmu_112_graphics import *
from pacman import Pacman
server = "192.168.1.66"
port = 5555
masterGrid = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 16384)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")
pacmanDir = 0
ghostDir = 0
pacmanReady = False
ghostReady = True

def threaded_client(conn, player):
    global ghostDir
    global pacmanDir
    global pacmanReady
    global ghostReady   
    if player == 1:
        conn.send(str(ghostDir).encode())
        while True:
            data = (conn.recv(4096).decode())
            if data == "Ready":
                pacmanReady = True
                conn.send("ok".encode())
            elif data == "Ready?":
                conn.send(str(pacmanReady and
                              ghostReady).encode())
            else:
                pacmanDir = int(data)                
                print(pacmanDir)
                conn.send(str(ghostDir).encode())
    if player == 2:
        conn.send(str(pacmanDir).encode())
        while True:
            data = (conn.recv(4096).decode())
            if data == "Ready":
                ghostReady = True
                conn.send("ok".encode())
            elif data == "Ready?":
                conn.send(str(pacmanReady and
                              ghostReady).encode())
            else:
                ghostDir = int(data)                
                print(ghostDir)
                conn.send(str(pacmanDir).encode())

    elif player == 2:
        conn.send(pacmanDir)
player = 0
while True:
    conn, addr = s.accept()
    player += 1
    print("Connected to", addr)

    start_new_thread(threaded_client, (conn,player))