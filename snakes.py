#a random snake game by Jaedon
import turtle
import time
import random

#score
score = 0
high_score = 0

#set up screen
wn = turtle.Screen()
wn.title("A Snake Game By Jaedon")
wn.bgcolor("green")
wn.setup(width = 600, height = 600)
wn.tracer(0)
