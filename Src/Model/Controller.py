#!/usr/bin/python
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

class Controller:
    def __init__(self, tk):
        self.canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
        self.canvas.pack()
        self.ball = None
#        brick = Brick(self.canvas, 200, 300)
        self.bar = None
        self.bricks = []
        for i in range(0, 4):
            for j in range(0, 5):
                self.bricks.append(Brick(self.canvas, 55*j+120, 30*i+50))
                              
    def conflict_ball_wall(self, ball_id):
        pass

    def conflict_ball_bar(self, ball_id, bar_id):
        pass

    def conflict_ball_brick(self, ball_id, bricks):
        pass

    def conflict_bar_wall(self, bar_id):
        pass

    def draw_all(self, ball, bricks, bar, canvas):
        pass


tk = Tk()
tk.title("test")
tk.wm_attributes("-topmost",1)
cs = Controller(tk)
tk.update()

