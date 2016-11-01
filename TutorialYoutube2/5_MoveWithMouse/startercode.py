from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Agent():
    def __init__(self):
        self.pos = vec2d(0, 0)
        self.target = vec2d(0, 0)


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))

        self.agents = []
        for i in range(10):
            a = Agent()
            a.pos = vec2d(int(uniform(0, self.w)), int(uniform(0, self.h)))
            a.target = vec2d(int(uniform(0, self.w)), int(uniform(0, self.h)))
            self.agents.append(a)

        self.selected = self.agents[0]

    def update(self):
        for a in self.agents:
            if a.target != a.pos:
                dir = a.target - a.pos
                if dir.length > 1:
                    dir.length = 3
                    a.pos = a.pos + dir
                    a.pos[0] = int(a.pos[0])
                    a.pos[1] = int(a.pos[1])

    def keyDown(self, key):
        pass

    def keyUp(self, key):
        pass

    def mouseUp(self, button, pos):
        if button == 3:
            self.selected.target = vec2d(pos)
        elif button == 1:
            for a in self.agents:
                if a.pos.get_distance(vec2d(pos)) < 20:
                    self.selected = a

    def mouseDown(self, button, pos):
        pass

    def mouseMotion(self, buttons, pos, rel):
        pass

    def draw(self):
        self.screen.fill((255,255,255))

        for a in self.agents:
            pygame.draw.circle(self.screen, (255, 0, 0), a.target, 30, 1)

            pygame.draw.circle(self.screen, (0, 0, 0), a.pos, 21)

            if a == self.selected:
                pygame.draw.circle(self.screen, (200, 0, 255), a.pos, 20)
            else:
                pygame.draw.circle(self.screen, (200, 200, 255), a.pos, 20)

s = Starter()
s.mainLoop(40)
