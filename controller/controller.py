#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

gpio_fwd = 26
gpio_back = 19
gpio_left = 21
gpio_right = 20 

GPIO.setmode(GPIO.BCM)

# setup GPIO pins
GPIO.setup(gpio_back, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_fwd, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while 1:
  if GPIO.input(gpio_fwd):
    print 'FORWARDS'
  if GPIO.input(gpio_back):
    print 'BACKWARDS'
  if GPIO.input(gpio_left):
    print 'LEFT'
  if GPIO.input(gpio_right):
    print 'RIGHT'
