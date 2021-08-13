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
ghostDir = "0"
pacmanReady = False
ghostReady = False
ghostCenter = "0"
ghostSend = "0"

def threaded_client(conn, player):
    global ghostDir
    global ghostSend
    global pacmanReady
    global ghostReady
    global ghostCenter   
    if player == 1:     
        conn.send(str(0).encode())
        while True:
            data = (conn.recv(256).decode())
            if data == "Ready":
                pacmanReady = True
                conn.send("ok".encode())
            elif data == "Ready?":
                conn.send(str(pacmanReady and
                              ghostReady).encode())
            else:
                ghostSend = data 
                conn.send(";".join([ghostDir, ghostCenter]).encode())
    if player == 2:
        conn.send(str(0).encode())
        while True:
            data = (conn.recv(128).decode())
            if data == "Ready":
                ghostReady = True
                conn.send("ok".encode())
            elif data == "Ready?":
                conn.send(str(pacmanReady and
                              ghostReady).encode())
            else:
                ghostDir, ghostCenter = data.split(";")                
                print("STUCK:" + ghostDir)
                print(len(ghostSend.encode()))
                conn.send(ghostSend.encode())

    elif player == 2:
        conn.send(pacmanDir)
player = 0
while True:
    conn, addr = s.accept()
    player += 1
    print("Connected to", addr)

    start_new_thread(threaded_client, (conn,player))