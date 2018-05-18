#!/usr/bin/python
#-*- coding: utf-8 -*-

class Ball:
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

class Controller:
     def __init__(self):
         self.ball = None
         self.bricks = None
         self.brick = None
         self.bar = None
         self.canvas = None

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