import curses
#from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random inport randint

WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100

class Snake(object):
    def __init__(self):
        self.x = 'Hisss!'

    def method_a(self, foo):
        print self.x + ' ' + foo

snake = Snake()
snake.method_a('Says the snake')

class Body(object):
    def __init__(self):
        self.x = 'this is the'

    def method_a(self, foo):
        print self.x + ' ' + foo

body = Body().method_a('Body')

class Food(object):
    def __init__(self):
        self.y = 'Yum, Tasty'

    def method_a(self, foo):
        print self.y + ' ' + foo

food = Food().method_a('Food')

