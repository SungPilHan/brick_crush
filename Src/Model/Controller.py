#!/usr/bin/python
#-*- coding: utf-8 -*-

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

