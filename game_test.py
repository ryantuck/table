# python script for testing out pygame functionality

# you'll need to have pygame installed. check out their site on how to get it. 

# python game_test.py
# opens pygame window. hit space to change color of rectangle. use arrows to move.


import pygame
import pygame.gfxdraw as gfx

# initialize with array size
pygame.init()
screen = pygame.display.set_mode((1000,280))
done = False

# initial shit
color = (255,0,0)
x = 30
y = 30

clock = pygame.time.Clock()

def cycleColor():
  global color
  if color == (255,0,0): color = (0,255,0)
  elif color == (0,255,0): color = (0,0,255)
  elif color == (0,0,255): color = (255,0,0)

# main loop
while not done:
  for event in pygame.event.get():

    # handle quit
    if event.type == pygame.QUIT:
      done = True

    # cycle the color of our rectangle if space bar is hit
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      cycleColor()

  # keep frame rate to 60 fps
  clock.tick(60)

  # clear screen
  screen.fill((0,0,0))

  # change x,y based on key presses
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]: y -= 3
  if pressed[pygame.K_DOWN]: y += 3
  if pressed[pygame.K_LEFT]: x -= 3
  if pressed[pygame.K_RIGHT]: x += 3


  # draw our rectangle
  gfx.rectangle(screen,pygame.Rect(x,y,100,150),color)

  # update display
  pygame.display.flip()



