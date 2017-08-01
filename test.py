import pygame
import time


pygame.init()

display_width = 1500
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

x =  (display_width * 0.45)
y = (display_height * 0.8)
biplaneImg = pygame.image.load('biplane.png')

for i in range(100):
	pygame.display.update()
	gameDisplay.fill(white)
	gameDisplay.blit(biplaneImg, (x,y))
	x += 2
	y -= 4
	time.sleep(0.01)

pygame.quit()
quit()