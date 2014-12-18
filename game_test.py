# python script for testing out pygame functionality

import pygame
import pygame.gfxdraw as gfx

pygame.init()
screen = pygame.display.set_mode((1000,320))
done = False

is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()



while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      is_blue = not is_blue

  clock.tick(60)
  screen.fill((0,0,0))

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]: y -= 3
  if pressed[pygame.K_DOWN]: y += 3
  if pressed[pygame.K_LEFT]: x -= 3
  if pressed[pygame.K_RIGHT]: x += 3



  if is_blue: color = (0,128,255)
  else: color = (255,100,0)


  gfx.rectangle(screen,pygame.Rect(x,y,100,200),color)

  pygame.display.flip()



