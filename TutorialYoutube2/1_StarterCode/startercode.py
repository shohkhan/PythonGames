from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))

    def update(self):
        pass

    def keyDown(self, key):
        pass
        
    def keyUp(self, key):
        pass

    def mouseUp(self, button, pos):
        pass

    def mouseDown(self, button, pos):
        pass

    def mouseMotion(self, buttons, pos, rel):
        pass
        
    def draw(self):
        self.screen.fill((255,255,255))
        
s = Starter()
s.mainLoop(40)
