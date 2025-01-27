import pygame, sys,time

pygame.init()

screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("Hello World")

color = (255,0,0)
 
# Drawing Rectangle
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60),  2)
pygame.display.flip()
i=0
while True:
   # windowSurface.fill(WHITE) 
   i=+1
   pygame.draw.rect(screen, color, pygame.Rect(30+i, 30+i, 60+i, 30+i),  2)
   pygame.display.update()

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
