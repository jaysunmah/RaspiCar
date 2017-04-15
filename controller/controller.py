#! /usr/bin/env python
# -*- coding: utf-8 -*-
from socket import * # Communicate with the CAR
import RPi.GPIO as GPIO

gpio_fwd = 26
gpio_back = 19
gpio_left = 21
gpio_right = 20 
gpio_pandown = 6

HOST = '128.237.232.190'    # Server(Raspberry Pi) IP address
PORT = 21567
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server

GPIO.setmode(GPIO.BCM)

# setup GPIO pins
GPIO.setup(gpio_back, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_fwd, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_pandown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
  moveForward = False
  moveBackward = False
  if GPIO.input(gpio_fwd):
    print 'FORWARDS'
    moveForward = True
  elif GPIO.input(gpio_back):
    print 'BACKWARDS'
    moveBackward = True

  if GPIO.input(gpio_left):
    print 'LEFT'
  if GPIO.input(gpio_right):
    print 'RIGHT'
  if GPIO.input(gpio_pandown):
    print 'RIGHT'

  if moveForward:
    tcpCliSock.send('forward')
  elif moveBackward:
    tcpCliSock.send('backward')
  else: 
    tcpCliSock.send('stop')
