#! /usr/bin/env python

import pygame

screen = pygame.display.set_mode((640,400))
clock = pygame.time.Clock()

running = 1

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = 0
    elif event.type == pygame.KEYDOWN:
      key = chr(event.key)
      if key == "w":
        print("w")
      elif key == "a":
        print("a")
      elif key == "s":
        print("s")
      elif key == "d":
        print("d")

    elif event.type == pygame.KEYUP:
      key = chr(event.key)
      if key == "w":
        print("w")
      elif key == "a":
        print("a")
      elif key == "s":
        print("s")
      elif key == "d":
        print("d")


  clock.tick(50)

  screen.fill((0,122,122))
