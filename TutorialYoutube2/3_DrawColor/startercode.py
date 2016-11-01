from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform


def setColor(s, pos):
    s.drawcolor = s.screen.get_at(pos)
    pygame.draw.circle(s.screen, s.drawcolor, (500, 100), 100)


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))

        img = pygame.image.load("colors.jpg")
        #rect = img.get_rect() #(x, y, width, height)
        img = pygame.transform.scale(img, (200, 200))
        self.screen.blit(img, (0,0))
        self.drawcolor = (0, 0, 0)
        self.x = 0
        self.y = 0

    def update(self):
        pass

    def keyDown(self, key):
        pass
        
    def keyUp(self, key):
        pass

    def mouseUp(self, button, pos):
        if pos[0] <= 200 or pos[1] <= 200:
            if button == 1:
                setColor(self, pos)

    def mouseDown(self, button, pos):
        if pos[0] > 200 or pos[1] > 200:
            pygame.draw.circle(self.screen, self.drawcolor, pos, 2)
        pass

    def mouseMotion(self, buttons, pos, rel):
        if (pos[0] > 200 or pos[1] > 200) and (pos[0]-rel[0] > 200 or pos[1]-rel[1] > 200):
            if buttons[0] == 1:
                pygame.draw.line(self.screen, self.drawcolor, pos, (pos[0]-rel[0], pos[1]-rel[1]), 5)
            if buttons[1] == 1:
                #Rainbow color
                color = self.screen.get_at((self.x, self.y))
                pygame.draw.line(self.screen, color, pos, (pos[0]-rel[0], pos[1]-rel[1]), 5)

                self.x += 1
                if self.x >= 200:
                    self.x = 0
                    self.y += 5
                if self.y >= 200:
                    self.y = 0
            elif buttons[2] == 1:
                pygame.draw.circle(self.screen, (255, 255, 255), pos, 10)
            pass
        else:
            if buttons[0] == 1:
                setColor(self, pos)

    def draw(self):
        pass
        #self.screen.fill((255,255,255))


s = Starter()
s.mainLoop(40)
