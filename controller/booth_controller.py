#! /usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *      # Import necessary modules
import pygame
import os
import RPi.GPIO as GPIO

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']

HOST = '128.237.247.101'    # Server(Raspberry Pi) IP address
PORT = 21567
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
clock = pygame.time.Clock()

GPIO.setmode(GPIO.BCM)

spd = 99
tmp = 'speed'
data = tmp + str(spd)  # Change the integers into strings and combine them with the string 'speed'. 
tcpCliSock.send(data)  # Send the speed data to the server(Raspberry Pi)

running = 1

#control how often we send our pulses for panning
tickBuffer = 3
currentTick = 0
panLeft = False
panRight = False
panUp = False
panDown = False

moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

gpio_fwd = 6
gpio_back = 13
gpio_left = 20
gpio_right = 21
gpio_panup = 19
gpio_pandown = 26

GPIO.setup(gpio_back, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_fwd, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_panup, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_pandown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while running:
  for event in pygame.event.get():
    break
    print("this shouldnt print")
    if event.type == pygame.QUIT:
      running = 0
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
          tcpCliSock.send('xy_home')

      if (event.key <= 127):
        key = chr(event.key)
        if key == "w":
          moveForward = True
        elif key == "a":
          moveLeft = True
        elif key == "s":
          moveBackward = True
        elif key == "d":
          moveRight = True
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
          moveForward = False
        elif key == "a":
          moveLeft = False
        elif key == "s":
          moveBackward = False
        elif key == "d":
          moveRight = False
      else:
        if event.key == pygame.K_UP:
          panUp = False
        elif event.key == pygame.K_DOWN:
          panDown = False
        elif event.key == pygame.K_LEFT:
          panLeft = False
        elif event.key == pygame.K_RIGHT:
          panRight = False

  moveForward = GPIO.input(gpio_fwd)
  moveBackward = GPIO.input(gpio_back)
  moveLeft = GPIO.input(gpio_left)
  moveRight = GPIO.input(gpio_right)
  panUp =  GPIO.input(gpio_panup)
  panDown =  GPIO.input(gpio_pandown)
  
  if panUp and currentTick % tickBuffer == 0:
      tcpCliSock.send('y+')

  if panDown and currentTick % tickBuffer == 0:
      tcpCliSock.send('y-')

  if moveForward:
    tcpCliSock.send('forward')
  elif moveBackward:
    tcpCliSock.send('backward')
  else:
    tcpCliSock.send('stop')

  if moveLeft:
    tcpCliSock.send('left')
  elif moveRight:
    tcpCliSock.send('right')
  else:
    tcpCliSock.send('home')


  currentTick += 1

  clock.tick(60)



