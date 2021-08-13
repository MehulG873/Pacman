    Pacman is a project that replicates the famous arcade game called Pacman
but with a twist. The twist is that this is a multiplayer game where someone 
plays Pacman, but the other player gets to play as one of the ghosts. Along
with that we will have three different difficulty ghosts, and over the network
multiplayer. Pacman will go around the map eating special pellets and
increasing its score. Its adversaries are 4 ghosts of varying colors, whose
objective is to capture the pacman. 

There are two ways to run this project. If you want to play singleplayer just
run the game.py as it currently is. BUT if it wanted to be tested in multiplayer
there are a couple of modifications that need to be made. First you need to
go into server.py and network.py and look for the line with that sets the value
of self.server or server to a string of an IP Adress. You need to change this
to your local ip adress. To get your local ip address there is a guide:
https://www.avast.com/c-how-to-find-ip-address#:~:text=Open%20the%20Windows%20Start%20menu,address%20in%20the%20new%20window.
After doing so run the server.py file. Simultaneously run game.py twice for each player.
Click the Pacman Multiplayer first otherwise the game will crash. 

Modules that need to be installed:
All requirements for cmu_112_graphics.py
Pickle by using this command: pip3 install Pickle
Anyothers from this list that are not already installed:
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

There are no shortcut commands in my game as of now, but 