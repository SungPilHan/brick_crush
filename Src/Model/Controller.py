#-*- coding: utf-8 -*-
from tkinter import *
import random
import time

class Ball(object):
        def __init__(self, canvas):
                self.canvas = canvas
                self.starting_posX = 240
                self.starting_posY = 300
                self.starting_direction = [-3, -2, -1, 1, 2, 3]
                self.sizeX1 = 10
                self.sizeY1 = 10
                self.sizeX2 = 25
                self.sizeY2 = 25
                random.shuffle(self.starting_direction)
                self.posX = self.starting_direction[0]
                self.posY = -3
                self.id = self.canvas.create_oval(self.sizeX1, self.sizeY1, self.sizeX2, self.sizeY2, fill = 'red')
                self.canvas.move(self.id, self.starting_posX, self.starting_posY)

        def set_posX(self, x):
                self.posX = x

        def set_posY(self, y):
                self.posY = y
               
        def draw(self):
                self.canvas.move(self.id, self.posX, self.posY)

        def get_id(self):
                return self.id


class Bar(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.starting_posX = 205
        self.starting_posY = 325
        self.sizeX1 = 0
        self.sizeY1 = 0
        self.sizeX2 = 100
        self.sizeY2 = 5
        self.id = self.canvas.create_rectangle(self.sizeX1, self.sizeY1, self.sizeX2, self.sizeY2, fill='green')
        self.canvas.move(self.id, self.starting_posX, self.starting_posY)
        self.posX = 0

    def draw(self):
        self.canvas.move(self.id, self.posX, 0)

    def set_posX(self, x):
            self.posX = x

    def set_posX_left(self, evt):
            self.posX = -3
            
    def set_posX_right(self, evt):
            self.posX = 3

    def get_id(self):
        return self.id

class Brick:
    def __init__(self, canvas , X , Y ):
        self.canvas = canvas
        self.posX = X
        self.posY = Y
        self.sizeX1 = 0
        self.sizeY1 = 0
        self.sizeX2 = 50
        self.sizeY2 = 25
        self.id = self.canvas.create_rectangle(self.sizeX1,self.sizeY1,self.sizeX2,self.sizeY2,fill = 'blue')
        self.canvas.move(self.id, self.posX, self.posY)

    def get_id(self):
        return self.id

class Controller:
    def __init__(self, tk):
        self.tk = tk
        self.canvas = Canvas(self.tk,width=500,height=400,bd=0,highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.ball = Ball(self.canvas)
        self.ball_id = self.ball.get_id()
        self.bar = Bar(self.canvas)
        self.bar_id = self.bar.get_id()
        self.bricks = []
        self.bias = 1
        for i in range(0, 4):
            for j in range(0, 5):
                self.bricks.append(Brick(self.canvas, 55*j+120, 30*i))
        self.canvas.bind_all('<KeyPress-Left>', self.bar.set_posX_left)
        self.canvas.bind_all('<KeyPress-Right>', self.bar.set_posX_right)

    def collision_ball_wall(self):
        ball_pos = self.canvas.coords(self.ball_id)
        if ball_pos[0] <= 0:
                self.ball.set_posX(3)
        if ball_pos[2] >= self.canvas_width:
                self.ball.set_posX(-3)
        if ball_pos[1] <= 0:
                self.ball.set_posY(3)
        if ball_pos[3] >= self.canvas_height:
                return False
        return True

    def collision_ball_bar(self):
        ball_pos = self.canvas.coords(self.ball_id)
        bar_pos = self.canvas.coords(self.bar_id)
        if ball_pos[0] >= bar_pos[0] + self.bias:
                if ball_pos[2] <= bar_pos[2] + self.bias:
                        if ball_pos[3] >= bar_pos[1]:
                                if ball_pos[3] <= bar_pos[3]:
                                        self.ball.set_posY(-3)


    def collision_ball_brick(self):
         ball_pos = self.canvas.coords(self.ball_id)
         for i in self.bricks:
                brick_pos = self.canvas.coords(i.get_id())
                
                #공이 벽돌의 밑변에 맞았을 때
                if ball_pos[1] <= brick_pos[3] and ball_pos[3] >= ball_pos[3] and ball_pos[0] >= brick_pos[0] + self.bias and ball_pos[2] <= brick_pos[2] + self.bias:
                        self.canvas.delete(i.get_id())
                        try:
                                self.bricks.remove(i)
                        except ValueError:
                                pass
                        self.ball.set_posY(3)

                #공이 벽돌의 윗변에 맞았을 때
                elif ball_pos[1] <= brick_pos[1] and ball_pos[3] >= brick_pos[1] and ball_pos[0] >= brick_pos[0] + self.bias and ball_pos[2] <= brick_pos[2] + self.bias:
                        self.canvas.delete(i.get_id())
                        try:
                                self.bricks.remove(i)
                        except ValueError:
                                pass
                        self.ball.set_posY(-3)

                #공이 벽돌의 왼쪽에 맞았을 때
                elif ball_pos[0] <= brick_pos[0] and ball_pos[2] >= brick_pos[0] and ball_pos[1] >= brick_pos[1] + self.bias and ball_pos[3] <= brick_pos[3] + self.bias:
                        self.canvas.delete(i.get_id())
                        try:
                                self.bricks.remove(i)
                        except ValueError:
                                pass
                        self.ball.set_posX(-3)

                #공이 벽돌의 오른쪽에 맞았을 때
                elif ball_pos[0] <= brick_pos[2] and ball_pos[2] >= brick_pos[2] and ball_pos[1] >= brick_pos[1] + self.bias and ball_pos[3] <= brick_pos[3] + self.bias:
                        self.canvas.delete(i.get_id())
                        try:
                                self.bricks.remove(i)
                        except ValueError:
                                pass
                        self.ball.set_posX(3)
                        
    def collision_bar_wall(self):
        bar_pos = self.canvas.coords(self.bar_id)
        if bar_pos[0] <= 0:
                self.bar.set_posX(3)
        if bar_pos[2] >= self.canvas_width:
                self.bar.set_posX(-3)

    def draw_brick(self):
#        print(len(self.bricks))
        for i in self.bricks:
                self.canvas.move(i.get_id, i.posX, i.posY)
                
    def draw_all(self):
            while self.collision_ball_wall() and len(self.bricks) != 0:
                    self.collision_bar_wall()
                    self.collision_ball_brick()
                    self.collision_ball_bar()
                    self.ball.draw()
                    self.bar.draw()
                    self.draw_brick()
                    self.tk.update()
                    time.sleep(0.005)
                    
if __name__=="__main__":
        tk = Tk()
        tk.title("test")
        tk.resizable(0,0)
        tk.wm_attributes("-topmost",1)
        cs = Controller(tk)
        print("1")
        cs.draw_all()
        print("2")

