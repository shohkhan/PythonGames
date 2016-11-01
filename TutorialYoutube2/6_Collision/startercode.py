from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

'''
function checkCircCollision(r1, r2)
{
    //if pythagoras-calculated distance between middle points is smaller then combined radius:
    return Math.sqrt(Math.pow(r2.x-r1.x,2)+Math.pow(r2.y-r1.y,2)) < r1.radius+r2.radius;
}

function checkRectCollision(r1, r2){
    return !(r1.x + r1.width < r2.x || r1.y + r1.height < r2.y || r1.x > r2.x + r2.width || r1.y > r2.y + r2.height);
}
'''

class Agent():
    def __init__(self):
        self.id = -1
        self.pos = vec2d(0, 0)
        self.target = vec2d(0, 0)


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))

        self.agents = []
        self.totalagents = 10
        for i in range(self.totalagents):
            a = Agent()
            a.id = i
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
        for a in self.agents:
            for a2 in self.agents:
                if a == a2: continue

                d = a.pos.get_distance(a2.pos)
                if d < 40:
                    overlap = 40 - d
                    dir = a2.pos - a.pos
                    dir.length = overlap/2
                    if a == self.selected:
                        a2.pos = a2.pos + dir + dir
                    elif a2 == self.selected:
                        a.pos = a.pos + dir + dir
                    else:
                        a2.pos = a2.pos + dir
                        a.pos = a.pos - dir
                    a.pos[0] = int(a.pos[0])
                    a.pos[1] = int(a.pos[1])
                    a2.pos[0] = int(a2.pos[0])
                    a2.pos[1] = int(a2.pos[1])
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.selected.target = self.selected.target + vec2d(0, -1)
            self.selected.pos = self.selected.pos + vec2d(0, -1)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.selected.target = self.selected.target + vec2d(0, 1)
            self.selected.pos = self.selected.pos + vec2d(0, 1)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.selected.target = self.selected.target + vec2d(-1, 0)
            self.selected.pos = self.selected.pos + vec2d(-1, 0)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.selected.target = self.selected.target + vec2d(1, 0)
            self.selected.pos = self.selected.pos + vec2d(1, 0)

    def keyDown(self, key):
        if key == 9:    #the Tab key
            i = self.selected.id
            if i == self.totalagents - 1: i = 0
            else: i += 1
            self.selected = self.agents[i]

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
