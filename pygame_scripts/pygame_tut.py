#! /usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *      # Import necessary modules
import pygame

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']

HOST = '128.237.232.190'    # Server(Raspberry Pi) IP address
PORT = 21567
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server

screen = pygame.display.set_mode((640,400))
clock = pygame.time.Clock()

spd = 50
tmp = 'speed'
data = tmp + str(spd)  # Change the integers into strings and combine them with the string 'speed'. 
tcpCliSock.send(data)  # Send the speed data to the server(Raspberry Pi)

running = 1

#control how often we send our pulses for panning
tickBuffer = 1
currentTick = 0
panLeft = False
panRight = False
panUp = False
panDown = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = 0
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
          tcpCliSock.send('xy_home')

      if (event.key <= 127):
        key = chr(event.key)
        if key == "w":
          tcpCliSock.send('forward')
        elif key == "a":
          tcpCliSock.send('left')
        elif key == "s":
          tcpCliSock.send('backward')
        elif key == "d":
          tcpCliSock.send('right')
      else:
        if event.key == pygame.K_UP:
          panUp = True
        elif event.key == pygame.K_DOWN:
          panDown = True
        elif event.key == pygame.K_LEFT:
          panLeft = True
        elif event.key == pygame.K_RIGHT:
          panRight = True
       
    elif event.type == pygame.KEYUP:
      if (event.key <= 127):
        key = chr(event.key)
        if key == "w":
          tcpCliSock.send('stop')
        elif key == "a":
          tcpCliSock.send('home')
        elif key == "s":
          tcpCliSock.send('stop')
        elif key == "d":
          tcpCliSock.send('left')
          tcpCliSock.send('home')
      else:
        if event.key == pygame.K_UP:
          panUp = False
        elif event.key == pygame.K_DOWN:
          panDown = False
        elif event.key == pygame.K_LEFT:
          panLeft = False
        elif event.key == pygame.K_RIGHT:
          panRight = False

  
  if panLeft:
    if currentTick % tickBuffer == 0:
      tcpCliSock.send('x-')

  if panRight:
    if currentTick % tickBuffer == 0:
      tcpCliSock.send('x+')

  if panUp:
    if currentTick % tickBuffer == 0:
      tcpCliSock.send('y+')

  if panDown:
    if currentTick % tickBuffer == 0:
      tcpCliSock.send('y-')

  currentTick += 1

  clock.tick(60)

  screen.fill((0,122,122))


