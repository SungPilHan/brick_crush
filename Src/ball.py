from tkinter import *

class ball(object):
	def __init__(self, canvas, sp_x, sp_y, x1, y1, x2, y2):
		self.canvas = canvas
		self.starting_posX = sp_x
		self.starting_posY = sp_y
		self.starting_direction = [-3, -2, -1, 1, 2, 3]
		self.sizeX1 = x1
		self.sizeY1 = y1
		self.sizeX2 = x2
		self.sizeY2 = y2
		self.posX = random.shuffle(starting_direction)[0]
		self.posY = -3
		self.id = canvas.create_oval(x1, y1, x2, y2, fill = color)

	def draw(self, posX, posY):
		self.canvas.move(self.id, posX, posY)

	def get_id(self):
		return self.id
