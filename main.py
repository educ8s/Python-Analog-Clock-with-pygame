import pygame, sys
from clock import AnalogClock

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

pygame.init()
background_color = (225, 239, 240)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Analog Clock")

clock = pygame.time.Clock()
analog_clock = AnalogClock((250,250), 200, SCREEN_WIDTH, SCREEN_HEIGHT)

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