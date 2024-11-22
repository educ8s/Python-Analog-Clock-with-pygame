import pygame, sys
from clock import AnalogClock

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

pygame.init()
background_color = (225, 239, 240)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Analog Clock")

clock = pygame.time.Clock()
analog_clock = AnalogClock((300,300), 250, SCREEN_WIDTH, SCREEN_HEIGHT)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	analog_clock.update()

	window.fill(background_color)
	analog_clock.draw(window)

	pygame.display.update()
	clock.tick(60)