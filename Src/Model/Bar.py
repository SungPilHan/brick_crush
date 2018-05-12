#!/usr/bin/python
#-*- coding: utf-8 -*-

class Bar:
    def __init__(self, canvas, x1, y1, x2, y2, sp_x, sp_y):
        self.canvas = canvas
        self.starting_posX = sp_x
        self.starting_posY = sp_y
        self.id = canvas.create_rectangel(x1, y1, x2, y2, fill = color)
        self.sizeX1 = x1
        self.sizeY1 = y1
        self.sizeX2 = x2
        self.sizeY2 = y2

    def get_id(self):
        return self.id

