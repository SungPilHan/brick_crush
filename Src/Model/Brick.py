#-*- coding: utf-8 -*-
from tkinter import *

class Brick:
    def __init__(self, canvas , X , Y ):
        self.canvas = canvas
        self.posX = X
        self.posY = Y
        self.sizeX1 = 0
        self.sizeY1 = 0
        self.sizeX2 = 50
        self.sizeY2 = 25
        self.id = self.canvas.create_rectangle(self.sizeX1,self.sizeY1,self.sizeX2,self.sizeY2,fill = 'red')
        self.canvas.move(self.id, self.posX, self.posY)

    def get_id(self):
        return self.id
