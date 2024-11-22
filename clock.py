import pygame, math
from datetime import datetime
import pygame.gfxdraw 

dark_grey = (45, 45, 45)
light_grey = (229, 229, 229)
white = (255, 255, 255)

class AnalogClock:
	def __init__(self, position, size, screen_width, screen_height):
		self.position = position
		self.size = size
		self._screen_width = screen_width
		self._screen_height = screen_height
		self._minute = 0
		self._hour = 0
		self._second = 0
		self._rotation_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

	def update(self):
		time = self._get_current_time()
		self._minute = time[1]
		self._hour = time[0]
		self._second = time[2]

	def draw(self, surface):
		self._draw_face(surface)
		self._draw_hand(surface, 0.7 * self.size, 10, self._minute * 6 - 90, dark_grey)
		self._draw_hand(surface, 0.6 * self.size, 15, (self._hour + self._minute / 60) * 30 - 90, dark_grey)
		self._draw_hand(surface, self.size + 10, 5, self._second * 6 - 90, 'red', 50)
		self.draw_center(surface)

	def draw_center(self, surface):
		pygame.gfxdraw.aacircle(surface, self.position[0], self.position[1], 15, dark_grey)
		pygame.gfxdraw.filled_circle(surface, self.position[0], self.position[1], 15, dark_grey)

	def _draw_face(self, surface):
		pygame.gfxdraw.aacircle(surface, self.position[0], self.position[1], self.size, dark_grey)
		pygame.gfxdraw.filled_circle(surface, self.position[0], self.position[1], self.size, dark_grey)

		pygame.gfxdraw.aacircle(surface, self.position[0], self.position[1], self.size - 30, light_grey)
		pygame.gfxdraw.filled_circle(surface, self.position[0], self.position[1], self.size - 30, light_grey)

		pygame.gfxdraw.aacircle(surface, self.position[0], self.position[1], self.size - 40, white)
		pygame.gfxdraw.filled_circle(surface, self.position[0], self.position[1], self.size - 40, white)

		num_ticks = 12  
		tick_length = self.size

		for i in range(num_ticks):
			angle = (i / num_ticks) * 360  
			angle_rad = math.radians(angle) 
			start_radius = self.size -5  
			end_radius = start_radius - tick_length

			start_x = self.position[0] + start_radius * math.cos(angle_rad)
			start_y = self.position[1] + start_radius * math.sin(angle_rad)
			end_x = self.position[0] + end_radius * math.cos(angle_rad)
			end_y = self.position[1] + end_radius * math.sin(angle_rad)

			pygame.draw.line(surface, dark_grey, (start_x, start_y), (end_x, end_y), 10)

		pygame.gfxdraw.aacircle(surface, self.position[0], self.position[1], self.size - 60, white)
		pygame.gfxdraw.filled_circle(surface, self.position[0], self.position[1], self.size - 60, white)

	def _get_current_time(self):
		current_time = datetime.now()
		hours = current_time.hour % 12 or 12
		return (hours, current_time.minute, current_time.second)

	def _draw_hand(self, surface, hand_length, hand_width, angle, color, offset = 0):
		self._rotation_surface.fill((0, 0, 0, 0))
		rect_x = self._screen_width // 2
		rect_y = self._screen_height // 2 - hand_width // 2
		pygame.draw.rect(self._rotation_surface, color, (rect_x - offset, rect_y, hand_length, hand_width))
		rotated_hand = pygame.transform.rotate(self._rotation_surface, -angle)
		rotated_rect = rotated_hand.get_rect(center=self.position)
		surface.blit(rotated_hand, rotated_rect.topleft)