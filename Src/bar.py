from tkinter import *

class bar(object):
	def __init__(self, canvas, x1, y1, x2, y2, sp_x, sp_y):
		self.canvas = canvas
		self.id = canvas.create_rectangel(x1, y1, x2, y2, fill = color)
		self.canvas.move(self.id, sp_x, sp_y)

	def draw(self, posX, key_pressed):
		self.canvas.move(self.id, posX, 0)
		


	def get_id(self):
		return self.id